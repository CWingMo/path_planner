from collections import deque

directions = [
    (-1, 0),  # 上
    (1, 0),   # 下
    (0, -1),  # 左
    (0, 1)    # 右
]

def bfs(start, goal, graph):
    queue = deque()
    queue.append(start)
    parent = {start: None}
    visited = set()
    visited.add(start)
    while queue:
        current = queue.popleft()
        
        if current == goal:
            break
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < len(graph) and
                0 <= neighbor[1] < len(graph[0]) and
                graph[neighbor[0]][neighbor[1]] == 1 and
                neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                
    if goal not in parent:
        return []
    
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()  # 反转顺序，从 start -> goal
    return path

# # 测试示例
# if __name__ == "__main__":
#     maze = [
#         [1, 1, 0, 1],
#         [0, 1, 1, 1],
#         [1, 1, 0, 1]
#     ]
#     start = (0, 0)
#     goal = (2, 3)
#     path = bfs(start, goal, maze)
#     print("路径:", path)
        
        
        
    
        
    
    