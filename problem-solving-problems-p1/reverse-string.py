# use user input function to get word then save input into a variable
word = input('\nPlease enter a word to be reversed: ') 


# then create a function that would reiterate through the number of characters in the string using a for loop,
# the range, and length function to count the number of characters within the range of how ever long the word is
# the for loop would begin, end, and count down by typing in -1
# then concatenate each character into a new variable called reversed_word then print out that new variable to the
# terminal

def reverser(word):
    reversed_word= ''
    for i in range(len(word) -1, -1, -1): # what does the range function do?
        reversed_word += word[i]
    print('\n', reversed_word, '\n')
    return reversed_word

start_reverser = reverser(word)