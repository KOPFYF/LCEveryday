class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        i, j, k = 0, 0, 0
        res = []
        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                min_num = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == min_num:
                    i += 1
                if arr2[j] == min_num:
                    j += 1
                if arr3[k] == min_num:
                    k += 1
        return res