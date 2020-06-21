import gym
from gym import error, utils
from gym.utils import seeding
from custom_gym.envs.myxpc import xpc2 as xpc
from custom_gym.envs.myxpc.utils import observation, check_failures, check_goal_reached, perform_action, check_wp_reached, get_waypoints, set_waypoint, check_route
import pygetwindow
import numpy as np
from pydirectinput import keyDown, keyUp
import time
import asyncio


class XPL(gym.Env):
    metadata = {"render.modes": ["human"]}
    

    def __init__(self):
        print("init xpl")
        self.waypoints = get_waypoints()
        self.waypoint_counter = 0
        self.current_waypoint = self.waypoints[self.waypoint_counter]
        # check_route()
        
    

   
    def reset(self):
        print("reset")
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
            # Setting the starting waypoint
            set_waypoint(self.waypoints[0])
            # Setting simulation speed
            simulation_dref = "sim/time/sim_speed"
            client.sendDREF(simulation_dref, 1000.0)
            res = client.getDREF(simulation_dref)
            print(res)

            # Selecting the current and XPlane window 
            current_window = pygetwindow.getActiveWindow()
            xplane_window = pygetwindow.getWindowsWithTitle("X-System")[0]
            # Focuss on the Xplane window
            xplane_window.activate()

            # Performing the reset command ctr+; on the focussed window
            keyDown('ctrl')
            keyDown(';')
            keyUp('ctrl')
            keyUp(';')

            time.sleep(3)
            # Releasing brakes
            keyDown('b')
            keyUp('b')

            # Return to the old window I was on
            current_window.activate()
            # Gives the simulator enough time to reload
            time.sleep(3)
            # Get observation
            obs = observation()
            time.sleep(3)
            return obs
        
        
            

    def render(self, mode="human"):
        print("render")

    def quit(self):
        print("quit")

    def record_waypoint(self):
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
            for _ in range(100):
                time.sleep(2)
                pt = client.getPOSI()[0:3]
                print(pt)

    def step(self, action):
        # Perform action
        perform_action(action)
        time.sleep(4)
        # Get obeservation
        new_observation = observation()
        time.sleep(3)
        # Initialize variables for reward
        reward = 0
        plane_lat = new_observation[0]
        plane_lon = new_observation[1]
        plane_alt = new_observation[2]

        
        # Check for failures/crashes and assigining reward
        check_failure = check_failures()
        
        # Check if goal is reached and assigining reward
        if self.waypoint_counter == 99:
            check_goal = check_goal_reached(plane_lat, plane_lon, plane_alt)
        
        # Check if a waypoint is reached
        check_wp = check_wp_reached(plane_lat, plane_lon, plane_alt, self.current_waypoint)
        if check_wp == True:
            reward = reward + 10
            print("waypoint reached")
            if self.waypoint_counter < 99:
                self.waypoint_counter = self.waypoint_counter + 1
                set_waypoint(self.current_waypoint)

        # Assigining done 
        if check_failure  == True:
            done = True
            reward = reward - 100
        elif self.waypoint_counter == 99 :
            if check_goal == True:
                done = True
                reward = reward + 50
        else:
            done = False
            reward = reward
        # return new_observation, reward, done
        return new_observation, reward, done
    
               
            
