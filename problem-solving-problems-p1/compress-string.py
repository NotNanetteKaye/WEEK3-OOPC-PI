count_this_variable = input('Type any variable to count its types: ')
def type_counter(og_variable):
    final_result = ''
    letter_counter = 1
    for i in range(len(og_variable)):
        if i == len(og_variable) - 1:
            final_result += str(letter_counter) + og_variable[i]
        elif og_variable[i] == og_variable[i + 1]:
            letter_counter += 1
        elif og_variable[i] != og_variable[i + 1]:
            final_result += str(letter_counter) + og_variable[i]
            letter_counter = 1
    print(final_result)


start = type_counter(count_this_variable)