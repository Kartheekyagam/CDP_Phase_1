class Box:
    def __init__(self, data):
        self.data=data
        self.left= None
        self.right= None
def printInorder(root):
    if root==None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

def printPreorder(root):
    if root==None:
        return
    print(root.data, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)

def printPostorder(root):
    if root==None:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.data, end=" ")
    
obj1= Box(1)
obj2= Box(28)
obj3= Box(27)
obj4= Box(-105)
obj5= Box(-18)
obj6= Box(-15)
obj7= Box(22)
obj8= Box(82)

obj4.left=obj1
obj4.right=obj8
obj1.right=obj2
obj2.left= obj3
obj8.left=obj6
obj6.left=obj5
obj6.right=obj7

printInorder(obj4)
print(" ")
printPreorder(obj4)
print(" ")
printPostorder(obj4)