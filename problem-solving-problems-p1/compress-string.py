
count_this_variable = input('\nType any variable to count its types: \n')



def type_counter(og_variable):
    final_result = ''
    letter_counter = 1 # define a letter counter that begins at 1
    for i in range(len(og_variable)):
        if i == len(og_variable) - 1:
            final_result += str(letter_counter) + og_variable[i]
        elif og_variable[i] == og_variable[i + 1]: # condition if variable at that index == variable ahead of the index by 1 then we + 1 to letter counter
            letter_counter += 1
        elif og_variable[i] != og_variable[i + 1]:
            final_result += str(letter_counter) + og_variable[i]
            letter_counter = 1 # letter counter resets back to 1 everytime all the same variables are accounted for
    print(final_result)


start = type_counter(count_this_variable)