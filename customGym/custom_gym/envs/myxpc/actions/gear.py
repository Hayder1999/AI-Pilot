from custom_gym.envs.myxpc import xpc2 as xpc


def gear_up():
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
        gear_u = [-998, -998, -998, 1, -998, -998, -998]
        client.sendCTRL(gear_u)

def gear_down():
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
        gear_d = [-998, -998, -998, 0, -998, -998, -998]
        client.sendCTRL(gear_d)