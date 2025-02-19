def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

user_word = input("Enter a word to check if it's a palindrome: ")

if palindrome(user_word):
    print(f"{user_word} is a palindrome!")
else:
    print(f"{user_word} is not a palindrome.")