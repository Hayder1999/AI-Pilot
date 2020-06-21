import numpy as np 
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model


# Experience replay
class ReplayBuffer():
    def __init__(self, mem_size, input_dims):
        self.mem_size = mem_size
        self.mem_counter = 0

        self.state_memory = np.zeros((self.mem_size, *input_dims),dtype=np.float32) 
        self.new_state_memory = np.zeros((self.mem_size, *input_dims),dtype=np.float32)
        self.action_memory = np.zeros(self.mem_size, dtype=np.int32)
        self.reward_memory = np.zeros(self.mem_size, dtype=np.float32)
        self.terminal_memory = np.zeros(self.mem_size, dtype=np.int32)

    def store_transition(self, state, action, reward, new_state, done):
        index = self.mem_counter % self.mem_size
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.reward_memory[index] = reward
        self.action_memory[index] = action
        self.terminal_memory[index] = 1 - int(done)
        self.mem_counter += 1

    def sample_buffer(self, batch_size):
        max_mem = min(self.mem_counter, self.mem_size)
        batch = np.random.choice(max_mem, batch_size, replace=False)

        states = self.state_memory[batch]
        new_state = self.new_state_memory[batch]
        rewards = self.reward_memory[batch]
        actions = self.action_memory[batch]
        terminal = self.terminal_memory[batch]
        
        return states, new_state, rewards, actions, terminal

# Neural network model 
def DeepQ_model(lr, n_actions, input_dims, fcl1_dims, fcl2_dims):
    model = keras.Sequential([
        Dense(fcl1_dims, activation='relu', input_shape=input_dims),
        Dense(fcl2_dims, activation='relu'),
        Dense(n_actions, activation=None)
    ])
    model.compile(optimizer=Adam(lr), loss='mean_squared_error')
    return model

# Agent for running in the environment
class Agent():
    def __init__(self, learning_rate, gamma, n_actions, epsilon, batch_size,
                input_dims, file_name, epsilon_dec=1e-3, epsilon_end=0.01, 
                mem_size=1000000):
        self.action = [i for i in range(n_actions)]
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_end
        self.epsilon_dec = epsilon_dec
        self.batch_size = batch_size
        self.model_file = file_name
        self.memory = ReplayBuffer(mem_size, input_dims)
        self.q_eval = DeepQ_model(learning_rate,n_actions,input_dims, 50, 30)

    def store_transition(self, state, action, reward, new_state, done):
        self.memory.store_transition(state, action, reward, new_state, done)
    
    def choose_action(self, observation):
        if np.random.random() < self.epsilon:
            action = np.random.choice(self.action)
        else:
            state = np.array([observation])
            actions = self.q_eval.predict(state)
            action = np.argmax(actions)
        
        return action

    def learn(self):
        if self.memory.mem_counter < self.batch_size:
            return
        
        states, new_states, rewards, actions, dones = self.memory.sample_buffer(self.batch_size)

        q_eval = self.q_eval.predict(states)
        q_next = self.q_eval.predict(new_states)

        q_target = np.copy(q_eval)
        batch_index = np.arange(self.batch_size, dtype=np.int32)

        q_target[batch_index, actions] = rewards + self.gamma* np.max(q_next, axis=1) * dones

        self.q_eval.train_on_batch(states, q_target)

        if self.epsilon > self.epsilon_min:
            self.epsilon = self.epsilon - self.epsilon_dec
        else:
            self.epsilon = self.epsilon_min
    
    def save_model(self):
        self.q_eval.save(self.model_file)

    def load_model(self):
        self.q_eval = load_model(self.model_file)
