# Определим слова в хэштеге. Дана строка, начинается с # и содержит набор слов соединенных в одну строку без пробелов.
# Срока описана в стиле camelCase, то есть первое слово начинается с прописной буквы, а каждое следующее с заглавной.
# Например: #приветКакДела, #меняЗовутЕгорМнеМногоЛет и тд.
# Необходимо посчитать количество слов в строке и вывести количество этих слов.

s: str = input('Input line: ')

#nefig mne tut neskol'ko hashtagov pisat'
s = s[0:s.find(' ')]

counter: int = 0
if s[1].islower() and s[0] == "#":
    counter += 1
    for ch in s:
        if ch.isupper():
            counter += 1

print('Number of words in correct hashtag: ', counter)