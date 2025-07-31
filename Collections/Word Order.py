num_of_words = int(input())

word_count = {}
order_of_words = []

for i in range(num_of_words):
    word = input()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        order_of_words.append(word)

print(len(order_of_words))
print(' '.join(str(word_count[word]) for word in order_of_words))