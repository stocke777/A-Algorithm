from queue import PriorityQueue
from collections import defaultdict

# Heuristic Function based on Manhattan Distance
def h(point1, point2):
    x, y = point1
    a, b = point2
    return abs(x-a)+abs(y-b)

# Priority Queue for getting minimum F_score node always in log(n) time
pq = PriorityQueue()

# Grid of 10*10
g = [[0 for i in range(10)] for j in range(10)]

# Start and End
start = (0, 0)
end = (9, 5)

# Source = 1, End = 2
g[end[0]][end[1]] = 2
g[0][0] = 1

# obstacles using digit 3
for i in range(2, 10):
    g[4][i] = 3
for i in range(0, 9):
    g[7][i] = 3

# g_score of nodes using dictionary with default value "inf"
g_score = defaultdict(lambda: float("inf"))
g_score[start] = 0

# g_score of nodes using dictionary with default value "inf"
f_score = defaultdict(lambda: float("inf"))
f_score[start] = g_score[start] + h(start, end)

# put start node into Priority Queue
pq.put((0, start))

# Hash set for checking if node is in Priority Queue in Time O(1)
pq_hash = set()
pq_hash.add(start)

# Dictionary to keep track of the path we came from
came_from = dict()

# flag to know if we got to end or not, if we did then f = 1 and we check that at last
f = 0

# Main loop until Queue is not empty
while not pq.empty():

    # get current node with its f_score eg. (f_score, (node_x, node_y))
    current = pq.get()

    # if node is the end, flag = 1 and break the loop
    if g[current[1][0]][current[1][1]]==2:
        print("last reached\n")
        f = 1
        break

    # for traversing in 4 directions, up, down, right, left in order
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    # remove the node from set too cause set basically tracks pq
    pq_hash.remove(current[1])


    # traversing 4 neighbor nodes
    for r, c in zip(x, y):

        # check if node is in boundaries of grid
        if 0<=current[1][0]+r<=9 and 0<=current[1][1]+c<=9:

            # let temporary g_score be 1 + g_score of the node we came from i.e current node
            temp_g_score = current[0] + 1

            # if tempp_g_score is less than the score we had for this node, set that score
            if temp_g_score < g_score[(r+current[1][0], c+current[1][1])]:
                g_score[(r+current[1][0], c+current[1][1])] = temp_g_score

                # to keep track of where we came from to this node
                came_from[(r+current[1][0], c+current[1][1])] = current[1]

                # f_score = g_score + h_score of the node
                f_score[(r+current[1][0], c+current[1][1])] = g_score[(r+current[1][0], c+current[1][1])] + h((r+current[1][0], c+current[1][1]), end)
                
                # if the node we are on is not in priority queue and is not an obstacle, then add it to pq
                if ((r+current[1][0], c+current[1][1]) not in pq_hash) and g[r+current[1][0]][c+current[1][1]] != 3:
                    pq.put((f_score[(r+current[1][0], c+current[1][1])], (r+current[1][0], c+current[1][1])))
                    pq_hash.add((r+current[1][0], c+current[1][1]))

# check if we reached end or not
if not f:
    print("failed")		
else:
    print("passed")		

    # Using came_from we make the path from end to start using 5 as path
    while True:
        x, y = came_from[end]
        if (x, y) == start:
            break
        g[x][y] = 5
        end = (x, y)

    # Print the grid
    for i in g:
        print(i)


        

