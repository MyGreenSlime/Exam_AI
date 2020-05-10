Action_List = ['L' , 'R'] #L,R
State_Name = ['X','A', 'B', 'C', "D",'Y']
State_Reward = {
    "X":10.0,
    "Y":-10.0
}
State_U = {
    "X":0.0,
    "A":0.0,
    "B":0.0,
    "C":0.0,
    "D":0.0,
    "Y":0.0
}
discount = 0.5
Transition  = {}

Transition['X'] = {} #Current State 
Transition['X']['L'] = {} #Action = L 
Transition['X']['L']['X'] = 1.0
Transition['X']['R'] = {} #Action = R 
Transition['X']['R']['X'] = 1.0

Transition['Y'] = {} #Current State 
Transition['Y']['L'] = {} #Action = L 
Transition['Y']['L']['Y'] = 1.0 
Transition['Y']['R'] = {} #Action = R 
Transition['Y']['R']['Y'] = 1.0 

Transition['A'] = {} #Current State 
Transition['A']['L'] = {} #Action = L
Transition['A']['L']['X'] = 0.8
Transition['A']['L']['B'] = 0.2
Transition['A']['R'] = {} #Action = R
Transition['A']['R']['C'] = 0.2
Transition['A']['R']['B'] = 0.6
Transition['A']['R']['X'] = 0.2


Transition['B'] = {} #Current State 
Transition['B']['L'] = {} #Action = L
Transition['B']['L']['X'] = 0.2
Transition['B']['L']['A'] = 0.6
Transition['B']['L']['C'] = 0.2
Transition['B']['R'] = {} #Action = R
Transition['B']['R']['D'] = 0.2
Transition['B']['R']['C'] = 0.6
Transition['B']['R']['A'] = 0.2


Transition['C'] = {} #Current State 
Transition['C']['L'] = {} #Action = L
Transition['C']['L']['A'] = 0.2
Transition['C']['L']['B'] = 0.6
Transition['C']['L']['D'] = 0.2
Transition['C']['R'] = {} #Action = R
Transition['C']['R']['Y'] = 0.2
Transition['C']['R']['D'] = 0.6
Transition['C']['R']['B'] = 0.2

Transition['D'] = {} #Current State 
Transition['D']['L'] = {} #Action = L
Transition['D']['L']['B'] = 0.2
Transition['D']['L']['C'] = 0.6
Transition['D']['L']['Y'] = 0.2
Transition['D']['R'] = {} #Action = R
Transition['D']['R']['Y'] = 0.8
Transition['D']['R']['C'] = 0.2

List_Dict  = []
for t in range(0,1000):
    print(t)
    Temp_U = {
        "X":0.0,
        "A":0.0,
        "B":0.0,
        "C":0.0,
        "D":0.0,
        "Y":0.0
    }
    TempDict = {}
    TempDict['T'] = t
    for ind_state, curr_state in enumerate(State_Name):
        Temp_Q_value = []
        for ind_act, action in enumerate(Action_List):
            Q_value = 0
            for ind_trans, trans_state in enumerate(Transition[curr_state][action].keys()):
                if(t == 0):
                    Q_value = 0
                elif(curr_state != 'X' and curr_state != 'Y'):
                    Q_value += Transition[curr_state][action][trans_state]*(discount*State_U[trans_state])
                else:
                    Q_value += Transition[curr_state][action][trans_state]*(State_Reward[trans_state] + 1*State_U[trans_state])
            TempDict["Q("+curr_state+","+action+")"] = round(Q_value,2)
            Temp_Q_value.append(TempDict["Q("+curr_state+","+action+")"])
        TempDict["V("+curr_state+")"] = max(Temp_Q_value)
        Temp_U[curr_state] = TempDict["V("+curr_state+")"]
        if(Temp_Q_value[0] > Temp_Q_value[1]):
            print("When You stay on state", curr_state, "you choose action L")
        else:
            print("When You stay on state", curr_state, "you choose action R")
        if((curr_state == 'X' or curr_state == 'Y') and t == 1):
            State_Reward[curr_state] = 0
    State_U = Temp_U.copy() 
    print(State_U)
    List_Dict.append(TempDict)

import pandas as pd

df = pd.DataFrame(List_Dict)

# df.to_csv("Exam3_a.csv", index = False) #export to exel


