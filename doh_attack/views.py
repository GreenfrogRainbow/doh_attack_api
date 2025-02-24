import os.path
import time

import pandas
import requests

from rest_framework.views import APIView
from doh_attack.serializer import *
from django.http import JsonResponse
from doh_attack.utils import *
from doh_attack.go_predict import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_path = os.path.join(BASE_DIR, 'static')
pcaps_path = os.path.join(source_path, 'pcaps')
csvs_path = os.path.join(source_path, 'csvs')


# Create your views here.
def baseResponse(message, success=True, code=200):
    return JsonResponse({
        'message': message,
        'success': success,
        'code': code
    })


def baseDataResponse(message, data, success=True, code=200):
    return JsonResponse({
        'message': message,
        'success': success,
        'code': code,
        'data': data
    })


def get_ip_geo_data(ip):
    input_text = ip

    url = f"https://ipinfo.io/{input_text}/json"
    result_text = {}
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'loc' in data:
                lat_long = data['loc'].split(',')
                latt = lat_long[0]
                longt = lat_long[1]
                city = data.get('city', 'N/A')
                region = data.get('region', 'N/A')
                country = data.get('country', 'N/A')
                result_text = {
                    'flag': 1,
                    'latt': latt,
                    'longt': longt,
                    'city': city,
                    'region': region,
                    'country': country
                }
            elif 'city' in data and 'country' in data:
                city = data['city']
                country = data['country']
                region = data['region']
                result_text = {
                    'flag': 1,
                    'city': city,
                    'region': region,
                    'country': country
                }
            else:
                result_text = {
                    'flag': 1,
                    'msg': "Data not found for the given input."
                }
        else:
            result_text = f"Failed to retrieve data. Status code: {response.status_code}"
    except requests.RequestException as e:
        result_text = f"Error: {e}"

    return result_text


class testData(APIView):
    def get(self, request):
        data_list = [
            {
                "id": 1,
                "content": "亚洲"
            },
            {
                "id": 2,
                "content": "中国"
            },
            {
                "id": 3,
                "content": "湖南"
            },
            {
                "id": 4,
                "content": "湘潭"
            },
            {
                "id": 6,
                "content": "雨湖区"
            },
            {
                "id": 5,
                "content": "湘潭大学"
            }
        ]
        return JsonResponse(data_list, safe=False)


class testDataa(APIView):
    def get(self, request):
        # return_data = IP2Number('113.240.75.249')
        # start_time = time.perf_counter()
        # print(start_time)
        # # 执行查询
        # IP_infos = IP2Location.objects.filter(ipFrom__lte=return_data, ipTo__gte=return_data)
        # print(IP_infos.values())
        # end_time = time.perf_counter()
        # print(end_time)
        #
        # IP_infos_values = list(IP_infos.values())
        # # 记录结束时间
        # end_time = time.perf_counter()
        # print(end_time)

        # Handle pcaps
        # for i in range(32):
        #     filename = 'tcpdump_' + str(i+1) + '.pcap'
        #     csv_name = 'flow_data_' + str(i+1) + '.csv'
        #     analysePcap(os.path.join(pcaps_path, filename), os.path.join(csvs_path, csv_name))

        analysePcap(os.path.join(pcaps_path, 'tcpdump_13.pcap'), os.path.join(csvs_path, 'flow_data_13.csv'))

        # predict test

        return baseDataResponse(message='success', data='IP_infos')


class testPredict(APIView):
    def get(self, request):
        data = request.query_params
        file_id = data.get('file_id')
        file_name = 'flow_data_' + str(file_id) + '.csv'
        isDoH, y_pred = doh_predict(file_name)

        return baseDataResponse(message='预测成功', data={ 'y_pred': y_pred[0][0] })


class handlerIp2Location(APIView):
    def post(self, request):
        data = request.data
        IPwLOCATION_file = pandas.read_csv(os.path.join(source_path, 'IP2LOCATION-LITE-DB5.csv'))

        for item in IPwLOCATION_file.iterrows():
            add_data = {
                "ipFrom": item[1][0],
                "ipTo": item[1][1],
                "countryCode": item[1][2],
                "countryName": item[1][3],
                "regionName": item[1][4],
                "cityName": item[1][5],
                "latitude": item[1][6],
                "longitude": item[1][7]
            }
            new_data = IP2locationModelSerializer(data=add_data)
            if new_data.is_valid():
                new_data.save()

        return JsonResponse({
            'msg': 'Success'
        }, safe=False)


# Flow list
"""
    @todo:
    1. 获取流量列表
    2. 处理流量信息： 流量文件 handle_file_upload + 流量信息 fileInfos
    3. 
"""
def handle_file_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        count = Files.objects.count()
        base_name, extension = os.path.splitext(uploaded_file.name)
        local_file_name = 'tcpdump_' + str(count + 1) + extension

        with open('static/pcaps/' + local_file_name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        filename = 'tcpdump_' + str(count+1) + '.pcap'
        csv_name = 'flow_data_' + str(count+1) + '.csv'
        analysePcap(os.path.join(pcaps_path, filename), os.path.join(csvs_path, csv_name))

        # 返回上传成功的响应
        filesize = os.path.getsize(os.path.join(csvs_path, csv_name))
        if filesize != 0:
            return baseDataResponse(message='File upload success', data={ 'file_id': count + 1 })
        else:
            os.remove(os.path.join(pcaps_path, filename))
            os.remove(os.path.join(csvs_path, csv_name))
            return baseDataResponse(message='Csv File is empty.', data={'file_id': 0})
    else:
        # 返回上传失败的响应
        return baseResponse(message='File upload failed', success=False, code=400)


class addFileInfos(APIView):
    def post(self, request):
        data = request.data

        filename = 'tcpdump_' + str(data['file_id']) + '.pcap'
        csv_name = 'flow_data_' + str(data['file_id']) + '.csv'
        filesize = os.path.getsize(os.path.join(pcaps_path, filename))

        IP_sting = data['destination_ip']
        IP_number = IP2Number(IP_sting)
        IP_infos = IP2Location.objects.filter(ipFrom__lte=IP_number, ipTo__gte=IP_number)
        crcName = IP_infos.values('countryName', 'regionName', 'cityName')
        location = crcName[0]['countryName'] + ' / ' + crcName[0]['regionName'] + ' / ' + crcName[0][
            'cityName']

        isDoH, y_pred = doh_predict(csv_name)
        dangerLever = 0
        if isDoH :
            if y_pred < 0.01:
                dangerLever = 3
            elif 0.01 <= y_pred < 0.05:
                dangerLever = 2
            else:
                dangerLever = 1
        else:
            dangerLever = 0

        add_data = {
            'filename': filename,
            'filesize': filesize,
            'sourceIp': data['source_ip'],
            'sourcePort': data['source_port'],
            'destinationIp': data['destination_ip'],
            'destinationPort': data['destination_port'],
            'tlsVersion': data['tls_version'],
            'clientCipherSuits': str(data['client_cipher_suits']),
            'serverAcceptedSuit': data['server_accepted_suit'],
            'clientExtensions': str(data['client_extensions']),
            'serverExtensions': str(data['server_extensions']),
            'domain': data['domain'],
            'tlsSession': data['tls_session'],
            'packetLen': data['packet_len'],
            'fingerPrint': data['finger_print'],
            'sessionTimeStamp': data['session_time_stamp'],
            'location': location,
            'dangerLever': dangerLever,
            'benignProbability': y_pred[0][0]
        }

        new_data = FilesModelSerializer(data=add_data)
        if new_data.is_valid():
            new_data.save()
            return baseResponse(message='文件添加成功')
        return baseDataResponse(message='文件添加失败', data=new_data.errors, success=False, code=400)


class getFlowInfosList(APIView):
    def get(self, request):
        data = request.query_params
        page = data.get('page')
        page = int(page)
        ids = (page - 1) * 20
        try:
            flowListInfos = Files.objects.all()[ids: ids + 20]
        except:
            flowListInfos = Files.objects.all()[ids: -1]
        data = list(flowListInfos.values())
        return_data = []
        try:
            for item in data:
                new_data = {
                    'flowID': item['id'],
                    'srcIP': item['sourceIp'],
                    'srcPort': item['sourcePort'],
                    'dstIP': item['destinationIp'],
                    'dstPort': item['destinationPort'],
                    'protocolVersion': item['tlsVersion'],
                    'fingerPrint': item['fingerPrint'],
                    'domain': item['domain'],
                    'location': item['location'],
                    'sessionTimeStamp': item['sessionTimeStamp'],
                    'dangerLever': item['dangerLever']
                }
                return_data.append(new_data)
            return baseDataResponse(message='获取成功', data=return_data)
        except Exception as e:
            return baseDataResponse(message='获取失败', data=e, success=False, code=400)


class getFlowInfos(APIView):
    def get(self, request):
        data = request.query_params
        IP = data.get('ip')
        IP_number = IP2Number(IP)

        start_time = time.perf_counter()
        print(start_time)
        # 执行查询
        rcName = IP2Location.objects.filter(ipFrom__lte=IP_number, ipTo__gte=IP_number)

        # 记录结束时间
        end_time = time.perf_counter()
        print(end_time)

        # 计算查询时间
        elapsed_time = end_time - start_time

        return baseDataResponse(message=str(elapsed_time), data=list(rcName.values()))


class getFileInfos(APIView):
    def get(self, request):
        data = request.query_params
        fileID = data.get('file_id')
        file_value = Files.objects.filter(id=fileID)

        return JsonResponse(file_value.values(), safe=False)
