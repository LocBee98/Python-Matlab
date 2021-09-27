function [state, reward] = env_step(action, state)
%Tham so
bigR = 10;
smallR = 2;
slip = 0.1;
length = int8(5);
%executing

%define action for Matlab: left ~ 1; right ~ 2
%define action for python: left ~ 0; right ~ 1
S = state; %current state

if (rand < slip) %disturbance
    action = not(action);
end
if (action == 0)
    reward = smallR;
    state = int8(0);   %0 for python
else
    if (S < length - 1)  %lenght - 1 : for python | <length -0 for matlab
        state = state + 1;
        reward = 0;
    else
        reward = bigR;
    end
end
    
end