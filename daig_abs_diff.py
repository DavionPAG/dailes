# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    left_to_right_sum = 0
    right_to_left_sum = 0

    for i in range(n):
        left_to_right_sum += arr[i][i]
        right_to_left_sum += arr[i][n - 1 - i]

    return abs(left_to_right_sum - right_to_left_sum)
