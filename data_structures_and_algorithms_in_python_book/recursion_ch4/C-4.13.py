"""
In Section 4.2 we prove by induction that the number of lines printed by
a call to draw interval(c) is 2^c − 1. Another interesting question is how
many dashes are printed during that process. Prove by induction that the
number of dashes printed by draw interval(c) is 2^c+1 − c − 2.
"""
"""
[1] initial step
for the base cases:
    interval(0) -> 0
    interval(1) -> 1
    interval(2) -> 4

[2] inductive step
from the code implementation we observe that:
each call to interval(c) invokes
    1- two calls of interval(c-1) and 
    2- a call to line(c) which draws c dashes
    
our goal is to count the number of the printed dashes of interval(c),
 so we need to count each (c) inter to every call to line(c) function inside the stack of interval(c).

from [2] -> interval(c) draw X dashes where:
X = 2(dashes printed by interval(c-1) + c (which is the input of the line(c) func)

for interval(c) = 2[interval(c-1)] + c 
                = 2[2^(c-1+1) - (c-1) -2] + c
                = 2*2^c - 2c -2 -4 +c
                = 2^c+1 -c - 2
"""