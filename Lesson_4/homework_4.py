adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)



# task 02 ==
""" Замініть .... на пробіл
"""
print()
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print()
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print()
text = adwentures_of_tom_sawer.count("h")
print(text)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

count = (sum(word.istitle() for word in adwentures_of_tom_sawer.split()))
print(count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
word_Tom = adwentures_of_tom_sawer.find ("Tom")
print (word_Tom)
word_Tom2 = adwentures_of_tom_sawer.find ("Tom", word_Tom+1)
print(word_Tom2)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.

"""
sentence_4 = adwentures_of_tom_sawer_sentences[3].lower()
print()
print(sentence_4)

sentence_5 = adwentures_of_tom_sawer_sentences[4].lower()
print(f'\n"{sentence_5}"')


adwentures_of_tom_sawer_sentences1 = ". ".join(adwentures_of_tom_sawer_sentences)
sentence_4 = adwentures_of_tom_sawer_sentences1[3].lower()
print(sentence_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print()
# adwentures_of_tom_sawer_sentences = ". ".join(adwentures_of_tom_sawer_sentences)

print("By the time" in adwentures_of_tom_sawer_sentences)
print(adwentures_of_tom_sawer_sentences)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

sentence_last = sentence_5
words_in_last_sentence = sentence_last.split()
words_in_sentence_last = len(words_in_last_sentence)
print("Answer: the number of words in the last sentence:", words_in_sentence_last)
