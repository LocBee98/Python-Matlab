function action = agent_get_next_action(state, Q, epsilon)
if rand > epsilon
    action = agent_greedy_action(state, Q);
else 
    action = agent_random_action();
end