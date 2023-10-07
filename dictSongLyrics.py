#to get the number of times, a word has appeared in the song

def lyrics_to_freq(lyrics):
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word] = myDict[word]+1
        else:
            myDict[word]=1
    return myDict 

song=["hey","there","what","you","hey","there"]
print(lyrics_to_freq(song))


#to find most common words in the song
def most_common_words(freq):
    values=freq.values()
    best=max(values)
    words=[]
    for k in freq:
        if freq[k]==best:
            words.append(k)
    return (words,best)

    