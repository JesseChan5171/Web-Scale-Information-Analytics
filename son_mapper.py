#!/usr/bin/env python

import sys



lines = []
count = 0
threshold = 0.005

freq_word = dict()
for line in sys.stdin:
    words = line.strip().split()
    set_words = list(set(words))
    for i in set_words:
        if i in freq_word:
            freq_word[i] += 1
        else:
            freq_word[i] = 1
    count += 1
    lines.append(line.strip())

freq_word = {key: value for key, value in freq_word.items() if value >= count * threshold}
#print(freq_word)

freq_pair = dict()
for i in range(0, len(lines)):
    line = lines[i]
    words = line.strip().split()
    set_words = list(set(words))
    words = []
    for j in range(0, len(set_words) - 1):
        for k in range(j + 1, len(set_words)):
            if set_words[j] in freq_word:
                if set_words[k] in freq_word:
                    if set_words[j] <= set_words[k]:
                        pair = set_words[j] + "," + set_words[k]
                    else:
                        pair = set_words[k] + "," + set_words[j]
                    if pair not in freq_pair:
                        freq_pair[pair] = 1
                    else:
                        freq_pair[pair] += 1

for i in freq_pair:
    if freq_pair[i] >= count * threshold:
        print('%s\t%s' % (i, freq_pair[i]))

