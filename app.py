import pandas as pd
import matplotlib as plt
import networkx as nx
import pyshark
import socket


def scan_open_ports_on_lm():
    target = 'localhost'
    port = 22

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")



def pyshark_pcap_file_reader():
    cap = pyshark.FileCapture(r'', display_filter='')
    for pkt in cap:
        print(pkt.pretty_print())
    

def analyze_network_traffic_with_pandas():
    cap = pyshark.FileCapture(r'C:\Users\asher\Downloads\tfp_capture.pcapng', display_filter='tcp')
    data = []
    
    for packet in cap:
        data.append({
            'source': packet.ip.src,
            'destination': packet.ip.dst,
            'protocol': packet.transport_layer,
            'length': packet.length
        })

    df = pd.DataFrame(data)
    print(df.head())
    print(df.groupby('protocol')['length'].sum())

