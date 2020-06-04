import socket
import struct
import binascii
import msvcrt


class XPlaneIpNotFound(Exception):
    args = "Could not find any running XPlane instance in network."


class XPlaneTimeout(Exception):
    args = "XPlane timeout."


class XPlaneUdp:

    '''
    Get data from XPlane via network.
    Use a class to implement RAI Pattern for the UDP socket. 
    '''

    # constants
    UDP_PORT = 49000
    MCAST_GRP = "239.255.1.1"
    MCAST_PORT = 49707  # (MCAST_PORT was 49000 for XPlane10)

    def __init__(self):
        # Open a UDP Socket to receive on Port 49000
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(3.0)
        # list of requested datarefs with index number
        self.datarefidx = 0
        self.datarefs = {}  # key = idx, value = dataref
        # values from xplane
        self.BeaconData = {}
        self.xplaneValues = {}
        # ============= The default GET frequency / second, 1 for testing =============
        self.defaultFreq = 1

        # values for upload to xplane           WORK IN PROGRESS
        self.datawriteIdx = 0
        self.dataWrites = {}  # key = idx, value = dataWrite

    def __del__(self):
        for _ in range(len(self.datarefs)):
            self.AddDataReader(next(iter(self.datarefs.values())), freq=0)
        for _ in range(len(self.dataWrites)):
            self.AddDataWriter(next(iter(self.dataWrites.values())), freq=0)
        self.socket.close()

    def AddDataReader(self, dataref, freq=None):
        '''
        Configure XPlane to send the dataref with a certain frequency.
        You can disable a dataref by setting freq to 0. 
        '''

        idx = -9999

        if freq == None:
            freq = self.defaultFreq

        if dataref in self.datarefs.values():
            idx = list(self.datarefs.keys())[
                list(self.datarefs.values()).index(dataref)]
            if freq == 0:
                if dataref in self.xplaneValues.keys():
                    del self.xplaneValues[dataref]
                del self.datarefs[idx]
        else:
            idx = self.datarefidx
            self.datarefs[self.datarefidx] = dataref
            self.datarefidx += 1

        cmd = b"RREF\x00"
        string = dataref.encode()
        message = struct.pack("<5sii400s", cmd, freq, idx, string)
        print("read-message",message)
        assert(len(message) == 413)
        self.socket.sendto(message, (self.BeaconData["IP"], self.UDP_PORT))

    def GetValues(self):
        try:
            # Receive packet
            data, _ = self.socket.recvfrom(
                1024)  # buffer size is 1024 bytes
            # Decode Packet
            retvalues = {}
            # * Read the Header "RREFO".
            header = data[0:5]
            if(header != b"RREF,"):  # (was b"RREFO" for XPlane10)
                print("Unknown packet: ", binascii.hexlify(data))
            else:
                # * We get 8 bytes for every dataref sent:
                #   An integer for idx and the float value.
                values = data[5:]
                lenvalue = 8
                numvalues = int(len(values)/lenvalue)
                for i in range(0, numvalues):
                    singledata = data[(5+lenvalue*i):(5+lenvalue*(i+1))]
                    (idx, value) = struct.unpack("<if", singledata)
                    # print("(idx,value)",(idx,value))
                    if idx in self.datarefs.keys():
                        # Only convert int / float
                        # convert -0.0 values to positive 0.0
                        if (isinstance(value, float) or isinstance(value, int)) and value < 0.0 and value > -0.001:
                            value = 0.0
                        retvalues[self.datarefs[idx]] = value
            self.xplaneValues.update(retvalues)
        except:
            raise XPlaneTimeout
        return self.xplaneValues

    def AddDataWriter(self, dataWrite, freq=None):      # WORK IN PROGRESS
        idx = -9999

        if freq == None:
            freq = self.defaultFreq

        if dataWrite in self.dataWrites.values():
            idx = list(self.dataWrites.keys())[
                list(self.dataWrites.values()).index(dataWrite)]
            if freq == 0:
                if dataWrite in self.xplaneValues.keys():
                    del self.xplaneValues[dataWrite]
                del self.dataWrites[idx]
        else:
            idx = self.datawriteIdx
            self.dataWrites[self.datawriteIdx] = dataWrite
            self.datawriteIdx += 1

        cmd = b"DREF\x00"
        string = dataWrite.encode()
        message = struct.pack("<5sii400s", cmd, freq, idx, string)
        assert(len(message) == 413)
        self.socket.sendto(message, (self.BeaconData["IP"], self.UDP_PORT))

    def WriteValues(self):
        try:
            # Create packet
            self.socket.send()
        except:
            raise XPlaneTimeout
        return

    def FindIp(self):
        '''
        Find the IP of XPlane Host in Network.
        It takes the first one it can find. 
        '''

        self.BeaconData = {}

        # open socket for multicast group.
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # sock.bind((self.MCAST_GRP, self.MCAST_PORT))
        sock.bind(('', self.MCAST_PORT))
        mreq = struct.pack("=4sl", socket.inet_aton(
            self.MCAST_GRP), socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        sock.settimeout(3.0)

        while not self.BeaconData:

            # receive data
            try:
                packet, sender = sock.recvfrom(15000)

                # decode data
                # * Header
                header = packet[0:5]
                if header != b"BECN\x00":
                    print("Unknown packet from "+sender[0])
                    print(str(len(packet)) + " bytes")
                    print(packet)
                    print(binascii.hexlify(packet))

                else:
                    # * Data
                    data = packet[5:21]
                    # struct becn_struct
                    # {
                    # 	uchar beacon_major_version;		// 1 at the time of X-Plane 10.40
                    # 	uchar beacon_minor_version;		// 1 at the time of X-Plane 10.40
                    # 	xint application_host_id;			// 1 for X-Plane, 2 for PlaneMaker
                    # 	xint version_number;			// 104014 for X-Plane 10.40b14
                    # 	uint role;						// 1 for master, 2 for extern visual, 3 for IOS
                    # 	ushort port;					// port number X-Plane is listening on
                    # 	xchr	computer_name[strDIM];		// the hostname of the computer
                    # };
                    beacon_major_version = 0
                    beacon_minor_version = 0
                    application_host_id = 0
                    xplane_version_number = 0
                    role = 0
                    port = 0
                    (
                        beacon_major_version,  # 1 at the time of X-Plane 10.40
                        beacon_minor_version,  # 1 at the time of X-Plane 10.40
                        application_host_id,   # 1 for X-Plane, 2 for PlaneMaker
                        xplane_version_number,  # 104014 for X-Plane 10.40b14
                        role,                  # 1 for master, 2 for extern visual, 3 for IOS
                        port,                  # port number X-Plane is listening on
                    ) = struct.unpack("<BBiiIH", data)
                    computer_name = packet[21:-1]
                    # if beacon_major_version == 1 \
                    #     and beacon_minor_version == 1 \
                    #     pipand application_host_id == 1:
                    self.BeaconData["IP"] = sender[0]
                    self.BeaconData["Port"] = port
                    self.BeaconData["hostname"] = computer_name.decode()
                    self.BeaconData["XPlaneVersion"] = xplane_version_number
                    self.BeaconData["role"] = role

            except socket.timeout:
                raise XPlaneIpNotFound()

        sock.close()
        return self.BeaconData

    def AddAbles(self, altitude=False, position=False, speed=False):
        """
        Function for instantiating the requests
        """

        if False:
            altitude = False
            position = False
            speed = False
        if altitude:
            self.AddDataReader("sim/cockpit2/gauges/indicators/altitude_ft_copilot")
            self.AddDataReader("sim/cockpit2/gauges/indicators/altitude_ft_pilot")
            self.AddDataReader("sim/cockpit2/gauges/indicators/altitude_ft_stby")
        if position:
            self.AddDataReader("sim/flightmodel/position/local_x")
            self.AddDataReader("sim/flightmodel/position/local_y")
            self.AddDataReader("sim/flightmodel/position/Prad")
            self.AddDataReader("sim/flightmodel/position/Qrad")
            self.AddDataReader("sim/flightmodel/position/Rrad")
        if speed:
            self.AddDataReader("sim/flightmodel/position/groundspeed")
            self.AddDataReader("sim/flightmodel/position/indicated_airspeed")
            self.AddDataReader("sim/flightmodel/position/indicated_airspeed2")
            self.AddDataReader("sim/flightmodel/position/true_airspeed")
        

        # Testing
        
        # self.AddDataReader("sim/world/winch/winch_speed_knots")
        # self.AddDataReader("sim/weather/wind_altitude_msl_m[0]")
        # self.AddDataReader("sim/weather/wind_direction_degt[0]")
        # self.AddDataReader("sim/weather/wind_speed_kt[0]")
        # self.AddDataReader("sim/weather/wind_altitude_msl_m[1]")
        # self.AddDataReader("sim/weather/wind_direction_degt[1]")
        # self.AddDataReader("sim/weather/wind_speed_kt[1]")
        # self.AddDataReader("sim/weather/wind_altitude_msl_m[2]")
        # self.AddDataReader("sim/weather/wind_direction_degt[2]")
        # self.AddDataReader("sim/weather/wind_speed_kt[2]")

# Example how to use:
# You need a running xplane in your network.
if __name__ == '__main__':

    xp = XPlaneUdp()

    try:
        beacon = xp.FindIp()
        print(beacon)
        print()

        # Load reader
        xp.AddAbles(altitude=True, position=True, speed=True)

        # Load writer
        # xp.AddDataWriter("sim/engines/throttle_up")

        running = True
        while running:
            # Check for 'esc' press
            if msvcrt.kbhit() and msvcrt.getch()[0] == 27:
                running = False
                break
            try:
                # print("try")
                values = xp.GetValues()
                # xp.WriteValues()
                print(values)
                print()
            except XPlaneTimeout:
                print("XPlane Timeout")

    except XPlaneIpNotFound:
        print("XPlane IP not found. Probably there is no XPlane running in your local network.")
