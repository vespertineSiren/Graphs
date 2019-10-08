
def earliest_ancestor(ancestors, starting_node):
    graph = {}

    # 1: Build Graph. Adjacency list
    # 2:  Search Graph at given node
    def connect_node(graph, ancestors):
        parent, child = ancestors
        if not graph.get(child, None):
            graph[child] = [parent]
        else:
            graph[child].append(parent)

    for pair in ancestors:
        connect_node(graph, pair)



    def dft(graph, start):
        stack = []
        visited = set()
        stack.append([start])
        longest = [-1]

        while len(stack) > 0:
            path = stack.pop()
            current = path[-1]

            if current not in visited:
                if len(path) > len(longest):
                    longest = path
                elif len(path) == len(longest):
                    longest = path if path[-1] < longest[-1] else longest

                for parent in graph.get(current, []):
                    stack.append(path + [parent])

        return longest[-1]

    return dft(graph, starting_node)