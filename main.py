import text_analyser

stats = text_analyser.TextAnalyser()

while True:
    print("Type the text:")
    text = input()
    if stats.get_text(text):
        break

stats.words_counter()
stats.avarage()

while True:
    print("Write k:")
    K = input()
    
    if (K == ''):
        k = 10
        break
    else:
        try:
            k = int(K)
        except ValueError:
            print("Try again")
        else:
            break

while True:
    print("Write n:")
    N = input()
    
    if (N == ''):
        n = 4
        break
    else:
        try:
            n = int(N)
        except ValueError:
            print("Try again")
        else:
            break

stats.get_n_grams(n, k)
