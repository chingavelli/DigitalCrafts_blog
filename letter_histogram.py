#letter_histogram('banana')
{'a': 3, 'b': 1, 'n': 2}

def letter_histogram(word):
    tally = {}
    for char in word:
        if tally.get(char):
            tally[char] += 1
        else:
            tally[char] = 1    
    print tally            

letter_histogram('banana')           