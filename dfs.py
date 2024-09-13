graph=  {
's':['a','b','d'],
'a':['c'],
'b':['d'],
'c':['d','g'],
'd':['g']

}   




def dfs(graph,start,goal):
    visited=[]
    stack=[[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            next_node=graph.get(node,[])
            for node2 in next_node:
                new_path=path.copy()
                new_path.append(node2)
                stack.append(new_path)
sol=dfs(graph,'s','g')
print(sol)
           