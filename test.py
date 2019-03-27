import machine 
pin=machine.Pin(2, machine.Pin.OUT)
pin.on()
print("hello World")
for i in range(1, 11):
    print(i)
