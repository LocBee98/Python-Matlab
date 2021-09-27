import random
import json

import time
import matlab.engine
from gambler import QAgent
from enums import *

def main():

    agent = QAgent()
    iterations = 100
    # setup environment
    engine1 = matlab.engine.start_matlab()
    engine2 = matlab.engine.start_matlab()
    #reset Environment
    state = engine1.env_reset()

    # total_reward = 0 # Score keeping
    # last_total = 0
    # main loop
    for step in range(iterations):
        old_state = state # Store current state
        action = agent.get_next_action(old_state) # Query agent for the next action
        state, reward = engine2.env_step(action, old_state, nargout = 2) # Take action, get new state and reward
        agent.update(old_state, state, action, reward) # Let the agent update internals

        # total_reward += reward # Keep score
        # if step % 250 == 0: # Print out metadata every 250th iteration
        #     performance = (total_reward - last_total) / 250.0
        #     print(json.dumps({'step': step, 'performance': performance, 'total_reward': total_reward}))
        #     last_total = total_reward
        #     print("state = ", dungeon.state)
        #     print(agent.q_table)

        time.sleep(0.0001) # Avoid spamming stdout too fast!

    print("Final Q-table", agent.q_table)

if __name__ == "__main__":
    main()
