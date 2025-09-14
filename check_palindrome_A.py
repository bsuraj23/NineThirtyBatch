def check_palindrome(str):
    left,right=0,len(str)-1
    while left<right:
        if str[left]!=str[right]:
            return False
        left=left+1
        right=right-1
    return True
print(check_palindrome("racecar"))