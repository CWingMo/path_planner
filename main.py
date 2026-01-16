import random
from algorithms import bfs
dires_for_path = [
    (-2,0),
    (2,0),
    (0,-2),
    (0,2)
]
visited = set()
def create_maze(height, width ,start):
    visited.clear()
    maze = [[0 for _ in range(2*width+1)] for _ in range(2*height+1)]
    current = start
    dfs(maze,current)
    return maze
        
def dfs(maze,current):
    visited.add(current)
    maze[current[0]][current[1]] = 1
    random.shuffle(dires_for_path)
    for direction in dires_for_path:
        neighbor = (current[0] + direction[0], current[1] + direction[1])
        if (1 <= neighbor[0] < len(maze)-1 and
            1 <= neighbor[1] < len(maze[0])-1 and
            neighbor not in visited):
            wall = ((current[0] + neighbor[0])//2, (current[1] + neighbor[1])//2)
            maze[wall[0]][wall[1]] = 1
            dfs(maze,neighbor)
    return maze

def print_maze(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 1:
                ch = '.'
            else:
                ch = '#'
            print(ch, end=' ')
        print()
    
def main():
    width = int(input())
    height = int(input())
    start = (1,1)
    maze = create_maze(height ,width ,start)
    print_maze(maze)

if __name__ == "__main__":
    main()