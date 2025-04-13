# This function checks if a given string is a palindrome.
# It ignores spaces and is case-insensitive.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
