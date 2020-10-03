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
        tree = draw_paths(flights)
        cheapest = 1000 ** 1000

        def _recur(node, price, k):
            try:
                for i in tree[str(node)]:
                    if k > K:
                        continue
                    if i[0] == dst:
                        total = price + i[1]
                        nonlocal cheapest
                        if total <= cheapest:
                            cheapest = total
                    else:
                        _recur(str(i[0]), price + i[1], k + 1)
            except:
                pass

        _recur(src, 0, 0)
        return cheapest if (cheapest < 1000 ** 1000) else -1

s = Solution()
print(s.findCheapestPrice(17, [], 13, 4, 13))

