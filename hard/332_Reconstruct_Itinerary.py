from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = None
        self.tickets_len = None

    def find_smallest_lexical(self, start, current_path):
        if len(current_path) == self.tickets_len + 1: return current_path
        if start not in self.graph: return None

        tmp_edges = list(self.graph[start])
        for i, dst in enumerate(tmp_edges):
            current_path.append(dst)
            self.graph[start].pop(i)
            answer = self.find_smallest_lexical(dst, current_path)
            if answer is not None:
                return answer
            self.graph[start].insert(i, dst)
            current_path.pop()
        return None

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        self.graph = graph
        self.tickets_len = len(tickets)
        return self.find_smallest_lexical("JFK", ["JFK"])
