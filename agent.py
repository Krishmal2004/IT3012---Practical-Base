# agent.py
import random

class GreedyGridAgent:

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']
        self.agent_pos = (0, 0)
        self.alive = True
        self.toxic_traps = []
        self.pit_locations = []
        self.gold_locations = []

    def sense_and_act(self, percept: dict) -> str:
        pos = percept['agent_pos']

        if percept.get('smells_toxin', False):
            return random.choice(['Left', 'Right', 'Up', 'Down'])

        if percept.get('smells_food', False):
            return random.choice(self.actions_pool)

        return random.choice(self.actions_pool)

    def get_percept(self) -> dict:
        smells_toxin = self.agent_pos in self.toxic_traps
        
        percept = {
            'agent_pos': self.agent_pos,
            'smells_food': self.agent_pos in self.gold_locations,
            'smells_toxin': smells_toxin,  
            'alive': self.alive,
            'score': 0
        }
        return percept