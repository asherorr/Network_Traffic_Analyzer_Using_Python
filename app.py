import pandas as pd
import matplotlib as plt
import networkx as nx
import pyshark


def pyshark_analyzing_tool():
    cap = pyshark.FileCapture(r'', display_filter='')
    for pkt in cap:
        print(pkt)
    

def analyze_network_traffic_with_pandas():
    cap = pyshark.FileCapture(r'', display_filter='')
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
