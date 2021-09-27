function action = agent_greedy_action(state, Q)
if Q(1, state) > Q(2, state)
    action = 1;
elseif Q(1, state) < Q(2, state)
    action = 2;
else 
    action = agent_random_action();
end
end