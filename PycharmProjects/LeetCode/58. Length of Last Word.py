def lengthOfLastWord(s):
    words = s.split(" ")
    return words[-1]
    # last_word = ""
    # i = -1
    # while s[i] != " ":
    #     last_word += s[i]
    #     i -= 1
    # last_word_convert = ""
    # for i in range(-1, -len(last_word)):
    #     last_word_convert += last_word[i]
    # return last_word_convert

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
s = "Hello World"
print(lengthOfLastWord(s))
