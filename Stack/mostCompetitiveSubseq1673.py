class Solution:
    def mostCompetitive(self, A: List[int], k: int) -> List[int]:
#         Keep a mono inc stack as result.
#         If current element a is smaller then the last element in the stack,
#         we can replace it to get a smaller sequence.

#         Before we do this,
#         we need to check if we still have enough elements after.
#         After we pop the last element from stack,
#         we have stack.size() - 1 in the stack,
#         there are A.size() - i can still be pushed.
#         if stack.size() - 1 + A.size() - i >= k, we can pop the stack.

#         Then, is the stack not full with k element,
#         we push A[i] into the stack.

#         Finally we return stack as the result directly.
        stack = []
        for i, a in enumerate(A):
            while stack and stack[-1] > a and len(stack) - 1 + len(A) - i >= k:
                stack.pop()
                # print('while:', stack)
            if len(stack) < k:
                stack.append(a)
                # print('if:', stack)
        return stack