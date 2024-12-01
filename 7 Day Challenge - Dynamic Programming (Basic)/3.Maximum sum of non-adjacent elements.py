'''
Problem statement
You are given an array 'a' consisting of 'n' integers.



A subsequence of an array is obtained by deleting some elements (can be zero) from the array, leaving the remaining elements in their original order.



Find the maximum sum of a subsequence with the constraint that no two elements in the subsequence are adjacent in the given array.



Example :
Input: 'a' = [1, 2, 3, 4]

Output: 6

Explanation: We can consider the subsequence [2, 4].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
4
1 2 3 4


Sample Output 1:
6


Explanation to Sample Output 1:
We can consider the subsequence [2, 4].


Sample Input 2:
5
5 1 10 20 2


Sample Output 2:
25


Explanation to Sample Output 2:
We can consider the subsequence [5, 20].


Expected time complexity :
The expected time complexity is O(n).


Constraints:
1 <= 'n' <= 10000
0 <= 'a[i]' <= 10 ^ 5

Time Limit: 1 sec.
'''


from typing import List

def maxSumNonAdjacent(a: List[int], n: int) -> int:
    if n == 1:
        return a[0]

    prev2 = 0  
    prev1 = a[0]  

    for i in range(1, n):
        curr = max(prev1, a[i] + prev2)  
        prev2 = prev1
        prev1 = curr
    return prev1