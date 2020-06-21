from custom_gym.envs.myxpc import xpc2 as xpc


def flaps_up_full():
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
        flaps_uf = [-998, -998, -998, -998, -998, 1.0, -998]
        client.sendCTRL(flaps_uf)

def flaps_up_half():
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
        flaps_uh = [-998, -998, -998, -998, -998, 0.5, -998]
        client.sendCTRL(flaps_uh)

def flaps_neutral():
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
        flaps_n = [-998, -998, -998, -998, -998, 0, -998]
        client.sendCTRL(flaps_n)


def flaps_down_half():
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
        flaps_dh = [-998, -998, -998, -998, -998, -0.5, -998]
        client.sendCTRL(flaps_dh)


def flaps_down_full():
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
        flaps_uf = [-998, -998, -998, -998, -998, -1, -998]
        client.sendCTRL(flaps_uf)

