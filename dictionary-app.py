from Levenshtein import distance as levenshtein_distance

def readDictionary():
    lines = []
    with open('dictionary.txt', 'r', encoding='UTF8') as f:
        lines = f.readlines()

    data = []
    words = []
    for line in lines:
        x = line.split()
        if len(x) > 1 :
            words.append(x[0].lower())
            data.append(line)
    return (words, data)

def createBuckets(words):
    buckets = []
    for i in range(30):
        buckets.append([])

    for word in words :
        cleanWord = word.replace('-', '')
        buckets[len(cleanWord)].append(cleanWord)

    return buckets

def searchWords(words, searchWord):
    wordCount = len(words)
    index = int(wordCount / 2)
    lower = 0
    upper = wordCount - 1
    while index <= upper and index >= lower :
##        print(str(index) + ' ' + words[index])
        dictionaryWord = words[index].replace('-', '')
            
        if searchWord == dictionaryWord :
            return index
        elif searchWord > dictionaryWord :
            lower = index + 1
            index = int((lower + upper) / 2)
        elif searchWord < dictionaryWord :
            upper = index - 1
            index = int((lower + upper) / 2)

##    Alternative method but not very effective...
##    print("Word not found in dictionary. Did you mean? ")
##
##    if lower - 1 < 0 :
##        lower = 0
##    else :
##        lower = lower - 1
##    if upper + 2 > wordCount :
##        upper = wordCount
##    else:
##        upper = upper + 2
##        
##    for i in range(lower, upper):
##        print(words[i])
    return -1



def findNearest(buckets, searchWord):
    suggestions = {}
    for bucket in buckets :
        for word in bucket:
            levDistance = levenshtein_distance(word, searchWord)
            if levDistance <= 4 :
                if levDistance in suggestions :
                    suggestions[levDistance].append(word)
                else :
                    suggestions[levDistance] = [word]
            
    return suggestions

def main():
    (words, data) = readDictionary()
    buckets = createBuckets(words)
    print('Enter the word you want to search: ')
    searchWord = input().replace('-', '')
    wordIndex = searchWords(words, searchWord.lower())
    if wordIndex > -1 :
        print(data[wordIndex])
    else :
        print("Word not found in dictionary. Did you mean? ")        
        suggestions = findNearest(buckets, searchWord)

    totalSuggestions = 0
    for i in range(5) :
        if i in suggestions:            
            for suggestion in suggestions[i]:
                print(suggestion)
                totalSuggestions += 1
                if totalSuggestions > 3 :
                    break

if __name__ == '__main__' :
    main()
