import matlab.engine
action = 1;
state = 1;
eng1 = matlab.engine.start_matlab()
state, reward = eng1.env_step(action, state, nargout = 2)
print(state)
print(reward)
