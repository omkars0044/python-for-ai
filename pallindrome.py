def pallindrome(s):
    if s == s[::-1]:
        return "pallindrome"
    else:
        return "not pallindrome"


num = input("Enter number or pallindrome ")
print(pallindrome(num))
