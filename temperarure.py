 from machine import Pin
 from dht import DHT11
 d = DHT11(Pin(14))
 d.measure()
 d.temperature()
 d.humidity()
 
