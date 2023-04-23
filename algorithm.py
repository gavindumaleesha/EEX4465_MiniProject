import re

# simple and capital English characters
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#  map letters with relevant numbers
letter_to_number = dict(zip(list(alphabet), [str(i) for i in range(0, 51)]))

# reads the text from a file 6 and removes all non-alphabetic characters
with open('file6.txt', 'r') as inputFile:
    inputText = re.sub(r'[^a-zA-Z\s]', '', inputFile.read())


wordIndex = 1                       # set word index (j) as 1
word = ''                           # set word as string
hashKey = 0                         # set hash key (Kj) as 0
tableSize = 157                     # set size of hash table
hashTable = [None] * tableSize      # create empty hash table

# create a empty set to store unique words
uniqueWords = set()

# loop through unique words
for i in range(len(inputText)):

    # if current character is a letter, add its value to current word sum
    if inputText[i] in alphabet:
        hashKey += int(letter_to_number[inputText[i]])
        word += inputText[i]

    # if current character is a space, compute key, new key, and hash value for current word
    elif inputText[i] == ' ':

        # new hash key =  Kj + c1*(i**2) + c2*i + c3
        # Kj = hashKey from wordsHK6 table
        # c1 = c2 = c = 1,  c3 = 0
        key = hashKey
        c = 1
        i = wordIndex

        # formula for new hash key
        newHashKey = key + c * (i ** 2) + c * i + 0
        quadraticHF = newHashKey % tableSize

        # quadratic probing to resolve collisions
        while hashTable[quadraticHF] is not None and hashTable[quadraticHF][2] != key:
            c += 1
            i += 1
            quadraticHF = (newHashKey + c * (i ** 2) + c * i) % tableSize

        # add current word to hash table if it's unique
        if word not in uniqueWords:
            uniqueWords.add(word)
            hashTable[quadraticHF] = (wordIndex, word, hashKey, newHashKey, quadraticHF)

        # reset variables for processing next word
        hashKey = 0
        word = ''
        wordIndex += 1
    # if current character is not a letter or space, add it to current word without processing
    else:
        word += inputText[i]

# add last word to hash table if it's unique
if word not in uniqueWords:
    uniqueWords.add(word)
    key = hashKey
    c = 1
    i = wordIndex
    newHashKey = key + c * (i ** 2) + c * i
    quadraticHF = newHashKey % tableSize
    while hashTable[quadraticHF] is not None and hashTable[quadraticHF][2] != key:
        c += 1
        i += 1
        quadraticHF = (newHashKey + c * (i ** 2) + c * i) % tableSize
    hashTable[quadraticHF] = (wordIndex, word, hashKey, newHashKey, quadraticHF)