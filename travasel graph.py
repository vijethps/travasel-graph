def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            traversal.append(node)

            for neighbor in sorted(graph[node],reverse = True):
                if not visited[neighbor]:
                    stack.append(neighbor)
    return traversal
def main():
    V, E = map(int, input().split())
    graph = {i: [] for i in range(V)}
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    start_node = int(input())
    traversal_order = dfs(graph, start_node)
    print(" ".join(map(str, traversal_order)))
if __name__ =="__main__":
    main()
