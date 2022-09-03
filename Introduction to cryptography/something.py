def Build(low, high, treeIndex, pos, val): # 1 node update
	global Tree
	if (low == high):
		Tree[treeIndex] = val
		return
	mid = (low + high)>>1
	if (mid < pos):
		Build(mid + 1, high, (treeIndex<<1)|1, pos, val)
	else:
		Build(low, mid, treeIndex<<1, pos, val)

	Tree[treeIndex] = min(Tree[treeIndex<<1],Tree[(treeIndex<<1)|1])
	return
const = 10**9 + 1
def Query(low, high, treeIndex, left, right):
	global Tree
	if (low > high):
		return const
	if (right < low or left > high):
		return const
	if (left <= low and high <= right):
		return Tree[treeIndex]
	mid = (low + high)>>1
	L = Query(low, mid, (treeIndex<<1) , left, right)
	R = Query(mid + 1, high, (treeIndex<<1) | 1, left, right)
	return min(L,R)


n, q = map(int,input().split())

arr = list(map(int,input().split()))
Tree = [0 for _ in range(4 * n + 1)]
for i in range(n):
	Build(1, n, 1, i+1, arr[i])

for i in range(q)
:	left, right = map(int,input().split()
)	res = Query(1, n, 1, left, right)
	print(res)



dfs -> return mảng chứa các ô của cái hồ, outside
pos, outside = dfs(i, j)
if (not outside):
	c += 1
	Lakes.append(pos)

Lakes.sort(lambda x: len(x))