class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # maintain prev list and cur list
        stack, union, product = [], [], ['']
        for c in expression:
            if c.isalpha():
                # grow the current str, [a]*b -> ab
                product = [p + c for p in product]
            elif c == '{':
                # push into stack for the last group {}
                stack.append(union)
                stack.append(product)
                union, product = [], [''] # init for merging
            elif c == '}':
                # cross multiplying the result inside "{ }" into the second list.
                pre_product = stack.pop()
                pre_union = stack.pop()
                # print('pre_product/product:', pre_product, product)
                # print('pre_union/union:', pre_union, union)
                product = [p + r for r in product + union for p in pre_product]
                union = pre_union
            elif c == ',':
                # the second list can't grow anymore. combine with the first list 
                union += product
                product = ['']
            # print(union, product, stack)
        return sorted(set(union + product))


'''
Use stack for "{" and "}" just like in calculator.
Maintain two lists:
  1. the previous list before ",",
  2. the current list that is still growing.
  
When seeing an "alphabet", grow the second list by corss multiplying. So that [a]*b will become "ab", [a,c]*b will become ["ab", "cb"]
When seeing ",", that means the second list can't grow anymore. combine it with the first list and clear the second list.
When seeing "{", push the two lists into stack,
When seeing "}", pop the previous two lists, cross multiplying the result inside "{ }" into the second list.

If not considering the final sorting before return, the time complexity should be O(n)

'''
class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        # stack
        stack, cur, res = [], [], []
        for i, ch in enumerate(expression):
            if ch.isalpha():
                cur = [c + ch for c in cur or ['']]
            elif ch == ',':
                res += cur
                cur = []
            elif ch == '{':
                # push the two lists into stack
                stack.append(res)
                stack.append(cur)
                res, cur = [], []
            elif ch == '}':
                pre = stack.pop()
                pre_res = stack.pop()
                cur = [p + c for c in res + cur for p in pre or ['']]
                res = pre_res
            print(i, ch, cur, res, stack)
        return sorted(set(res + cur))