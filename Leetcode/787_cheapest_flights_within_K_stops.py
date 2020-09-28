def draw_paths(flights):
    paths_tree = {}
    for flight in flights:
        try:
            paths_tree[str(flight[0])] += [flight[1:]]
        except:
            paths_tree[str(flight[0])] = [flight[1:]]
    return paths_tree


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        pass


s = Solution()
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))