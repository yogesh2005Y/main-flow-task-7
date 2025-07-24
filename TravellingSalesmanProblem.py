from itertools import permutations

def tsp(graph):
    n = len(graph)
    min_path = float('inf')
    best_route = []
    for perm in permutations(range(n)):
        cost = sum(graph[perm[i]][perm[i+1]] for i in range(n - 1))
        cost += graph[perm[-1]][perm[0]]  # Return to start
        if cost < min_path:
            min_path = cost
            best_route = perm
    return best_route, min_path

graph = [[0, 10, 15], [10, 0, 20], [15, 20, 0]]
route, cost = tsp(graph)
print("Best Route:", route, "Cost:", cost)
