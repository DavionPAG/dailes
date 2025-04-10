#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    a_pnt = 0
    b_pnt = 0
    
    for num in range(len(a)):
        if a[num] > b[num]:
            a_pnt+=1
        elif a[num] < b[num]:
            b_pnt+=1
    return [a_pnt,b_pnt]