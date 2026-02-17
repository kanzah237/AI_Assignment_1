
import matplotlib.pyplot as plt
import numpy as np
import time
from collections import deque
import heapq

# Grid constants
ROWS, COLS = 10, 10
START = (7, 1)
TARGET = (5, 7)

# Static walls
walls = {(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)}

# clockwise movement order
MOVES = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # bottom
    (1, 1),   # bottom-right
    (0, -1),  # left
    (-1, -1)  # top-left
]


# check conditions

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS


def neighbors(node):
    r, c = node
    result = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and (nr, nc) not in walls:
            result.append((nr, nc))
    return result


def reconstruct_path(parent, end):
    path = []
    while end in parent:
        path.append(end)
        end = parent[end]
    path.append(START)
    return path[::-1]


# intialise grid

def draw_grid(frontier=set(), explored=set(), path=[]):
    grid = np.zeros((ROWS, COLS))

    for r, c in walls:
        grid[r][c] = -1

    for r, c in explored:
        grid[r][c] = 0.3

    for r, c in frontier:
        grid[r][c] = 0.6

    for r, c in path:
        grid[r][c] = 0.9

    sr, sc = START
    tr, tc = TARGET

    grid[sr][sc] = 1.5
    grid[tr][tc] = 2

    plt.clf()
    plt.imshow(grid)
    plt.title("Uninformed Search Visualization")
    plt.pause(0.15)


# bfs
def bfs():
    visited = set([START])
    queue = deque([START])
    parent = {}

    while queue:
        node = queue.popleft()

        draw_grid(set(queue), visited)

        if node == TARGET:
            return reconstruct_path(parent, node)

        for nb in neighbors(node):
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                queue.append(nb)

    return []


# dfs

def dfs():
    visited = set([START])
    stack = deque([START])
    parent = {}

    while stack:
        node = stack.pop()

        draw_grid(set(stack), visited)

        if node == TARGET:
            return reconstruct_path(parent, node)

        for nb in neighbors(node):
            if nb not in visited:
                visited.add(nb)
                parent[nb] = node
                stack.append(nb)

    return []


# ucs

def ucs():
    pq = [(0, START)]
    visited = set()
    parent = {}
    cost = {START: 0}

    while pq:
        g, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        draw_grid({n for _, n in pq}, visited)

        if node == TARGET:
            return reconstruct_path(parent, node)

        for nb in neighbors(node):
            new_cost = g + 1
            if nb not in cost or new_cost < cost[nb]:
                cost[nb] = new_cost
                parent[nb] = node
                heapq.heappush(pq, (new_cost, nb))

    return []


# dls

def dls(limit):
    stack = [(START, 0)]
    visited = set([START])
    parent = {}

    while stack:
        node, depth = stack.pop()

        draw_grid({n for n, _ in stack}, visited)

        if node == TARGET:
            return reconstruct_path(parent, node)

        if depth < limit:
            for nb in neighbors(node):
                if nb not in visited:
                    visited.add(nb)
                    parent[nb] = node
                    stack.append((nb, depth + 1))

    return []


# iddfs

def iddfs(max_depth=20):
    for depth in range(max_depth):
        path = dls(depth)
        if path:
            return path
    return []


# bidirectional

def bidirectional():
    q_start = deque([START])
    q_goal = deque([TARGET])

    parent_start = {}
    parent_goal = {}

    visited_start = {START}
    visited_goal = {TARGET}

    while q_start and q_goal:
        node_s = q_start.popleft()
        node_g = q_goal.popleft()

        draw_grid(set(q_start) | set(q_goal), visited_start | visited_goal)

        if node_s in visited_goal:
            meet = node_s
            break

        if node_g in visited_start:
            meet = node_g
            break

        for nb in neighbors(node_s):
            if nb not in visited_start:
                visited_start.add(nb)
                parent_start[nb] = node_s
                q_start.append(nb)

        for nb in neighbors(node_g):
            if nb not in visited_goal:
                visited_goal.add(nb)
                parent_goal[nb] = node_g
                q_goal.append(nb)
    else:
        return []

    path_start = []
    n = meet
    while n in parent_start:
        path_start.append(n)
        n = parent_start[n]
    path_start.append(START)
    path_start.reverse()

    path_goal = []
    n = meet
    while n in parent_goal:
        n = parent_goal[n]
        path_goal.append(n)

    return path_start + path_goal


# main

if __name__ == "__main__":
    plt.figure()

    print("1 = BFS | 2 = DFS | 3 = UCS | 4 = DLS | 5 = IDDFS | 6 = Bidirectional")
    choice = input("Enter choice: ")

    if choice == "1":
        path = bfs()
    elif choice == "2":
        path = dfs()
    elif choice == "3":
        path = ucs()
    elif choice == "4":
        path = dls(limit=15)
    elif choice == "5":
        path = iddfs()
    elif choice == "6":
        path = bidirectional()
    else:
        path = []

    draw_grid(path=path)
    print("Final Path:", path)

    plt.show()
