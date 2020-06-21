from custom_gym.envs.myxpc import xpc2 as xpc



def pedal_up_full():
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
        pedal_uf = [-998, -998, 1.0, -998, -998, -998, -998]
        client.sendCTRL(pedal_uf)

def pedal_up_half():
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
        pedal_uh = [-998, -998, 0.5, -998, -998, -998, -998]
        client.sendCTRL(pedal_uh)

def pedal_neutral():
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
        pedal_n = [-998, -998, 0.0, -998, -998, -998, -998]
        client.sendCTRL(pedal_n)


def pedal_down_half():
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
        pedal_dh = [-998, -998, -0.5, -998, -998, -998, -998]
        client.sendCTRL(pedal_dh)


def pedal_down_full():
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
        pedal_uf = [-998, -998, -1.0, -998, -998, -998, -998]
        client.sendCTRL(pedal_uf)

