from typing import Sequence
import numpy as np
# Test 01: Play Right


def playRight(sequence, beats):
    # TO DO
    for i in range(len(beats)):
        j = 0
        if (beats[i]) == 1:
            tmp = sequence[len(sequence)-1]
            for j in range(len(sequence)-2, -1, -1):
                sequence[j+1] = sequence[j]
                # print(j)
            sequence[0] = tmp
    return sequence


print("///  Test 01: Play Right  ///")
sequence = np.array([10, 20, 30, 40, 50, 60])
beats = np.array([1, 0, 0, 1, 0, 1])
returned_value = playRight(sequence, beats)
# This should print [40, 50, 60, 10, 20, 30]
print(f'Task 1: {returned_value}')
