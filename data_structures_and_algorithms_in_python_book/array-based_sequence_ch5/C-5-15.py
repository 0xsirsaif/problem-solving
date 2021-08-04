"""
[Doubling the Array]
in proposition 5.1 we prove that all append operations run in o(n)* in amortized sense.

to sum up the proof we use amortization method called counting, we assume that each cheap append operation take 1$,
and we overcharge it by 3$. when array is full we have to do doubling which we pay for by the $s we did not use in
the previous cheap append operations. we use this analysis patten cause not all append operations require doubling,

we double the array when inserting 2**i th element  [i >= 0]
then each single operation takes o(n)*/n = o(1)*

[increase array by n/4]
BUT if we increase array by n/4 ?

len(new_arr) = n + n/4
- the first note is that the number of resizing operations increases.
- in the same way, the overcharged coins paid for the resizing operation to move elements.
- in the same way, we ensure that the total running time required for resize the array by n/4 = o(n)*

then each single operation takes o(n)*/n = o(1)*

"""