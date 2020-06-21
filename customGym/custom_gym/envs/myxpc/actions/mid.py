from custom_gym.envs.myxpc import xpc2 as xpc



def mid_left():
    print('mid_left')
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
        mid_l = [0.0, -1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(mid_l)

def mid_mid():
    print('mid_mid')
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
        mid_m = [0.0, 0.0, -998, -998, -998, -998, -998]
        client.sendCTRL(mid_m)

def mid_right():
    print('mid_right')
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
        mid_r = [0.0, 1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(mid_r)

