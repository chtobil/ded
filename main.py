def is_palindrome(word: str) -> True | False:
    arr = list(word)
    flag = True
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr)-1 -i] :
            flag = False
    return flag
word = "ded"
x = is_palindrome(word)
print(x)
def re_is_palindrome(word: str) -> True | False:
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return re_is_palindrome(word[1:-1])
print(re_is_palindrome(word))
p = 2
o = 4
def power(p:int,o:int):
    if o == 1:
        return p
