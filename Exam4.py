# Action_List = ['L' , 'R'] #L,R
State_Name = ['A', 'B', 'C', 'D','E',"F", "G", "H"]
State_Reward = {
    "D":10.0,
    "E":1.0,
}
State_U = {
    "A":0.0,
    "B":0.0,
    "C":0.0,
    "D":0.0,
    "E":0.0,
    "F":0.0,
    "G":0.0,
    "H":0.0,
}
discount = 1.0
Transition1  = {}

Transition1['A'] = {} #Current State  
Transition1['A']['B'] = 0.6
Transition1['A']['F'] = 0.2
Transition1['A']['A'] = 0.2 

Transition1['B'] = {} #Current State  
Transition1['B']['C'] = 0.6
Transition1['B']['A'] = 0.2
Transition1['B']['B'] = 0.2

Transition1['C'] = {} #Current State  
Transition1['C']['D'] = 0.6
Transition1['C']['B'] = 0.2
Transition1['C']['H'] = 0.2

Transition1['D'] = {} #Current State  
Transition1['D']['D'] = 1.0

Transition1['E'] = {} #Current State  
Transition1['E']['E'] = 1.0

Transition1['F'] = {} #Current State  
Transition1['F']['E'] = 0.6
Transition1['F']['A'] = 0.2
Transition1['F']['G'] = 0.2

Transition1['G'] = {} #Current State  
Transition1['G']['F'] = 0.6
Transition1['G']['H'] = 0.2
Transition1['G']['G'] = 0.2

Transition1['H'] = {} #Current State  
Transition1['H']['G'] = 0.6
Transition1['H']['C'] = 0.2
Transition1['H']['H'] = 0.2

Transition2  = {}

Transition2['A'] = {} #Current State  
Transition2['A']['B'] = 0.2
Transition2['A']['F'] = 0.6
Transition2['A']['A'] = 0.2 

Transition2['B'] = {} #Current State  
Transition2['B']['C'] = 0.6
Transition2['B']['A'] = 0.2
Transition2['B']['B'] = 0.2

Transition2['C'] = {} #Current State  
Transition2['C']['D'] = 0.6
Transition2['C']['B'] = 0.2
Transition2['C']['H'] = 0.2

Transition2['D'] = {} #Current State  
Transition2['D']['D'] = 1.0

Transition2['E'] = {} #Current State  
Transition2['E']['E'] = 1.0

Transition2['F'] = {} #Current State  
Transition2['F']['E'] = 0.6
Transition2['F']['A'] = 0.2
Transition2['F']['G'] = 0.2

Transition2['G'] = {} #Current State  
Transition2['G']['F'] = 0.2
Transition2['G']['H'] = 0.6
Transition2['G']['G'] = 0.2

Transition2['H'] = {} #Current State  
Transition2['H']['G'] = 0.2
Transition2['H']['C'] = 0.6
Transition2['H']['H'] = 0.2

Transition = Transition1.copy()
for t in range(0,11):
    if(t == 6):
        print("change transition function")
        Transition = Transition2.copy()
    Temp_U = {
        "A":0.0,
        "B":0.0,
        "C":0.0,
        "D":0.0,
        "E":0.0,
        "F":0.0,
        "G":0.0,
        "H":0.0,
    }
    for ind_state, curr_state in enumerate(State_Name):
        Q_value = 0
        for ind_trans, trans_state in enumerate(Transition[curr_state].keys()):
            if(t == 0):
                Q_value = 0
            elif(curr_state != 'D' and curr_state != 'E'):
                Q_value += Transition[curr_state][trans_state]*(discount*State_U[trans_state])
            else:
                Q_value += Transition[curr_state][trans_state]*(State_Reward[trans_state] + 1*State_U[trans_state])
        Temp_U[curr_state] = round(Q_value,2)
        if((curr_state == 'D' or curr_state == 'E') and t == 1):
            State_Reward[curr_state] = 0
    State_U = Temp_U.copy() 
    print("T : %d" %(t), end = " ")
    for ind, key in enumerate(State_U):
        print("State %s : %.2f " %(key, State_U[key]), end =" ")
    print()
   



