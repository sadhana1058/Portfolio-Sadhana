from collections import deque

class Node:
    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def TreeConstruct(postorder,inorder):

    def helper(postord,inord):

        if len(postord)==0 or len(inord)==0:
            return None
        
        root_val = postord[-1]
        root = Node(root_val)

        ind = inord.index(root_val)
        inordl = inord[:ind]
        inordr = inord[ind+1:]
        left_len,right_len = ind,len(inord)-(ind+1)
        postordl = postord[:left_len]
        postordr = postord[ind:-1]


        root.left = helper(postordl,inordl)
        root.right = helper(postordr,inordr)
        

        return root
    
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
                
    return bfs(helper(postorder,inorder))

p = [4,5,2,3,1]
ino = [4,2,5,1,3]

print(TreeConstruct(p,ino))