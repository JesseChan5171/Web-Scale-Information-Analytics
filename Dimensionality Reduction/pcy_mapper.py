#!/usr/bin/env python

import sys

lines = []
count = 0
threshold = 0.005
sigleton_list = [0] * 100000
doubleton_list = [0] * 100000

freq_word = dict()
for line in sys.stdin:
    words = line.strip().split()
    set_words = list(set(words))

    for i in set_words:
        hash_val = hash(i) % 100000
        if sigleton_list[hash_val] > 0:
            sigleton_list[hash_val] += 1
        else:
            sigleton_list[hash_val] = 1
    count += 1
    lines.append(line.strip())

# freq_word = {key: value for key, value in freq_word.items() if value >= count * threshold}
# filtered_sigleton = [number for number in sigleton_list if number >= count * threshold]

# print(freq_word)

#freq_pair = []
for i in range(0, len(lines)):
    line = lines[i]
    words = line.strip().split()
    set_words = list(set(words))
    words = []
    for j in range(0, len(set_words) - 1):
        for k in range(j + 1, len(set_words)):
            hash_val_j = hash(j) % 100000
            hash_val_k = hash(k) % 100000
            if (sigleton_list[hash_val_j] > 0):
                if (sigleton_list[hash_val_k] > 0):
                    if (set_words[j] <= set_words[k]):
                        pair = set_words[j] + "," + set_words[k]
                        h_pair = set_words[j] + set_words[k]
                    else:
                        pair = set_words[k] + "," + set_words[j]
                        h_pair = set_words[k] + set_words[j]
                    hash_val_pair = hash(h_pair) % 100000
                    if hash_val_pair > 0:
                        doubleton_list[hash_val_pair] += 1
                        #freq_pair.append(pair)
                        # freq_pair[pair] = 1
                    else:
                        doubleton_list[hash_val_pair] = 1
                        #freq_pair.append(pair)
                        # freq_pair[pair] += 1

# filtered_dounleton = [number for number in doubleton_list if number >= count * threshold]

# for (i, item) in enumerate(doubleton_list, start=1):
#     print('%s\t%s' % (i, item))

# for i in freq_pair:
#     h_i = i.replace(',', '+')
#     hashv_i = hash(h_i) % 100000
#     if doubleton_list[hashv_i] >= count * threshold:
#         print('%s\t%s' % (i, doubleton_list[hashv_i]))

for i in range(0, len(lines)):
    line = lines[i]
    words = line.strip().split()
    set_words = list(set(words))
    words = []
    for j in range(0, len(set_words) - 1):
        for k in range(j + 1, len(set_words)):
            hash_val_j = hash(j) % 100000
            hash_val_k = hash(k) % 100000
            if (sigleton_list[hash_val_j] > 0):
                if (sigleton_list[hash_val_k] > 0):
                    if (set_words[j] <= set_words[k]):
                        pair = set_words[j] + "," + set_words[k]
                        h_pair = set_words[j] + set_words[k]
                    else:
                        pair = set_words[k] + "," + set_words[j]
                        h_pair = set_words[k] + set_words[j]
                    hash_val_pair = hash(h_pair) % 100000
                    if doubleton_list[hash_val_pair] >= threshold * count:
                        print('%s\t%s' % (pair, doubleton_list[hash_val_pair]))





