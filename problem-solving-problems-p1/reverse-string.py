word = input('Please enter a word to be reversed: ')
def reverser(word):
    reversed_word= ''
    for i in range(len(word) -1, -1, -1):
        reversed_word += word[i]
    print(reversed_word)

start_reverser = reverser(word)