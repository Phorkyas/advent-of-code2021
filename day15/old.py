#!/usr/bin/env python3

# calculate path of lowest risk
# use Dijkstra algorithm

risk = []
with open('input', 'r') as data:
    lines = data.readlines()
    for line in lines:
        risk.append([int(l) for l in line.strip()])
        

# prepare nodes
# we might get up with x <-> y again...
graph = []
for y in range(len(risk)):
    graph.append([{"visited": False, "risk": 10000000} for x in range(len(risk[y]))])

def visit_neighbors(position, graph):
    x = position[0]
    y = position[1]
    # if neighbor was not evaluated and path through current
    # costs less, then update count
    if x-1 >= 0:
        if not graph[x-1][y]["visited"]:
            if graph[x][y]["risk"] + risk[x-1][y] < graph[x-1][y]["risk"]:
                graph[x-1][y]["risk"] = graph[x][y]["risk"] + risk[x-1][y]
    if x+1 < len(graph[y]):
        if not graph[x+1][y]["visited"]:
            if graph[x][y]["risk"] + risk[x+1][y] < graph[x+1][y]["risk"]:
                graph[x+1][y]["risk"] = graph[x][y]["risk"] + risk[x+1][y]
    if y-1 >= 0:
        if not graph[x][y-1]["visited"]:
            if graph[x][y]["risk"] + risk[x][y-1] < graph[x][y-1]["risk"]:
                graph[x][y-1]["risk"] = graph[x][y]["risk"] + risk[x][y-1]
    if y+1 < len(graph):
        if not graph[x][y+1]["visited"]:
            if graph[x][y]["risk"] + risk[x][y+1] < graph[x][y+1]["risk"]:
                graph[x][y+1]["risk"] = graph[x][y]["risk"] + risk[x][y+1]

    return graph

def get_lowest_unvisited(graph):
    lowest = None
    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if not graph[x][y]["visited"]:
                if lowest == None or graph[x][y]["risk"] < graph[lowest[0]][lowest[1]]["risk"]:
                    lowest = [x, y]
    return lowest


# enter the starting node
position = [0,0]
graph[0][0]["visited"] = True
# special: start node is not counted
graph[0][0]["risk"] = 0

end = [len(graph)-1, len(graph[0])-1]

print(str(end))

while position != end:
    graph = visit_neighbors(position, graph)
    graph[position[0]][position[1]]["visited"] = True

    position = get_lowest_unvisited(graph)

#for y in range(len(graph)):
#    for x in range(len(graph[y])):
#        risk = graph[y][x]["risk"]
#        print(f'{risk:02d}', end=" ")
#    print("")

#print(str(position))
print(graph[end[0]][end[1]]["risk"])
