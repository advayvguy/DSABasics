from GraphADT import Queue
LEFT = "L"
RIGHT = 'R'

def rule_check(state, state_map):
    return ((state[0] >= state[1] or state[0] == 0) and 
            (state[2] >= state[3] or state[2] == 0) and 
            state[0] >= 0 and 
            state[1] >= 0 and 
            state[2] >= 0 and 
            state[3] >= 0 and 
            state not in state_map)

def traversal(state, prev_map):
    if state not in prev_map:
        print(state)
        return 
    traversal(prev_map[state], prev_map)
    print(state)

def three_man_cannibal():
    prev_map = {}
    state_map = {}
    initial_state = (3,3,0,0,LEFT)
    state_map[initial_state] = None
    queue = Queue()
    queue.enqueue(initial_state)

    while True:
        state = queue.dequeue()
        if state == (0,0,3,3,RIGHT):
            break

        #state machine
        s1 = s2 = s3 = s4 = s5 = None
        if state[4] == LEFT:
            s1 = (state[0]-2, state[1], state[2]+2, state[3], RIGHT)
            s2 = (state[0]-1, state[1]-1, state[2]+1, state[3]+1, RIGHT)
            s3 = (state[0], state[1]-2, state[2], state[3]+2, RIGHT)
            s4 = (state[0]-1, state[1], state[2]+1, state[3], RIGHT)
            s5 = (state[0], state[1]-1, state[2], state[3]+1, RIGHT)
        
        elif state[4] == RIGHT:
            s1 = (state[0]+2, state[1], state[2]-2, state[3], LEFT)
            s2 = (state[0]+1, state[1]+1, state[2]-1, state[3]-1, LEFT)
            s3 = (state[0], state[1]+2, state[2], state[3]-2, LEFT)
            s4 = (state[0]+1, state[1], state[2]-1, state[3], LEFT)
            s5 = (state[0], state[1]+1, state[2], state[3]-1, LEFT)
        
        for s in [s1,s2,s3,s4,s5]:
            if rule_check(s, state_map):
                state_map[s] = None
                prev_map[s] = state
                queue.enqueue(s)
    
    traversal(state, prev_map)

three_man_cannibal()