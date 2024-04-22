def is_palindrome(word):
    check = word[::-1]
    if  check == word : return True
    else:
        return False
    

print(is_palindrome('radar'))
        