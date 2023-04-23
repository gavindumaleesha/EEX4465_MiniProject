from prettytable import PrettyTable
from algorithm import hashTable

# generate wordsHK6.txt file
table = PrettyTable()
table.columnName = ['Word index j', 'Word', 'Hash key, kj']

for row in hashTable:
    if row is not None:
        table.add_row([row[0], row[1], row[2]])

with open('wordsHK6.txt', 'w') as f:
    f.write(str(table))

print("wordsHK6 Table Generated Successfully!\n")    # Success Message - Task 1


# generate wordsQHK6.txt file
table = PrettyTable()
table.columnName = ['Word index j', 'Word', 'Hash key, kj', 'new Hash key, Qkj', 'Quadratic h-f, h(j, i)']

for row in hashTable:
    if row is not None:
        table.add_row([row[0], row[1], row[2], row[3], row[4]])

with open('wordsQHK6.txt', 'w') as outputFile:
    outputFile.write(str(table))

print("wordsQHK6 Table Generated Successfully!\n")    # Success Message - task 2


# generate hash table in hashTable.txt file
table = PrettyTable()
table.columnName = ['Index', ' Words in “file6.txt”']

for row in hashTable:
    if row is not None:
        table.add_row([row[4], row[1]])

with open('hashTable.txt', 'w') as outputFile:
    outputFile.write(str(table))

print("Hash Table Generated in hashTable.txt File Successfully!\n")   # Success Message - Task 3

print("Designed By - G.G.Maleesha | 621437488 | s92077488")
