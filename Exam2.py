Action_Reward = [1 , 2]
State_name = ['A', 'B', 'C', "D"]
State_Reward = [0.0,0.0,0.0,-10.0]
State_U = [0,0,0,0]
Transition  = {}

Transition[0] = {} #current_state 
Transition[0][0] = {} #action
Transition[0][0][0] =1.0 #next_state
Transition[0][1] = {} #action
Transition[0][1][0] =0.5 #next_state
Transition[0][1][1] =0.5 #next_state 

Transition[1] = {} #current_state  
Transition[1][0] = {} #action
Transition[1][0][0] =0.5 #next_state
Transition[1][0][1] =0.5 #next_state 
Transition[1][1] = {} #action
Transition[1][1][1] =0.5 #next_state
Transition[1][1][2] =0.5 #next_state 

Transition[2] = {} #current_state  
Transition[2][0] = {} #action
Transition[2][0][1] =0.5 #next_state
Transition[2][0][2] =0.5 #next_state
Transition[2][1] = {} #action
Transition[2][1][2] =0.5 #next_state
Transition[2][1][3] =0.5 #next_state 

Transition[3] = {} #current_state  
Transition[3][0] = {} #action
Transition[3][0][3] =1 #next_state
Transition[3][1] = {} #action
Transition[3][1][3] = 1 #next_state 
print("T = %d; State A = %.2f State B = %.2f State C = %.2f State D = %.2f" %(0, State_U[0], State_U[1], State_U[2], State_U[3]))
for t in range(10):
    temp_u = [0,0,0,0]
    for ind_u, state_u, in enumerate(State_U):
        temp_list =[]
        for ind_act, current_reward in enumerate(Action_Reward):
            Q_value = 0
            for ind_key , key in enumerate(Transition[ind_u][ind_act].keys()):
                # print(ind_u, ind_act, key)
                Q_value += Transition[ind_u][ind_act][key]*(current_reward+State_Reward[key]+State_U[key])
            temp_list.append(Q_value)
        temp_u[ind_u] = max(temp_list)
        # if(temp_list[0] > temp_list[1]):
        #     print("When you stay state", State_name[ind_u],"choose action A")
        # else :
        #     print("When you stay state", State_name[ind_u],"choose action B")
    State_U = temp_u.copy()
    print("T = %d; State A = %.2f State B = %.2f State C = %.2f State D = %.2f" %(t+1, State_U[0], State_U[1], State_U[2], State_U[3]))




