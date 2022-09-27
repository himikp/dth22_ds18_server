try:
  import usocket as socket
except:
  import socket

import network
import onewire, ds18x20
from machine import Pin
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'ssid'
password = 'pass'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

ds_pin = Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
# Comment it if you are using DHT11 and uncomment the next line
#dht_pin = dht.DHT11(Pin(4)) # Uncomment it if you are using DHT11 and comment the above line

