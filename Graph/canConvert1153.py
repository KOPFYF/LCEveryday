class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        d = {}
        for i in range(len(str1)):
            if str1[i] not in d:
                d[str1[i]] = str2[i] # building a mapping
            elif d[str1[i]] != str2[i]: # 'aa' -> 'bc' is not possible
                return False
        
        # below is for cycle
        # transformation of cycle, like a -> b -> c -> a:
        # in this case we need a tmp, c->tmp, b->c a->b and tmp->a
        return len(set(str2)) < 26