class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as opened_file:
                words = []
                for line in opened_file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for i in punctuation:
                        line = line.replace(i, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        place = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                place[key] = value.index(word.lower()) + 1

        return place

    def count(self, word):
        amount = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            amount[value] = words_count

        return amount


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
