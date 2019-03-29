from pyHS100 import SmartPlug
plug = SmartPlug('192.168.1.48')

while 1:
    print("Current state: %s" % plug.state)
    key = input("Control(1:ON, 0:OFF, X: END): ")

    if key == '1':
        plug.turn_on()
    elif key == '0':
        plug.turn_off()
    elif key == 'X':
        print("Program end")
        break
    else:
        print("Input error!")