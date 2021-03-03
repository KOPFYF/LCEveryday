# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = startUrl.split("/")[2]
        
        bfs, seen = deque([startUrl]), set([startUrl])
        while bfs:
            cur = bfs.popleft()
            for nxt in htmlParser.getUrls(cur):
                if hostname in nxt and nxt not in seen:
                    bfs.append(nxt)
                    seen.add(nxt)
        
        return seen