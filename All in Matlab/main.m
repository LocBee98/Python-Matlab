max_step = 10000;
learningRate = 0.1;
discount = 0.95;
epsilon = 1.0;
epsilonDelta = 1.0/max_step;
Q = agent_QTable();

state = env_reset();
total_reward = 0;

for step = 1: max_step
    old_state = state;
    action = agent_get_next_action(state, Q, epsilon);
    [state, reward] = env_step(action, state);
    [Q, epsilon] = agent_update(Q, old_state, state, action, reward, epsilon, learningRate, discount, epsilonDelta);
    total_reward = total_reward + reward;
end
    
    
