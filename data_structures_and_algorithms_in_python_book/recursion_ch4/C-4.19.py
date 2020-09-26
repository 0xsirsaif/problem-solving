"""
Write a short recursive Python function that rearranges a sequence of integer values
 so that all the even values appear before all the odd values.
"""


# ِAlgorithm [1]
def rearrange_even_odd_1(seq):
    def _recur(seq, curr_ptr, even_ptr):
        if curr_ptr == len(seq):
            return seq
        elif seq[curr_ptr] % 2 == 0:
            seq[even_ptr], seq[curr_ptr] = seq[curr_ptr], seq[even_ptr]
            return _recur(seq, curr_ptr+1, even_ptr+1)
        else:
            return _recur(seq, curr_ptr+1, even_ptr)
    return _recur(seq, 0, 0)


# ===========================================
# Algorithm [2]
def rearrange_even_odd_2(seq):
    def _recur(seq, curr_ptr, move_num):
        if move_num == len(seq) - curr_ptr:
            return seq
        elif seq[curr_ptr] % 2 == 0:
            return _recur(seq, curr_ptr+1, move_num)
        else:
            seq.append(seq[curr_ptr])
            del seq[curr_ptr]
            return _recur(seq, curr_ptr+1, move_num+1)
    return _recur(seq, 0, 0)


print(rearrange_even_odd_1([]))
print(rearrange_even_odd_2([]))