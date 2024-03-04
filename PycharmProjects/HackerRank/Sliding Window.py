# Max number of vowels in a substring
def slidingWindow(s, k):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    substring = s[:k]
    total_vowels = 0
    for char in substring:
        if char in vowel_list:
            total_vowels += 1
    max_vowels = max(0, total_vowels)
    for i in range(len(s)-k):
        if s[i] in vowel_list:
            total_vowels -= 1
        if s[i+k] in vowel_list:
            total_vowels += 1
        max_vowels = max(max_vowels, total_vowels)
    return max_vowels

# string
s = "bacacbefaobeacfe"
# length of the substring
k = 5
# output = 4
print(slidingWindow(s, k))