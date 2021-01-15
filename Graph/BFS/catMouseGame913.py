'''
此题是game thoery中的好题．看上去像常规的minMax问题，但实际上几乎所有的DFS解法都是不完备的，参看leetcode的讨论区．

正确的解法是用BFS.我们设计节点状态是(m,c,turn)，用color[m][c][turn]来记忆该状态的输赢情况．

首先我们将所有已知的状态加入一个队列．已知状态包括(0,c,turn)肯定是老鼠赢，(x,x,turn)且x!=0肯定是猫赢．我们尝试用BFS的思路，将这些已知状态向外扩展开去．

扩展的思路是：从队列中取出队首节点状态（m,c,t），找到它的所有邻接的parent的状态（m2,c2,t2）．这里的父子关系是指，(m2,c2,t2)通过t2轮（老鼠或猫）的操作，能得到(m,c,t).我们发现，如果(m,c,t)是老鼠赢而且t2是老鼠轮，那么这个(m2,c2,t2)一定也是老鼠赢．同理，猫赢的状态也类似．于是，我们找到了一种向外扩展的方法．

向外扩展的第二个思路是：对于(m2,c2,t2)，我们再去查询它的所有children（必定是对手轮）是否都已经标注了赢的状态．如果都是赢的状态，那么说明(m2,c2,t2)无路可走，只能标记为输的状态．特别注意的是，第一条规则通过child找parent，和第二条规则通过parent找child的算法细节是不一样的，一定要小心．

这样我们通过BFS不断加入新的探明输赢的节点．直到队列为空，依然没有探明输赢的节点状态，就是平局的意思！

https://www.youtube.com/watch?v=sq6Ggb98A38

https://github.com/wisdompeak/LeetCode/tree/master/BFS/913.Cat-and-Mouse
'''

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # 
        N = len(graph)
        # 0 unvisited, 1 mouse turn, 2 cat turn
        color = [[[0]*3 for _ in range(N)] for _ in range(N)]        
        q = collections.deque()
        for i in range(1,N):            
            for t in range(1,3):                
                color[0][i][t] = 1 # mouse into hole, mouse wins
                q.append((0,i,t))                                                
                color[i][i][t] = 2  # cat wins, (i != 0 cat cannot into hole )          
                q.append((i,i,t))
        
        while (q):
            curStatus = q.popleft()            
            cat,mouse,turn = curStatus
            
            for prevStatus in self.findAllPrevStatus(graph,curStatus):
                
                if color[prevStatus[0]][prevStatus[1]][prevStatus[2]]!=0: continue
                
                # immediate win for prevStatus
                if color[cat][mouse][turn]==3-turn:
                    color[prevStatus[0]][prevStatus[1]][prevStatus[2]] = prevStatus[2]
                    q.append(prevStatus)
                
                # forced to lose for prevStatus
                elif self.allNeighboursWin(color,graph,prevStatus):
                    color[prevStatus[0]][prevStatus[1]][prevStatus[2]] = 3-prevStatus[2]
                    q.append(prevStatus)
            
        return color[1][2][1]
    
    def findAllPrevStatus(self,graph,curStatus):
        ret = []
        mouse,cat,turn = curStatus
        if turn==1:
            for prevCat in graph[cat]:
                if prevCat==0: continue
                ret.append((mouse,prevCat,2))
        else:
            for prevMouse in graph[mouse]:
                ret.append((prevMouse,cat,1))
        return ret
    
    def allNeighboursWin(self,color,graph,status):
        mouse,cat,turn = status
        if turn==1:
            for nextMouse in graph[mouse]:                
                if color[nextMouse][cat][2]!=2:
                    return False
        elif turn==2:            
            for nextCat in graph[cat]:
                if nextCat==0: continue
                if color[mouse][nextCat][1]!=1:
                    return False
        return True



class Solution2:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        # dp[mouse_loc][cat_loc][which_one_moves_first]
        # third index 0 mouse moves first
        # third index 1 cat moves first
        dp = [[[None,None] for j in range(n)] for i in range(n)]
        
        # same structure as dp to count the neighboring moves that makes current player lose
        # if count down goes to 0, then we can decide current move to be a lose for certain
        cd = [[[len(graph[i]),len(graph[j])] for j in range(n)] for i in range(n)]
        
        
        q = deque()
        
        # if a mouse arrives at hole, win for mouse
        for cat_index in range(1,n):
            dp[0][cat_index][0] = 'M'
            q.append((0,cat_index,0))
            dp[0][cat_index][1] = 'M'
            q.append((0,cat_index,1))
        
        # if a cat catches a mouse, win for cat
        for index in range(1,n):
            dp[index][index][0] = 'C'
            q.append((index,index,0))
            dp[index][index][1] = 'C'
            q.append((index,index,1))
        
        # cat can't go in at hole, regard it as lose for cat
        for mouse_index in range(1,n):
            dp[mouse_index][0][0] = 'M'
            q.append((mouse_index,0,0))
            dp[mouse_index][0][1] = 'M'
            q.append((mouse_index,0,1))
        
        
        while q:
            #print(q)
            mouse_loc,cat_loc,move = q.popleft()
            cur_move = 'mouse' if move == 0 else 'cat'
            
            # if previous move is mouse and current state is a win for mouse
            if cur_move == 'cat' and dp[mouse_loc][cat_loc][move] == 'M':
                for mouse_prev in graph[mouse_loc]:
                    if dp[mouse_prev][cat_loc][0] == None:
                        dp[mouse_prev][cat_loc][0] = 'M'
                        q.append((mouse_prev,cat_loc,0))
            
            # if previous move is mouse and current state is a lose for mouse
            elif cur_move == 'cat' and dp[mouse_loc][cat_loc][move] == 'C':
                for mouse_prev in graph[mouse_loc]:
                    cd[mouse_prev][cat_loc][0] -=1
                    if cd[mouse_prev][cat_loc][0] == 0 and dp[mouse_prev][cat_loc][0] == None:
                        dp[mouse_prev][cat_loc][0] = 'C'
                        q.append((mouse_prev,cat_loc,0))
            
            # if previous move is cat and current state is a win for cat
            elif cur_move == 'mouse' and dp[mouse_loc][cat_loc][move] == 'C':
                for cat_prev in graph[cat_loc]:
                    if dp[mouse_loc][cat_prev][1] == None:
                        dp[mouse_loc][cat_prev][1] = 'C'
                        q.append((mouse_loc,cat_prev, 1))
            
            # if previous move is car and current state is a lose for cat
            elif cur_move == 'mouse' and dp[mouse_loc][cat_loc][move] == 'M':
                for cat_prev in graph[cat_loc]:
                    cd[mouse_loc][cat_prev][1] -=1
                    if cd[mouse_loc][cat_prev][1] == 0 and dp[mouse_loc][cat_prev][1] == None:
                        dp[mouse_loc][cat_prev][1] = 'M'
                        q.append((mouse_loc,cat_prev,1))
                        
        
        if dp[1][2][0] == 'C':
            return 2
        elif dp[1][2][0] == 'M':
            return 1
        elif dp[1][2][0] == None:
            return 0