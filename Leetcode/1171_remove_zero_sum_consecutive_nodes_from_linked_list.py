from itertools import accumulate


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        def crash_values(arr):
            visited = {}
            cum_sum = list(accumulate(arr))
            for idx, ele in enumerate(cum_sum):
                exist = visited.get(cum_sum[idx], None)
                if exist is not None or ele == 0:
                    exist = exist if ele == 0 else exist + 1
                    del arr[exist:idx + 1]
                    visited.clear()
                    crash_values(arr)
                    break
                # remove this and put it in the if statement above
                # elif ele == 0:
                #     del arr[exist: idx + 1]
                #     visited.clear()
                #     crash_values(arr)
                #     break
                else:
                    visited[cum_sum[idx]] = idx
            return arr

        list_values = []
        while head:
            list_values.append(head.val)
            head = head.next

        dummy = curr = ListNode(-1)
        for i in crash_values(list_values):
            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next

# TODO -> need optimization !

S = Solution()
print(S.removeZeroSumSublists(ListNode(0)))