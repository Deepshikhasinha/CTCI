"""

Graph dfs

"""

# DFS will have stack because you first see through the entire path as far as it can take you and then backtrack


V = ['A','B','C','D','E']
E = [['A','B'],['B','C'],['C','D'],['D','A'],['D','E']]

visited = []
start = 'A'
stack = []
stack.append(start)
while stack:
    print(stack)
    cur = stack.pop(0)
    if cur not in visited:
        visited.append(cur)
        for i in E:
            for j in range(2):
                if i[0] == cur :
                    #print(stack)
                    if i[1] not in stack and i[1] not in visited:
                        stack.append(i[1])
                elif i[1] == cur:
                    if i[0] not in stack and i[0] not in visited:
                        stack.append(i[0])
        
print(visited)
