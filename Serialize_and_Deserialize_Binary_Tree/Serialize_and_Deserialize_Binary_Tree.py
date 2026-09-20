# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ''
        
        rtn = []

        # need to do level order traversal
        q = deque([root])

        while q:
            node = q.popleft()
            if node is None:
                rtn.append('null')
                continue

            rtn.append(str(node.val))

            q.append(node.left)
            q.append(node.right)
        
        return ','.join(rtn)



    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # return TreeNode(data)

        if not data:
            return None

        data = data.split(',')
        root = TreeNode(data[0])
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()

            # left
            if i < len(data) and data[i] != 'null':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i+=1
            #right
            if i < len(data) and data[i] != 'null':
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i+=1
        
        return root



