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

        if not self.text.endswith(values.end):
            return False
        else:
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

        return word_stat

    def get_sentences(self):
        i = 1

        for k in range(len(self.word_list_with_signs)):
            if any(word in values.end for word in self.word_list_with_signs[k]):

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

            if text_len % 2 == 1:
                median = self.sentences[(text_len - 1) // 2 + 1]
            else:
                median = (self.sentences[(text_len - 1) // 2] + self.sentences[(text_len - 1) // 2 + 1]) / 2

        else:
            median = average = self.sentences[0]

        return median, average

    def get_n_grams(self, n, k):
        n_grams_stat = {}

        for elem in self.word_list:
            if len(elem) < n:
                continue
            else:

                for i in range(len(elem)):
                    if (i + n) <= len(elem):
                        word = elem[i:i+n]
                        if word in n_grams_stat:
                            n_grams_stat[word] += 1
                        else:
                            n_grams_stat[word] = 1
                    else:
                        break

        sorted_n_grams = {key: value for key, value in
                          sorted(n_grams_stat.items(), key=lambda item: item[1], reverse=True)}
        return sorted_n_grams
