class Tree:
    def  __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        


def morris(root):
    curr = root
    res = []
    while curr:
        if not curr.left:
            res.append(curr.data)
            curr = curr.right
        else:
            temp = curr.left
            while temp.right and  temp.right is not curr:
                temp = temp.right
            if temp.right is None:
                temp.right = curr 
                curr = curr.left
            else:
                
                temp.right = None
                res.append(curr.data)
                curr =curr.right
                
    print(res)
    return res
        


    return None
r = Tree(1)
r.left = Tree(2)
r.right =   Tree(3)
r.left.left = Tree(4)
r.left.right = Tree(5)
r.left.right.right = Tree(6)


print(morris(r))