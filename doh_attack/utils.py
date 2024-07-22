from scapy.all import load_layer
from scapy.sendrecv import AsyncSniffer

from doh_attack.flow_session import generate_session_class


# IP to decimal system
def IP2Number(IP):
    ip_list = IP.split('.')
    ip_number_list = []
    for item in ip_list:
        ip_number_list.append(int(item))
    return ip_number_list[0] * 16777216 + ip_number_list[1] * 65536 + ip_number_list[2] * 256 + ip_number_list[3]


def create_sniffer(input_file, input_interface, output_mode, output_file):
    assert (input_file is None) ^ (input_interface is None)

    NewFlowSession = generate_session_class(output_mode, output_file)

    if input_file is not None:
        return AsyncSniffer(offline=input_file, filter='tcp port 443', prn=None, session=NewFlowSession, store=False)
    else:
        return AsyncSniffer(iface=input_interface, filter='tcp port 443', prn=None,
                            session=NewFlowSession, store=False)


def analysePcap(input_file, output_file):
    load_layer('tls')

    sniffer = create_sniffer(input_file=input_file, input_interface=None, output_mode='flow', output_file=output_file)
    sniffer.start()

    try:
        sniffer.join()
    except KeyboardInterrupt:
        sniffer.stop()
    finally:
        sniffer.join()