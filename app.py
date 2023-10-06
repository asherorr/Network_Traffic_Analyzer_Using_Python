import pandas as pd
import matplotlib as plt
import networknx as nx

wireshark_url = "C:\Users\asher\Downloads\tfp_capture.pcapng"
wireshark_data = pd.read_csv(wireshark_url)