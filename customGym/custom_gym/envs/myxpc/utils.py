from custom_gym.envs.myxpc import xpc2 as xpc
from custom_gym.envs.myxpc.actions.bottom import *
from custom_gym.envs.myxpc.actions.flaps import *
from custom_gym.envs.myxpc.actions.gear import *
from custom_gym.envs.myxpc.actions.mid import *
from custom_gym.envs.myxpc.actions.rudder_pedals import *
from custom_gym.envs.myxpc.actions.speed_brakes import *
from custom_gym.envs.myxpc.actions.throttle import *
from custom_gym.envs.myxpc.actions.top import *
import json
import time
import numpy as np
import matplotlib.pyplot as plt



def get_waypoints():
    file = open("customGym/custom_gym/envs/myxpc/take_off.json")
    data = json.load(file)
    wp = []
    for point in data:
        latitude = point['lat']
        longitude = point['lon']
        altitude = point['alt']
        wp.append([latitude,longitude,altitude])
    return wp

def set_waypoint(waypoint):
    print("Setting next waypoint")
    with xpc.XPlaneConnect() as client:
        # Verify connection
        try:
            # If X-Plane does not respond to the request, a timeout error
            # will be raised.
            client.getDREF("sim/test/test_float")
        except:
            print("Error establishing connection to X-Plane.")
            print("Exiting...")
        client.sendWYPT(1,waypoint)

def check_route():
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
        file = open("customGym/custom_gym/envs/myxpc/take_off.json")
        data = json.load(file)
        
        for points in data:
            latitude = points['lat']
            longitude = points['lon']
            altitude = points['alt']
            time.sleep(1)
            client.sendWYPT(1,[latitude,longitude,altitude])
        

def reset_wp():
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
        client.sendWYPT(3, [])

def test_waypoint():
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
        client.sendWYPT(1,[52.308099999999996,4.764170000000007, 0, 53.07139999999998,7.195830000000001,74146.982,53.633700000000005,9.985260000000011,0])
        print('sent')


def check_failures():
    print("Checking for failures")
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
        failures_dref = "sim/operation/failures/failures"
        failures = client.getDREF(failures_dref)
        for x in failures:
            if x > 0.0:
                return True
        return False 


def observation():
    print("Retrieving observation")
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
        air_speed_dref = "sim/flightmodel/position/true_airspeed"
        air_speed = client.getDREF(air_speed_dref)
        position_val = client.getPOSI(0)
        position = np.array(position_val)
        observation = np.append(position, [air_speed])
        return observation[0:3]

def calc_distance(coord1, coord2):
    print('distance')

def calc_alt(alt1, alt2):
    print('alt')

def check_goal_reached(plane_lat, plane_lon, plane_alt):
    # Setting goal
    final_lat = 52.44014358520508
    final_lon = 4.731904983520508
    final_alt = 3304.517333984375

    # Extracting the necessary observation values: lat, lon and alt
    current_lat = plane_lat 
    current_lon = plane_lon
    current_alt = plane_alt

    # Decide if goal is reached
    lat_dist = final_lat - current_lat
    lon_dist = final_lon - current_lon
    alt_dist = final_alt - current_alt

    lat_check = 0.001 <= lat_dist >= 0
    lon_check = 0.001 <= lon_dist >= 0
    alt_check = 0.001 <= alt_dist >= 0
        
    if lat_check and lon_check and alt_check:
        print("Goal reached")
        return True
        
    else:
        return False
        

def check_wp_reached(plane_lat, plane_lon, plane_alt, wp):
    # Setting goal
    wp_lat = wp[0]
    wp_lon = wp[1]
    wp_alt = wp[2]

    # Extracting lat, lon and alt
    current_lat = plane_lat
    current_lon = plane_lon 
    current_alt = plane_alt

    # Decide if goal is reached
    lat_dist = wp_lat - current_lat
    lon_dist = wp_lon - current_lon
    alt_dist = wp_alt - current_alt

    lat_check = 0.001 <= lat_dist >= 0
    lon_check = 0.001 <= lon_dist >= 0
    alt_check = 0.001 <= alt_dist >= 0
        
    if lat_check and lon_check and alt_check:
        print("Waypoint reached")
        return True
    else:
        return False
    


def perform_action(index):
    # Possible actions
    actions = [bot_left,bot_mid,bot_right, mid_left, mid_mid, mid_right, 
    throttle_up_full,throttle_up_low, throttle_up_half, throttle_neutral, throttle_down_half, throttle_down_full,
    top_left, top_mid, top_right]

    # Choose action
    chosen_action = actions[index]

    # Perform action
    chosen_action()

def draw_graph(episode, steps, reward):
    plt.figure(episode,steps)
    plt.savefig('DQN_model_vis.png')


def test_():
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
        val = client.getPOSI()
        print(val[0])
        arr = np.array([val[0]], dtype='c16')
        print(arr)
        


test_()

    
