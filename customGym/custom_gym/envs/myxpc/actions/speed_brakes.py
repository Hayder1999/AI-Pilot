from custom_gym.envs.myxpc import xpc2 as xpc


def speedbr_up_full():
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
        head_l = [-998, -998, -998, -998, -998, -998, 1.5]
        client.sendPOSI(head_l)

def speedbr_up_1():
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
        speedbr_u1 = [-998, -998, -998, -998, -998, -998, 1.0]
        client.sendCTRL(speedbr_u1)

def speedbr_up_2():
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
        speedbr_u2 = [-998, -998, -998, -998, -998, -998, 0.5]
        client.sendCTRL(speedbr_u2)

def speedbr_neutral():
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
        speedbr_n = [-998, -998, -998, -998, -998, -998, 0]
        client.sendCTRL(speedbr_n)


def speedbr_down():
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
        speedbr_d = [-998, -998, -998, -998, -998, -998, -0.5]
        client.sendCTRL(speedbr_d)