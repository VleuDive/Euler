def findPalindrome(digits):
    palindrome_list=[]
    number_list=[]
    multiplied=0
    mul1=0
    if_palindrome=False
    for num in range(10**(digits-1),10**digits):
        number_list.append(num)
    for i in number_list:
        mul1=i
        number_list=number_list[1:]
        for mul2 in number_list:
            if_palindrome=False
            multiplied=mul1*mul2
            str_mul=str(multiplied)
            str_rev=str_mul[::-1]
            if (str_mul==str_rev):
                if_palindrome=True
                break;
        if if_palindrome:
            palindrome_list.append(multiplied)
    return palindrome_list

print(max(findPalindrome(3)))
