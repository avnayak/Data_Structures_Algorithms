def BinaryTree(r):
    return [r,[],[]]
    
def insertLeft(rr,newBranch):
    t=r.pop(1)
    print t
    if len(t)>=1:
        r.insert(1,[newBranch,t,[]])
    else:
        r.insert(1,[newBranch,[],[]])
    return r

#insertLeft([11,[2],[]],4)
    
def insertRight(r,newBranch):
    t=r.pop(2)
    print t
    if len(t)>=1:
        r.insert(2,[newBranch,[],t])
    else:
        r.insert(2,[newBranch,[],[]])
    return r
def setRootValue(l,newValue):
    l[0]=newValue
    
#insertRight([11,[6],[]],1)
r=BinaryTree(3)
l=insertLeft(r,9)
rr=insertRight(r,7)
l=r[1]
rr=r[2]
setRootValue(l,8)
