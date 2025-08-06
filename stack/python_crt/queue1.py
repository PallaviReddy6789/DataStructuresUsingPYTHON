def levelorder(rrot): 
    queue=[]
    ans=[]
    queue=[root]
    while(len(queue)>0):
        popElememt = queue.pop(0)
        if(popElement.left):
            queue.append(popElement.left)
        if(popElement.right):
            queue.append(popElement.right)
        ans.append(popElement.data)
    return ans