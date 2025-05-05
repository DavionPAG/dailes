#given random values, print the total times a value falls within the range

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here

    apples_hit = 0
    oranges_hit = 0
    
    for apple in apples:
        if s <= a + apple <= t:
            apples_hit += 1      
    print(apples_hit)
    
    for orange in oranges:
        if s <= b + orange <= t:
            oranges_hit +=1           
    print(oranges_hit)


