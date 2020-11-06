"""
Given a list of strings words representing an English dictionary, find the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order (ie. The one that comes first alphabetically).
If there is no answer, return the empty string.

Example 1:
Input: words = [“w”,”wo”,”wor”,”worl”,”world”]
Output: “world”

Example 2:
Input: words = [“a”,”banana”,”app”,”appl”,”ap”,”apply”,”apple”]
Output: “apple”

"""

def compare_words(word1, word2):
    if len(word1) > len(word2):
        return word1
    if len(word2) > len(word1):
        return word2
    if word1 < word2:
        return word1
    return word2

def find_candidate_word(words):
    candidate = words[0]
    for word in words:
        candidate = compare_words(candidate, word)
    return candidate

def test_candidate(candidate, words):
    if len(candidate) == 0:
        return True
    if candidate in words:
        return test_candidate(candidate[0:-1], words)
    else:
        return False

def find_solution(input_words):
    words = input_words.copy()
    while len(words) > 0:
        candidate = find_candidate_word(words)
        if test_candidate(candidate, words):
            return candidate
        words.remove(candidate)
    return ""

sample_words = ["wo", "w", "world", "apple", "worl", "wor", "appl", "app", "ap"]
print(find_solution(sample_words))