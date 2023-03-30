# Given an array of strings, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from collections import defaultdict

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

anagram_map = defaultdict(list)
result = []

for s in strs:
    sorted_s = tuple(sorted(s))
    anagram_map[sorted_s].append(s)


for value in anagram_map.values():
    result.append(value)

print(result)

# youtube video answer: https://www.youtube.com/watch?v=RcZsTI5h0kg&t=10s