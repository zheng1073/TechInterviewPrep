Previous lecture:
BFS --> layer by layer, shortest path

## Lecture 14: Depth-First Search (DFS)
- recursively explore graph, backtracking as necessary

```python
parent = {s: None}

def DFS-Visit(v, Adj, S):
  for v in Adj[S]:
     if v not in parent:
      parent[v] = S
      DFS-Visit(v, Adj, u)
```




