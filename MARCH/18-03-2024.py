from collections import deque

class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        if root is None:
            return []
        
        q=deque()
        out=[]
        q.append(root)
        while q:
            front = q.popleft()
            out.append(front.data)
    
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)

        return out