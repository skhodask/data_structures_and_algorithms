''' 
in pre-order traversal, we can process the nodes depth-wise both iteratively and recursively.
process -> left subtree -> right subtree
'''

''' recursive pre-order traversal '''
def preorder(root):
  if root is None:
    return
  print(root.val)
  preorder(root.left)
  preorder(root.right)

''' recursive pre-order traversal, aggregate values in list '''
def preorder(root):
  if root is None:
    return []
  return [root.val] + preorder(root.left) + preorder(root.right) 


''' iterative pre-order traversal '''
from collections import deque
def preorder(root):
  if root is None:
    return
  stack = deque([root])
  while stack:
    node = root.pop()
    if type(node) == list: 
      print(node[0].val)
      continue
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
    stack.append([node])
    
'''
since we're using a stack to mimic the function call stack during recursion, we must process the order in reverse:
right subtree -> left subtree -> process
because when we pop items off the stack, we'll then get: process -> left subtree -> right subtree
'''
