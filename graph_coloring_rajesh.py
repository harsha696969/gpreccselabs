colors = ['Red', 'Blue', 'Green']
states = ['a','b','c','d']
neighbors = {}
neighbors['a'] = ['d','c','b']
neighbors['b'] = ['a','c']
neighbors['c'] = ['a','b','d']
neighbors['d']=['a','c']
colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)
    
main()