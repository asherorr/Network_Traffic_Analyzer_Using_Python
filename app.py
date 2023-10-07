import pandas as pd
import matplotlib as plt
import networkx as nx
import pyshark


def pyshark_analyzing_tool():
    cap = pyshark.FileCapture(r"", display_filter='')
    for pkt in cap:
        print(pkt)
    


