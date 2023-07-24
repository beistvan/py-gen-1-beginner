def is_one_away(word1, word2):
    if len(word1) == len(word2):
        c = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                c += 1
        return len(word1) - c == 1
    else:
        return False

txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
