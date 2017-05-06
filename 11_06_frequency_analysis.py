from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# that is develpes solution and this is community solution
# d = {}
# for i in range(int(input())):
#     for word in input().split():
#         d[word] = d.get(word, 0) + 1 
  
# for i in sorted(d.items(), key=lambda x:(-x[1],x[0])): 
#     print(i[0])

#and this is my (not finished) solution
# counter = {}
# for i in range(int(input())):
#     line = input().split()
#     for word in line:
#         counter[word] = counter.get(word, 0) + 1

# a = []
# for key, value in sorted(counter.items()):
#     temp = [value, key]
#     a.append(temp)
# for word in sorted(a, reverse=True):
#     print(word[1])