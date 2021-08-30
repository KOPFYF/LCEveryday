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

# https://docs.python.org/zh-cn/3/library/concurrent.futures.html
'''
Start from the page: startUrl
Call HtmlParser.getUrls(url) to get all URLs from a webpage of a given URL.
Do not crawl the same link twice. (BFS)
Explore only the links that are under the same hostname as startUrl.

We implement a classic BFS but the entries in our queue are future objects instead of primitve values. 
A pool of at most max_workers threads is used to execute getUrl calls asynchronously. 
Calling result() on our futures blocks until the task is completed or rejected.

worker thread only calls htmlParser.getUrls, and that's all a worker does;
bookkeeping of the seen urls are centralized in the main thread, therefore eliminates the need for a lock, 
which is necessary if worker threads also bookkeep seen urls.
'''

from concurrent import futures

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
    
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        
        return list(seen)
        