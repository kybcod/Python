#팰린드롬(회문) : 앞에서 읽으나 거꾸로 읽으나 똑같은 단어(Hannah, racecar)
def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    else: return False

print(is_palindrome("racecar"))
print(is_palindrome("raceaefecar"))