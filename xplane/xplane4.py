from time import sleep
import xplane.xpc as xpc

#
# with xpc.XPlaneConnect() as client:
#     dref = "sim/cockpit/switches/gear_handle_status"
#     value = client.getDREF(dref)
#     print("The gear handle status is " + str(value[0]))
#
#     throttlePos = "sim/cockpit2/engine/actuators/throttle_ratio"
#     value = client.getDREF(throttlePos)
#     print("The throttle position is "+ str(value[0]))
#
#     throttleUp = "sim/engines/throttle_up"
#     client.sendDREF(throttleUp, 1)
#
#     value = client.getDREF(throttlePos)
#     print("The throttle position is " + str(value[0]))
#
#     client.pauseSim(False)


def ex():
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
        posi = [37.524, -122.06899, 2500, 0, 0, 0, 1]
        client.sendPOSI(posi)

        # Set position of a non-player aircraft
        print("Setting NPC position")
        #       Lat       Lon         Alt   Pitch Roll Yaw Gear
        posi = [37.52465, -122.06899, 2500, 0, 20, 0, 1]
        client.sendPOSI(posi, 1)

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

        # Pause the sim
        print("Pausing")
        client.pauseSim(True)
        sleep(2)

        # Toggle pause state to resume
        print("Resuming")
        client.pauseSim(False)

        # Stow landing gear using a dataref
        print("Stowing gear")
        gear_dref = "sim/cockpit/switches/gear_handle_status"
        client.sendDREF(gear_dref, 0)

        # Let the sim run for a bit.
        sleep(4)

        # Make sure gear was stowed successfully
        gear_status = client.getDREF(gear_dref)
        if gear_status[0] == 0:
            print("Gear stowed")
        else:
            print("Error stowing gear")

        print("End of Python client example")


def ex2():
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

        # Get dataref value
        print('Getting dref value')
        _dref = "sim/aircraft/overflow/acf_stall_warn_alpha"

        # client.sendDREF(gear_dref, 0)

        # Make sure gear was stowed successfully
        _status = client.getDREF(_dref)
        print("dref value = ", _status)
        if isinstance(_status, list):
            print('value consists of the following entries: ')
            for x in _status:
                print('value ' + x + ' = ', _status[x])
        # if _status[0] == 0:
        #     print("Gear stowed")
        # else:
        #     print("Error stowing gear")

        print("End of Python client example")


def ex3():
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

        print("Reading file and passing datarefs to XPlane")
        f = open("../X-plane_instructions/DataRefs.txt", "r")
        index = 0
        for x in f:
            index = index + 1
            first = x.split(None, 1)
            # print("test ", first)
            if isinstance(first, list) and len(first) > 0:
                # print(first[0], "**IS WITH**", first[1])

                # Get dataref value
                # print('Getting dref value for ', first[0])
                _dref = first[0]
                _status = client.getDREF(_dref)
                print(index, first[0], "value = ", _status)

            # break
            sleep(0.001)
        f.close()

def ex4():
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

        client.sendUDP("sim/operation/quit", 1.0)



if __name__ == "__main__":
    # ex()
    # ex2()
    # ex3()
    ex4()
