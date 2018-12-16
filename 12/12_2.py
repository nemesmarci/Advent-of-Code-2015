import sys
import json

line = sys.stdin.readline().strip()
tree = json.loads(line)

def sum_json(node):
    sum_of_node = 0
    if type(node) == int:
        sum_of_node += node
    elif type(node) == list:
        for item in node:
            sum_of_node += sum_json(item)
    elif type(node) == dict:
        if 'red' not in node.values():
            for key in node:
                sum_of_node += sum_json(node[key])
    return sum_of_node

print(sum_json(tree))