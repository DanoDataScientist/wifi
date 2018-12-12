import pywifi as pw
from pywifi import *
import time
import numpy as np


rssi = {'TP-LINK_2019': []}
rssi_m = {'TP-LINK_2019': {}}

wifi = PyWiFi()
for data in wifi.interfaces():
    print(data.name())

# get 20 rssi signal
iface = wifi.interfaces()[0]
for i in range(1, 20):
    iface.scan()
    time.sleep(5)
    results = iface.scan_results()


    for data in results:
        if data.ssid == 'TP-LINK_2019':
            rssi['TP-LINK_2019'].append(data.signal)
print(rssi)

# calculate mean,std
rssi_m['TP-LINK_2019']['mean'] = np.mean(rssi['TP-LINK_2019'])
rssi_m['TP-LINK_2019']['std'] = np.std(rssi['TP-LINK_2019'])
print(rssi_m)









