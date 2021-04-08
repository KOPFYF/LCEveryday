class Solution0:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		# find the root node, assume root is node(0) by default
		# a node without any parent would be a root node
		# note: if there are multiple root nodes => 2+ trees
		root = 0
		childrenNodes = set(leftChild + rightChild)
		for i in range(n):
			if i not in childrenNodes:
				root = i
				break
		
		visited = set([root])
		queue = deque([root])
		
		while queue:
			node = queue.popleft()
			if leftChild[node] in visited or rightChild[node] in visited:
				return False # go back/cycle
			
			if leftChild[node] != -1:
				queue.append(leftChild[node])
				visited.add(leftChild[node])
			if rightChild[node] != -1:
				queue.append(rightChild[node])
				visited.add(rightChild[node])
		# number of visited nodes == given number of nodes
		# if n != len(visited) => some nodes are unreachable/multiple different trees
		return len(visited) == n


class Solution1:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		# find the root node, assume root is node(0) by default
		# a node without any parent would be a root node
		# note: if there are multiple root nodes => 2+ trees
		root = 0
		childrenNodes = set(leftChild + rightChild)
		for i in range(n):
			if i not in childrenNodes:
				root = i
				break # one root is enough, this is O(n) worst
		
		visited = set()
		queue = deque([root])
		
		while queue:
			node = queue.popleft()
			if node in visited:
				return False
			
			visited.add(node)
			if leftChild[node] != -1:
				queue.append(leftChild[node])
			if rightChild[node] != -1:
				queue.append(rightChild[node])
				
		# number of visited nodes == given number of nodes
		# if n != len(visited) => some nodes are unreachable/multiple different trees
		return len(visited) == n
 
class Solution2:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:   
		# topo sort
		indegree = [0] * n
		for left, right in zip(leftChild, rightChild):
			if left > -1: 
				indegree[left] += 1
			if right > -1: 
				indegree[right] += 1
			if indegree[left] > 1 or indegree[right] > 1: 
				return False
		queue = collections.deque(i for i, d in enumerate(indegree) if d == 0) # all possible roots
		
		if len(queue) > 1: # multiple roots
			return False
		while queue:
			node = queue.popleft()
			for child in (leftChild[node], rightChild[node]):
				if child == -1: 
					continue
				indegree[child] -= 1
				if indegree[child] == 0: 
					queue.append(child)
		return sum(indegree) == 0
				
			
			
		