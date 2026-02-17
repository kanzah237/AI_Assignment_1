# AI_Assignment_1
AI Pathfinder – Uninformed Search in Grid Environment
This project implements and visualizes six uninformed search algorithms in a grid-based environment.
The goal is to demonstrate how each algorithm explores the map step-by-step while navigating from a Start node (S) to a Target node (T) while avoiding walls.
The visualization is created using Matplotlib and shows:
Explored nodes (already visited)
Final successful path
Real-time animation of the search process
Algorithms Implemented
The following uninformed search strategies are included:
Breadth-First Search (BFS)
Depth-First Search (DFS)
Uniform-Cost Search (UCS)
Depth-Limited Search (DLS)
Iterative Deepening DFS (IDDFS)
Bidirectional Search
All algorithms follow the strict clockwise movement order required in the assignment:
Up → Right → Bottom → Bottom-Right → Left → Top-Left
(Top-Right and Bottom-Left diagonals are not allowed.)

Blue/Light cells → Frontier nodes
Gray cells → Explored nodes
Highlighted path → Final solution
Green cell → Start node
Red cell → Target node
Black cells → Walls/obstacles

Best-Case and Worst-Case Testing
Each algorithm was tested in:
Best case: Target is near the start → minimal exploration
Worst case: Target is far or blocked → large portion of grid explored

<img width="644" height="560" alt="image" src="https://github.com/user-attachments/assets/5316668d-60c3-4ea6-bf53-f10670a2c2c0" />
<img width="1271" height="179" alt="image" src="https://github.com/user-attachments/assets/d0aad8d6-59d1-493f-bae5-1e7f7cfa70d0" />

