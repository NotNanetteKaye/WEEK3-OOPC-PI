original_word = input('Type in palindrome word: ')
def palindrome_finder(potential_word):
    final_result = ''
    for i in range(len(potential_word) -1, -1, -1):
        final_result += potential_word[i]
    if final_result == potential_word:
        print(f'{potential_word} is a palindrome!')
    else:
        print(f'{potential_word} is not a palindrome.')

start = palindrome_finder(original_word)