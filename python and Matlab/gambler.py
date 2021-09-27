from enums import *
import random

class QAgent:
    def __init__(self, learning_rate=0.1, discount=0.95, epsilon=1.0, iterations=10000):
        self.q_table = [[0,0,0,0,0], [0,0,0,0,0]] # Spreadsheet (Q-table) for rewards accounting
        self.learning_rate = learning_rate # How much we appreciate new q-value over current
        self.discount = discount # How much we appreciate future reward over current
        self.epsilon = 1.0 # Initial epsilon rate
        self.epsilon_delta = 1.0 / iterations # Shift from epsilon to explotation

    def get_next_action(self, state):
        if random.random() > self.epsilon: # Explore (gamble) or exploit (greedy)
            return self.greedy_action(state)
        else:
            return self.random_action()

    def greedy_action(self, state):
        # Is RIGHT reward is bigger?
        if self.q_table[RIGHT][state] > self.q_table[LEFT][state]:
            return RIGHT
        # Is LEFT reward is bigger?
        elif self.q_table[LEFT][state] > self.q_table[RIGHT][state]:
            return LEFT
        # Rewards are equal, take random action
        return RIGHT if random.random() < 0.5 else LEFT

    def random_action(self):
        return RIGHT if random.random() < 0.5 else LEFT

    def update(self, old_state, state, action, reward):
        # Old Q-table value
        old_value = self.q_table[action][old_state]
        # What would be our best next action?
        best_action = self.greedy_action(state)
        # What is reward for the best next action?
        best_value = self.q_table[best_action][state]

        # Main Q-table updating algorithm
        new_value = old_value + self.learning_rate * (reward + self.discount * best_value - old_value)
        self.q_table[action][old_state] = new_value

        # Finally shift our epsilon toward zero (less gambling)
        if self.epsilon > 0:
            self.epsilon -= self.epsilon_delta
