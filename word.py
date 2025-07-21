def match_word(words) :
    c = 0
    l = []
    for word in words :
        if len(word) > 1 and word[0] == word[-1] :
            c += 1 
            l.append(word)
    print("list of the words with first and last charectars same",l)
    return c
count = match_word(['abc','mom','xyz','1221','cfc'])
print("number of words having the first and last charechtar same",count)