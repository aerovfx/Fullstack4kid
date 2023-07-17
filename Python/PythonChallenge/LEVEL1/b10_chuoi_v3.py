def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    return x

with open('b10_CHUOI.INP', 'r') as file:
    word = file.read().strip().split(',')
    
with open('b10_CHUOI.OUT', 'w') as file:
    x = reverse(word)
    if x == word:
        file.write('this is a palindrome')
    else:
        file.write('this is not a palindrome')