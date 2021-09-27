function [state, reward] = env_step(action, state)
%Tham so
bigR = 10;
smallR = 2;
slip = 0.1;
length = 5;
%executing

%define action: left ~ 1; right ~ 2

S = state; %current state

if (rand < slip) %disturbance
    action = not(action);
end
if (action == 1)
    reward = smallR;
    state = 1;   
else
    if (S < length - 1)
        state = state + 1;
        reward = 0;
    else
        state = length;
        reward = bigR;
    end
end
    
end