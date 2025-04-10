'return the words in a string in reverse order and swap case of each letter.'

'Ex. input: "HeLlO WoRld" Output: "wOrLD hElLo"'

in_str = "HeLlO WoRld"
result = []
def reverse_word_order_swap_case(in_str):
    rvsr_str = in_str.split(" ")
    rvsr_str = rvsr_str[::-1]
    
    for word in rvsr_str:
        new_str = ""
        for lett in word:
            new_str += lett.swapcase()
        result.append(new_str)    
    return result

print(reverse_word_order_swap_case(in_str))