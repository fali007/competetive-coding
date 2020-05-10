import heapq
class graph:
    def __init__(self,val):
        self.gr=val
        self.edge=[]
        self.vertices=[]
        for i in self.gr:
            if i not in self.vertices:
                self.vertices.append(i)
            for j in self.gr[i]:
                if [i,j] not in self.edge:
                    self.edge.append([i,j])
                if j not in self.vertices:
                    self.vertices.append(j)
    def draw(self,args=''):
        if args=='':
            print(self.gr)
            print(self.edge)
            print(self.vertices)
        elif args=='edge':
            print(self.edge)
        elif args=='vertices':
            print(self.vertices)
    def bfs(self,s,d=''):
        q=[]
        bfs=[]
        bfs.append(s)
        q.append(s)
        while len(q):
            temp=q.pop(0)
            for i in self.gr[temp]:
                if i not in bfs:
                    q.append(i)
                    if d==i:
                        bfs.append(i)
                        return bfs
                    bfs.append(i)
        return bfs
    def dfs(self,s,d=''):
        q=[]
        dfs=[]
        dfs.append(s)
        q.append(s)
        while len(q):
            temp=q.pop(-1)
            for i in self.gr[temp]:
                if i not in dfs:
                    q.append(i)
                    if d==i:
                        dfs.append(i)
                        return dfs
                    dfs.append(i)
        return dfs
    def dijkstra(self,s,d):
        heap=heapq()
        q=[]
        q.append(s)
        visited={s:0}
        while len(q):
            temp=q.pop(0)

map = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }

g=graph(map)
# g.draw()
print(g.bfs('c','b'))
print(g.dfs('c','b'))