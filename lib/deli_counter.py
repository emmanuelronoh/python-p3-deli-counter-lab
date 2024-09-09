# deli_counter.py

def line(queue):
    '''Prints the current line.'''
    if not queue:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_status += ' '.join(f"{i+1}. {person}" for i, person in enumerate(queue))
        print(line_status)

def take_a_number(queue, name):
    '''Adds a person to the line and prints their position.'''
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    '''Serves the next person in line.'''
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        person = queue.pop(0)
        print(f"Currently serving {person}.")
