def Read_all():
    lines =  open('input.txt','r').read().split('\n')
    d = open("input.txt").read().split("\n")
    graph = {}
    for s in d:
        b=s.split("-")
        if b[0] in graph: 
            graph[b[0]].append(b[1])
        else: 
            graph[b[0]] = [b[1]]
        if b[1] in graph: 
            graph[b[1]].append(b[0])
        else: 
            graph[b[1]] = [b[0]]
    return graph
paths = set()
def getPaths(graph,path):
    global paths
    if path[-1]=="end":
        paths.add(tuple(path))
        return
    for cord in graph[path[-1]]:
        if cord.islower():
            if not cord in path:
                getPaths(graph,path+[cord])
        else:
            getPaths(graph,path+[cord])
    return

def getPaths2(graph,path,second):
    global paths 
    print(second)
    if path[-1] == "end":
        paths.add(tuple(path))
        return
    for cord in graph[path[-1]]:
        if cord.islower():
            if second=="" and cord!="start":
                getPaths2(graph,path+[cord],cord)
                if not cord in path:
                    getPaths2(graph,path+[cord],"")
            elif second==cord:
                if path.count(cord)==1: 
                    getPaths2(graph,path+[cord],cord)
            else:
                if not cord in path:
                    getPaths2(graph,path+[cord],second)
        else:
            getPaths2(graph,path+[cord],second)
    return
def Part1(graph):
    global paths
    getPaths(graph,["start"])
    return len(paths)
def Part2(graph):
    global paths
    getPaths2(graph,["start"],"")
    return len(paths)


graph = Read_all()
print("part 1:",Part1(graph))
graph = Read_all()
print("part 2:",Part2(graph))







