function [Q, epsilon] = agent_update(Q, old_state, state, action, reward, epsilon, learningRate, discount, epsilonDelta)

old_Qvalue = Q(action, old_state);
best_action = agent_greedy_action(state, Q);
best_Qvalue = Q(best_action, state);
%update
new_Qvalue = old_Qvalue + learningRate*(reward + discount*best_Qvalue - old_Qvalue);
Q(action, old_state) = new_Qvalue;
if epsilon > 0
    epsilon = epsilon - epsilonDelta;
end

end

