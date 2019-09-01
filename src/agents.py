import torch
import numpy as np

class Agents:
    """An wrapper for multiple agents"""
    def __init__(self, *agents):
        """Initialize agents to be wrapped.
        Params
        ======
            *agents (tuple Agent - from maddpg_agent.py)    : list of agents.
        """
        self.agents = list(agents)
        
    def reset(self):
        """Resets the Ornstein-Uhlenbeck process for each agent (to be used for noisy actions)
        """
        for i in range(0,len(self.agents)):
            self.agents[i].reset()
        
    def act(self, states, add_noise = True):
        """Returns actions for both agents as per current policy, given their respective states."""
        return np.array(list(map(lambda x: x.act(states, add_noise),self.agents))).flatten()
    
    def step(self, states, actions, rewards, next_states, dones):
        """For each agent , save experience in respective replay memory, and use random sample from buffer to learn."""
        for i in range(0,len(self.agents)):
            self.agents[i].step(states, actions, rewards[i], next_states, dones,i)
            
    def save(self, folder_destination, solved):
        """Save agent model parameters"""
        if solved:
            for i in range(0,len(self.agents)):
                torch.save(self.agents[i].actor_local.state_dict(), folder_destination + '\checkpoint_actor_solved_'+str(i)+'.pth')
                torch.save(self.agents[i].critic_local.state_dict(), folder_destination + '\checkpoint_critic_solved_'+str(i)+'.pth')
        else:
            for i in range(0,len(self.agents)):
                torch.save(self.agents[i].actor_local.state_dict(), folder_destination + '\checkpoint_actor_not_solved_'+str(i)+'.pth')
                torch.save(self.agents[i].critic_local.state_dict(), folder_destination + '\checkpoint_critic_not_solved_'+str(i)+'.pth')
