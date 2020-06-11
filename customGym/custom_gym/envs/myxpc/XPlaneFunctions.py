from time import sleep
from custom_gym.envs.myxpc import xpc2 as xpc


def reset5():
    print("X-Plane Connect example script")
    print("Setting up simulation")
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

        # Set position of the player aircraft
        print("Setting position")
        #       Lat     Lon         Alt   Pitch Roll Yaw Gear
        posi = [31.246, -109.63, 2000, 0, 0, 0, 0]
        client.sendPOSI(posi)


        # Set angle of attack, velocity, and orientation using the DATA command
        print("Setting orientation")
        data = [ \
            [18, 0, -998, 0, -998, -998, -998, -998, -998], \
            [3, 130, 130, 130, 130, -998, -998, -998, -998], \
            [16, 0, 0, 0, -998, -998, -998, -998, -998] \
            ]
        client.sendDATA(data)

        # Set control surfaces and throttle of the player aircraft using sendCTRL
        print("Setting controls")
        ctrl = [0.0, 0.0, 0.0, 0.8]
        client.sendCTRL(ctrl)

        client.sendDREF("sim/operation/quit", 1.0)

def track_position():
    print("X-Plane Connect example script")
    print("Setting up simulation")
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
        res = client.getPOSI(0)
        print(res)

def send_waypoints():
    print("X-Plane Connect example script")
    print("Setting up simulation")
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
        res = client.getPOSI(0)
        print(res)


