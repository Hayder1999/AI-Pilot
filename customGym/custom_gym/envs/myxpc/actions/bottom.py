from custom_gym.envs.myxpc import xpc2 as xpc



def bot_left():
    print('bot_left')
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return
        bottom_l = [1, -1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(bottom_l)

def bot_mid():
    print('bot_mid')
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return
        bottom_m = [1, 0.0, -998, -998, -998, -998, -998]
        client.sendCTRL(bottom_m)

def bot_right():
    print('bot_right')
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
            return
        bottom_r = [1, 1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(bottom_r)