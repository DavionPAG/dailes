# Given an array of integers, calculate the ratios of its elements that are , , and . Print the decimal value of each fraction on a new line with 6 places after the decimal.

def plusMinus(arr):
    # Write your code here
    denom = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
        
    print(round(pos/denom,6), round(neg/denom,6), round(zero/denom,6), sep='\n')
