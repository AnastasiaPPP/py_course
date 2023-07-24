# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)

text = """
        In most parts of the world, software is automatically covered by copyright.
        This means that other developers require explicit permission to copy, 
        use, modify and redistribute the software.
        Open source licensing is a way of explicitly granting such permission in a relatively consistent way,
        allowing developers to share and collaborate efficiently by making common sol utions
        to various problems freely available. This leaves many developers free to spend more time
        focusing on the problems that are relatively unique to their specific situation.
        The distribution tools provided with Python are designed to make it reasonably straightforward
        for developers to make their own contributions back to that common pool of software if they choose to do so.
        The same distribution tools can also be used to distribute software within an organisation,
        regardless of whether that software is published as open source software or not.
        """


text = text.translate(str.maketrans({'.': '', ',': ''})).lower().split()
print(f'Длина текста: {len(text)}  слов')
frequent_words = {x:text.count(x) for x in text}
words = []
frequence = []

for key, value in frequent_words.items():
    words.append(key)
    frequence.append(value)

frequent_words = {}

for _ in range(10):
    max_frequence_index = frequence.index(max(frequence))
    frequent_words[words[max_frequence_index]] = max(frequence)
    words.pop(max_frequence_index)
    frequence.pop(max_frequence_index)

print(f'10 самых часто встречающихся слов: ')
for key, value in frequent_words.items():
    print(f'{key}  частота повторений - {value}')

