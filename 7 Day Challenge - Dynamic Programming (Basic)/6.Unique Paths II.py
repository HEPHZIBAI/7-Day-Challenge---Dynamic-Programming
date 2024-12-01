'''
Problem statement
Consider an 'n' * 'm' 2D matrix, 'maze', whose squares may have obstacles.



A cell in the given maze has a value '-1' if it is blocked by an obstacle, or else 0.



From a given cell, you can move to cells ( i+1, j ) and ( i, j+1 ) only, assuming that the following cell does not contain an obstacle.



Count and return the number of unique paths to reach the right-bottom cell from the top-left cell.



Since the answer can be large, print it modulo 10^9 + 7.



Note:
It is guaranteed that the top-left cell does not have an obstacle.
Example :
Input: 'n' = 3, 'm' = 3,
'maze':
[[0, 0, 0], 
[0, -1, 0],
[0, 0, 0]]

There are two ways to reach the bottom left corner - 

(1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)

Hence the answer for the above test case is 2.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
3 3
0 0 0 
0 -1 0 
0 0 0
Sample Output 1:
2
Explanation For Sample Output 1:
For the second test case, there are two ways to reach the bottom left corner - 
(1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)
Sample Input 2:
2 2
0 -1
-1 0
Sample Output 2:
0
Explanation For Sample Output 2:
There are no possible paths.
Expected time complexity:
The expected time complexity is O(n*m).
Constraints :
1 <= 'n', 'm' <= 100
-1 <= 'maze[i][j]' <= 0
Time Limit: 1 sec
'''

from typing import List

def mazeObstacles(n: int, m: int, maze: List[List[int]]) -> int:
    MOD = int(1e9 + 7)
    
    # Initialize DP table
    dp = [[0] * m for _ in range(n)]
    
    # Base case: start cell
    dp[0][0] = 1 if maze[0][0] != -1 else 0
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == -1:
                dp[i][j] = 0  # No paths through obstacles
            else:
                # Add paths from the top cell if it exists
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # Add paths from the left cell if it exists
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                # Take modulo to avoid overflow
                dp[i][j] %= MOD
    
    return dp[n-1][m-1]
