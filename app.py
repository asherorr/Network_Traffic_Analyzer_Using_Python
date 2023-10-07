import pandas as pd
import matplotlib as plt
import networkx as nx
import pyshark


def pyshark_analyzing_tool():
    cap = pyshark.FileCapture(r"C:\Users\asher\Downloads\tfp_capture.pcapng", display_filter='')
    for pkt in cap:
        print(pkt)
    


