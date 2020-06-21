from custom_gym.envs.myxpc import xpc2 as xpc



def top_left():
    print('top_left')
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
        top_l = [-1.0, -1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(top_l)

def top_mid():
    print('top_mid')
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
        top_m = [-1.0, 0.0, -998, -998, -998, -998, -998]
        client.sendCTRL(top_m)


def top_right():
    print('top_right')
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
        top_r = [-1.0, 1.0, -998, -998, -998, -998, -998]
        client.sendCTRL(top_r)
