import os
import yaml
import time
import importlib

from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from agent import WSNAgent
from wsn_message import WSNMessage
from mesa.datacollection import DataCollector

def split_on_last(string, char):
    rev_string = string[::-1]   # `[::-1]` gets the reverse of string
    end, start = rev_string.split(char, 1)
    return start[::-1], end[::-1]


class WSNModel(Model):
    def __init__(self, agents, width, height, blackholeRatio, seed=None):
        # Initialize the RNG
        self.seed = seed
        if self.seed is None:
            self.seed = time.time()
        self.reset_randomizer(self.seed)
        # Initialize the model
        self.running = True
        self.grid = SingleGrid(width, height, False)
        self.schedule = RandomActivation(self)
        self.bhRatio = blackholeRatio
        self.datacollector = DataCollector(
                agent_reporters={"tagDict": lambda a: a.tagDict}
        )
        # Add agents
        for agent_class, agents in agents.items():
            module_name, class_name = split_on_last(agent_class, '.')
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            for agent in agents:
                a = cls(agent["id"], self, agent["color"], self.bhRatio)
                self.schedule.add(a)
                self.grid.place_agent(a, (agent["x"], agent["y"]))

    def step(self, messages):
        for i in range(0, len(messages)):
            wsnmessages = []
            for j in range(0, len(messages[i])):
                tempMess = messages[i][j]
                wsnmessages.append(WSNMessage(**tempMess))
            self.schedule.agents[i].update_messages(wsnmessages)
        self.schedule.step()
    
    def run_model(self, n):
        for i in range(n):
            self.step()
