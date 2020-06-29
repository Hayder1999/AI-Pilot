import gym
import numpy as np
from custom_gym.envs.myxpc.utils import observation as obs ,draw_graph
from dqn import Agent
import time


def main():
    gym_env = gym.make('custom_gym:Xplane-v0')
    lr = 0.001
    gam = 0.01
    n_games = 500
    # nn_input = obs()
    agent = Agent(learning_rate=lr, gamma=gam, epsilon=1.0, 
        input_dims= (6,), n_actions=15, batch_size=32, file_name='saved_models/dq_model_2.h5')
    scores = []
    total_steps = []
    eps_hist = []
    # agent.load_model()
    
    for i in range(n_games):
        try:
            done = False
            score = 0 
            observation = gym_env.reset()
            time.sleep(2)
            observation_checkpoints = np.array([observation[0:2]])
            step_counter = 0
            print("GAME ITERATION ", i)
            while not done:
                action = agent.choose_action(observation)
                new_observation, reward, done = gym_env.step(action)
                step_counter = step_counter + 1
                score = score + reward
                agent.store_transition(observation, action, reward, new_observation, done)
                observation = new_observation
                agent.learn()
                # This if statement checks if the airplane is stuck 
                observation_checkpoints = np.append(observation_checkpoints, [new_observation[0:2]], axis=0)
                print(observation_checkpoints)
                print("stepcounter is", step_counter)
                if step_counter % 30 == 0:
                    if np.array_equal(observation_checkpoints[step_counter - 30], observation_checkpoints[step_counter - 1]):
                        done = True
            eps_hist.append(agent.epsilon)
            scores.append(score)
            total_steps.append(step_counter)
        except Exception as e:
            print(str(e))
    agent.save_model()
    print(scores)
    
main()

    

