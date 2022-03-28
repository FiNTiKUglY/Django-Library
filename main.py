import text_analyser

stats = text_analyser.TextAnalyser()

while True:
    print("Type the text:")
    text = input()
    if stats.get_text(text):
        break
    print("No punctuation mark in the end, try again")

words_list = stats.words_counter()

for key, value in words_list.items():
    print("{0}: {1}".format(key, str(value)))

median, average = stats.avarage()
print("Average count of words in sentence:", average)
print("Median count of words in sentence:", median)

while True:
    print("Write k:")
    K = input()
    
    if (K == ''):
        k = 10
        break
    else:
        try:
            k = int(K)
            break
        except ValueError:
            print("Try again")

while True:
    print("Write n:")
    N = input()
    
    if (N == ''):
        n = 4
        break
    else:
        try:
            n = int(N)
            break
        except ValueError:
            print("Try again")


n_grams = stats.get_n_grams(n, k)
i = 1
for key, value in n_grams.items():
    print("{0}: {1}".format(key, str(value)))

    if i == k:
        break
    else:
        i += 1
