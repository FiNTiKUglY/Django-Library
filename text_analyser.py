import re
import values


class TextAnalyser:

    def __init__(self):
        self.text = ''
        self.word_list = []
        self.word_list_with_signs = []
        self.sentences = []

    def get_text(self, input_text):
        self.text = input_text

        if not self.text.endswith(values.ends):
            print("No punctuation mark in the end, try again")
            return False

        return True

    def words_counter(self):
        self.word_list_with_signs = self.text.split()
        word_stat = {}

        for elem in self.word_list_with_signs:
            self.word_list.append(re.sub(values.regulars, '', elem).lower())

        for i in range(len(self.word_list)):
            if self.word_list[i] in word_stat:
                word_stat[self.word_list[i]] += 1
            else:
                word_stat[self.word_list[i]] = 1

        for key, value in word_stat.items():
            print("{0}: {1}".format(key, str(value)))

    def get_sentences(self):
        i = 1

        for k in range(len(self.word_list_with_signs)):
            if any(word in values.ends for word in self.word_list_with_signs[k]):

                if self.word_list_with_signs[k] in values.specials:
                    i += 1
                    continue
                else:

                    if k == (len(self.word_list_with_signs) - 1):
                        self.sentences.append(i)
                        i = 1
                    elif (self.word_list_with_signs[k + 1])[0].isupper():
                        self.sentences.append(i)
                        i = 1
                    else:
                        i += 1

            else:
                i += 1

    def avarage(self):
        self.get_sentences()
        text_len = len(self.sentences)
        average = 0

        if text_len > 1:

            for elem in self.sentences:
                average += elem

            average /= text_len
            print("Average count of words in sentence:", average)

            if text_len % 2 == 1:
                median = self.sentences[(text_len - 1) // 2 + 1]
            else:
                median = (self.sentences[(text_len - 1) // 2] + self.sentences[(text_len - 1) // 2 + 1]) / 2

            print("Median count of words in sentence:", median)
        else:
            median = average = self.sentences[0]
            print("Average count of words in sentence:", average)
            print("Median count of words in sentence:", median)

    def get_n_grams(self, n, k):
        n_grams_stat = {}

        for elem in self.word_list:
            if len(elem) < n:
                continue
            else:

                for i in range(len(elem)):
                    if (i + n) <= len(elem):
                        word = ''
                        for j in range(i, i + n):
                            word += elem[j]
                        if word in n_grams_stat:
                            n_grams_stat[word] += 1
                        else:
                            n_grams_stat[word] = 1
                    else:
                        break

        sorted_n_grams = {key: value for key, value in
                          sorted(n_grams_stat.items(), key=lambda item: item[1], reverse=True)}
        i = 1

        for key, value in sorted_n_grams.items():
            print("{0}: {1}".format(key, str(value)))

            if i == k:
                break
            else:
                i += 1
