from custom_gym.envs.myxpc import xpc2 as xpc



def throttle_up_full():
    print('throttle_up_full')
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
        throttle_uf = [-998, -998, -998, 1.0, -998, -998, -998]
        client.sendCTRL(throttle_uf)


def throttle_up_half():
    print('throttle_up_half')
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
        throttle_uh = [-998, -998, -998, 0.5, -998, -998, -998]
        client.sendCTRL(throttle_uh)

def throttle_up_low():
    print('throttle_up_low')
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
        throttle_uh = [-998, -998, -998, 0.2, -998, -998, -998]
        client.sendCTRL(throttle_uh)

def throttle_neutral():
    print('throttle_neutral')
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
        throttle_n = [-998, -998, -998, 0, -998, -998, -998]
        client.sendCTRL(throttle_n)

def throttle_down_half():
    print('throttle_down_half')
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
        throttle_dh = [-998, -998, -998, -0.5, -998, -998, -998]
        client.sendCTRL(throttle_dh)


def throttle_down_full():
    print('throttle_down_full')
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
        throttle_df = [-998, -998, -998, 1.0, -998, -998, -998]
        client.sendCTRL(throttle_df)

