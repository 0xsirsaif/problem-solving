"""
Given an unsorted sequence, S, of integers and an integer k, describe a
recursive algorithm for rearranging the elements in S so that all elements
less than or equal to k come before any elements larger than k. What is
the running time of your algorithm on a sequence of n values?
"""

def rearrange_due_to_num(seq, k):
    def _recur(seq, k, curr_ptr, move_count):
        if (move_count == len(seq) - curr_ptr -1) or not seq:
            return seq
        elif seq[curr_ptr] >= k:
            seq.append(seq[curr_ptr])
            del seq[curr_ptr]
            return _recur(seq, k, curr_ptr, move_count+1)
        else:
            return _recur(seq, k, curr_ptr+1, move_count)
    return _recur(seq, k, 0, 0)

print(rearrange_due_to_num([1], 2))