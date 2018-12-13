import pywifi as pw
from pywifi import *
import time
import numpy as np


rssi = {'TP-LINK_2019': [], 'MERCURY_4E9E': []}
rssi_m = {'TP-LINK_2019': {}, 'MERCURY_4E9E': {}}

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
        if data.ssid == 'MERCURY_4E9E':
            rssi['MERCURY_4E9E'].append(data.signal)
print('rssi = ')
print(rssi)

# calculate mean,std
rssi_m['TP-LINK_2019']['mean'] = np.mean(rssi['TP-LINK_2019'])
rssi_m['TP-LINK_2019']['std'] = np.std(rssi['TP-LINK_2019'])

rssi_m['MERCURY_4E9E']['mean'] = np.mean(rssi['MERCURY_4E9E'])
rssi_m['MERCURY_4E9E']['std'] = np.std(rssi['MERCURY_4E9E'])
print('rssi_m = ')
print(rssi_m)









