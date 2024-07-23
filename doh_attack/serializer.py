from rest_framework import serializers
from doh_attack.models import *


class attackDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = attackSource
        fields = ["host", "ip", "port", "protocol", "country", "city", "organization", "banner"]


class flowDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = flowData
        fields = [
            "SourceIP",
            "DestinationIP",
            "DestinationPort",
            "TimeStamp",
            "SourcePort",
            "SourcePortPre",
            "FlowBytesReceivedPre",
            "FlowBytesSentPre",
            "Duration",
            "DurationPre",
            "FlowBytesSent",
            "FlowSentRate",
            "FlowBytesReceived",
            "FlowReceivedRate",
            "PacketLengthVariance",
            "PacketLengthStandardDeviation",
            "PacketLengthMean",
            "PacketLengthMedian",
            "PacketLengthMode",
            "PacketLengthSkewFromMedian",
            "PacketLengthSkewFromMode",
            "PacketLengthCoefficientofVariation",
            "PacketTimeVariance",
            "PacketTimeStandardDeviation",
            "PacketTimeMean",
            "PacketTimeMedian",
            "PacketTimeMode",
            "PacketTimeSkewFromMedian",
            "PacketTimeSkewFromMode",
            "PacketTimeCoefficientofVariation",
            "ResponseTimeTimeVariance",
            "ResponseTimeTimeStandardDeviation",
            "ResponseTimeTimeMean",
            "ResponseTimeTimeMedian",
            "ResponseTimeTimeMode",
            "ResponseTimeTimeSkewFromMedian",
            "ResponseTimeTimeSkewFromMode",
            "ResponseTimeTimeCoefficientofVariation",
            "Label"]


class shapDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = shapData
        fields = [
            "flowID",
            "SourcePort_score",
            "Duration_score",
            "FlowBytesSent_score",
            "FlowSentRate_score",
            "FlowBytesReceived_score",
            "FlowReceivedRate_score",
            "PacketLengthVariance_score",
            "PacketLengthStandardDeviation_score",
            "PacketLengthMean_score",
            "PacketLengthMedian_score",
            "PacketLengthMode_score",
            "PacketLengthSkewFromMedian_score",
            "PacketLengthSkewFromMode_score",
            "PacketLengthCoefficientofVariation_score",
            "PacketTimeVariance_score",
            "PacketTimeStandardDeviation_score",
            "PacketTimeMean_score",
            "PacketTimeMedian_score",
            "PacketTimeMode_score",
            "PacketTimeSkewFromMedian_score",
            "PacketTimeSkewFromMode_score",
            "PacketTimeCoefficientofVariation_score",
            "ResponseTimeTimeVariance_score",
            "ResponseTimeTimeStandardDeviation_score",
            "ResponseTimeTimeMean_score",
            "ResponseTimeTimeMedian_score",
            "ResponseTimeTimeMode_score",
            "ResponseTimeTimeSkewFromMedian_score",
            "ResponseTimeTimeSkewFromMode_score",
            "ResponseTimeTimeCoefficientofVariation_score"
        ]


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "birth", "profession", "useravatar"]


class FilesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = [
            "filename",
            "filesize",
            "sourceIp",
            "sourcePort",
            "destinationIp",
            "destinationPort",
            "tlsVersion",
            "clientCipherSuits",
            "serverAcceptedSuit",
            "clientExtensions",
            "serverExtensions",
            "domain",
            "tlsSession",
            "packetLen",
            "fingerPrint",
            "sessionTimeStamp",
            "location"
        ]


class IP2locationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP2Location
        fields = [
            "ipFrom",
            "ipTo",
            "countryCode",
            "countryName",
            "regionName",
            "cityName",
            "latitude",
            "longitude",
        ]
