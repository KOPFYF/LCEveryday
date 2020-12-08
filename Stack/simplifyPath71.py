class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for d in path.split('/'):
            if d == '..' and stack:
                stack.pop()
            if d not in ('','.','..'):
                stack.append(d)
            # print(stack)
        return '/'+'/'.join(stack)