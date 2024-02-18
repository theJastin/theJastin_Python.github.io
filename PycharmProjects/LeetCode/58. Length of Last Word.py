def lengthOfLastWord(s):
    first_letter_ind = 0
    word_len = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " " and first_letter_ind == 0:
            first_letter_ind = i
            word_len += 1
        elif s[i] != " " and first_letter_ind > 0:
            word_len += 1
        elif s[i] == " " and first_letter_ind > 0:
            return word_len
    if word_len == 0:
        return -1
    else:
        return word_len

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
s = "a"
print(lengthOfLastWord(s))
