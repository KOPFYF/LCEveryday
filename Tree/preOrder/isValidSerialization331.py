class Solution_iteration:
    def isValidSerialization(self, preorder: str) -> bool:
        # Iteration
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot
        slot = 1
        for node in preorder.split(','):
            # case1, no empty slot to put the current node
            if slot == 0:
                return False
            # check node is valid or not
            if node == '#':
                slot -= 1
            else:
                slot += 1
        # don't allow empty slots at the end
        return slot == 0


'''
Similar to Problem 297: Serialize and Deserialize Binary Tree, but here we do not really need to reconstruct our tree, and using stack is enough. The trick is to add elements one by one and when we see num, #, #, we replace it with #. If we get just one # in the end, return True, else: False. Let us look at the example 9,3,4,#,#,1,#,#,2,#,6,#,#. Let us go through steps:

We add elements until we have 9, 3, 4, #, #. It means now that 4 is leaf, so let us remove it: we have 9, 3, #.
Add elements, so we have 9, 3, #, 1, #, #. We have leaf 1, remove it: 9, 3, #, #. Now, we have 3 as leaf as well: remove it: 9, #.
Add elements 9, #, 2, #, 6, #, # -> 9, #, 2, #, # -> 9, #, # -> #.
Complexity
It is O(n) for time and O(h) for space, where h is the height of our binary tree.
'''
class Solution_stack:
    def isValidSerialization(self, preorder: str) -> bool:
        # stack, when we see num, #, #, we replace it with #
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) > 2 and stack[-2:] == ["#"] * 2 and stack[-3] != "#":
                stack.pop(-3)
                stack.pop(-2)
            
        return stack == ["#"]