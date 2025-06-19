from collections import deque

class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def bfs(r):
    l = []
    start = r
    queue = deque([r])
    while queue:
        ele = queue.popleft()
        l.append(ele.data)
    
        if ele.left:
            queue.append(ele.left)
        if ele.right:
            queue.append(ele.right)
    return l
                
    

def serialize(root):
    queue = deque([root])
    s = ""
    while queue:
        ele = queue.popleft()
        if type(ele)==str:
            s += ele+","
            continue
        else:
            s += str(ele.data)
            s += ","
        if ele.left:
            queue.append(ele.left)
        else:
            queue.append("#")
            
        if ele.right:
            queue.append(ele.right)
        else:
            queue.append("#")
    return s

def deserialize(s):
    l = s.split(",")
    l.pop()
    i = 0
    root = Tree(int(l[0]))
    q = deque([root])
     
    while q:
        ele = q.popleft()
    
        i += 1
        if l[i] == "#":
            ele.left = None
        else:
            ele.left = Tree(int(l[i]))
            q.append(ele.left)
        i+= 1
        if l[i] == "#":
            ele.right = None
        else:
            ele.right = Tree(int(l[i]))
            q.append(ele.right)
        
    return root
        
            


    print(type(l),l)
        # root = Tree(l[0])
        
    

r = Tree(1)
r.left = Tree(2)
r.right =   Tree(13)
r.left.left = None
r.left.right = None
r.right.left = Tree(4)
r.right.right = Tree(5)
r.right.left.left = None
r.right.left.right = None
r.right.right.left = None
r.right.right.right = None

print(serialize(r))
a = serialize(r)
rooo=deserialize(a)
print(bfs(rooo))