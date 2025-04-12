# This is a staircase

#    #
#   ##
#  ###
# ####

def staircase(n):
    # Write your code here
    for i in range(n):
        n = n-1
        print(" "*n + '#'*(i+1))
