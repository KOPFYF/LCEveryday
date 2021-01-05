# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        """
        :type text: str
        :type w: int
        :type h: int
        :type fonts: List[int]
        :type fontInfo: FontInfo
        :rtype: int
        """
        def check(font):
            if fontInfo.getHeight(font) > h:
                return False
            if sum(fontInfo.getWidth(font, c) for c in text) > w:
                return False
            return True
        
        l, r = 0, len(fonts) - 1
        while l < r:
            mid = (l + r) // 2
            if check(fonts[mid + 1]): # bisect_right
                l = mid + 1
            else:
                r = mid
            print(l, r, mid, check(fonts[mid]), check(fonts[mid + 1]), fonts[l])
        return fonts[l] if check(fonts[l]) else -1
    
        # l, r = 0, len(fonts) - 1
        # while l < r:
        #     mid = r - (r - l) // 2
        #     if check(fonts[mid]):
        #         l = mid
        #     else:
        #         r = mid - 1
        # return fonts[l] if check(fonts[l]) else -1
         