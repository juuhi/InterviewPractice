# Given an integer x, return true if x is a palindrome and false otherwise.

 # Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

##########################################
def pal(num):
    if num < 0:
        return False
    rev_num = 0
    number = num
    while num > 0:
        digit = num % 10 # 122 : 2
        num = num // 10 # 122 : 12.  1
        rev_num = rev_num * 10 + digit # 20 + 2 22 220+ 1 221
    return number == rev_num
  
print(pal(2221))
print(pal(121))
print(pal(-10))
print(pal(10))
