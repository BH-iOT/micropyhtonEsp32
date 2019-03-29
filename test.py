import machine 
import time
import esp
esp.osdebug(None)

pin=machine.Pin(2, machine.Pin.OUT)
for i in range(10):
    pin.on()
    time.sleep(0.5)
    pin.off()
    time.sleep(0.5)
    print("blink")
pin.off()

