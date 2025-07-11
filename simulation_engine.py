import random
import math

class Agent:
    def __init__(self, x, y, dx, dy, state = 'S'):
        self.x = x                      # horizontal position
        self.y = y                      # vertical position
        self.dx = dx                    # horizontal movement speed
        self.dy = dy                    # vertical movement speed
        self.state = state              # 'S' (Susceptible), 'I' (Infected), 'R' (Recovered)
        self.infection_timer = 0        # Counts how long the agent has been infected

    def move(self, width, height):
        # Moves the agent, bouncing off walls if hitting canvas boundaries
        self.x += self.dx
        self.y += self.dy

        # Bounce on left/right wall
        if self.x <= 0 or self.x >= width:
            self.dx *= -1
        
        # Boounce on top/bottom wall
        if self.y <= 0 or self.y >= height:
            self.dy *= -1

    def infect(self):
        # Sets the agent's state to infected if they are susceptible
        if self.state == 'S':
            self.state = 'I'
            self.infection_timer = 0

    def recover(self):
         # Sets the agent's state to recovered if they are infected
         if self.state == 'I':
             self.state = 'R'