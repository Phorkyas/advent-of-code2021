#!/usr/bin/env python3

connections = []
with open('input', 'r') as data:
    lines = data.readlines()
    for line in lines:
        con = line.strip().split('-')
        connections.append(con)
        connections.append([con[1],con[0]])

print(str(connections))

class Node:
    def __init__(self, name, parent = None):
        self.name = name
        self.children = []
        self.parent = parent
        self.evaluated = False
    def append_node(self, node):
        self.children.append(node)

    def get_path(self):
        path = []
        node = self
        while node != None:
            path.append(node.name)
            parent = node.parent
            node = parent
        return path

def is_small(name):
    for letter in name:
        if letter not in "abcdefghijklmnopqrtstuvwxyz":
            return False
    return True

def next_nodes(node, cons):
    if node.name == "end":
        return []
    nodes = []
    for con in cons:
        # don't go back to start
        if con[0] == node.name and con[1] != "start":
            # small caves can only be visited once
            if is_small(con[1]):
                if con[1] in node.get_path():
                    print(con[1] + " already visited in: " + str(node.get_path()))
                    continue
            nodes.append(con[1])
    return nodes

# if there is an unevaluated child: elect it -
# otherwise look if a child has not yet been created -
#   if so create and return it
def create_or_choose_child(node, connect, nodes):
    for child in node.children:
        if not child.evaluated:
            print("unevaluated child: " + child.name)
            return child
    
    all_conn = next_nodes(node, connect)
    all_child = [child.name for child in node.children]
    print("existing connections: " + str(all_child))
    print("possible connections: " + str(all_conn))
    for candidate in all_conn:
        if candidate not in all_child:
            print(node.name + " has new path created to: " + str(candidate))
            new_node = Node(candidate, node)
            node.children.append(new_node)
            nodes.append(new_node)
            return new_node
    print(node.name + " has no paths left.")
    return None

# prepare tree
root = Node("start")
nodes = [root]        
node = root
count = 0
while node and not node.evaluated:
    # if tree can be extended or child not evaluated:
    #   descend into it
    new_node = create_or_choose_child(node, connections, nodes)
    if new_node != None:
        print("from " + node.name + " descend to: " + new_node.name)
        node = new_node
    else:
        # node is a dead end:
        # move up and look for unevaluated branches
        print("dead end at: " + node.name)
        node.evaluated = True
        up = node.parent
        if up:
            print("just go up to: " + up.name)
        node = up
    count += 1
    if count > 100000:
        print("oops")
        break

number = 0
for paths in nodes:
    if paths.name == "end":
        number += 1
        print(str(paths.get_path()))

print("count: " + str(number))
