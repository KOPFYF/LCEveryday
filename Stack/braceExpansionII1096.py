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