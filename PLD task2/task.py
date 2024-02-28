maze = [
    ['P', 'X', 'X', 'X', 'X'],
    ['.', '.', '.', '.', 'X'],
    ['X', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', 'X'],
    ['X', 'X', 'X', '.', '.']
]
def OffBounds(new_pos):
    if(new_pos[0]<0 or new_pos[0]>=len(maze)) or (new_pos[1]<0 or new_pos[1]>=len(maze)):
        return True
    else:
        return False 
def move(player_position,direction):
    x = 0
    y = 0
    match direction:
        case "up":
            x = -1
        case "down":
            x = 1
        case "right":
            y = 1
        case "left":
            y = -1
        case _:
            print("You can't move")
    new_pos = [player_position[0]+x ,player_position[1]+y]
    if(OffBounds(new_pos)):
        print("Wrong dir")
        return player_position
    
    if(maze[new_pos[0]][new_pos[1]]=='X'):
        print("there is a wall")
        return player_position
    
    maze[player_position[0]][player_position[1]]='.'
    maze[new_pos[0]][new_pos[1]]='P'
    return new_pos




def Print(maze):
    for line in maze:
        l=""
        for i in line:
           l+=i 
        print(l,'\n')
        

def CheckWin():
    player_position=[0,0]
    while player_position!=[4,4]:
        Print(maze)
        print("dir:")
        player_position = move(player_position,input())

    print("You win")

CheckWin()


        
    