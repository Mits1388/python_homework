# Написать программу, которая принимает текст и выводит два слова: наиболее
# часто встречающееся и самое длинное
from collections import *
import string

text = 'Specifying reasonable shipping and handling costs in your listing is essential for smart selling. ' \
       'eBay’s free Shipping Calculator provides real-time shipping costs to buyers all over the world, ' \
       'so you can increase your chances of success. ' \
       'Remember that a long wait can be both boring and frustrating for customers.'
for i in string.punctuation:
    if i in text:
        text = text.replace(i, '')
word_list = text.split(' ')
often_word, count = max(Counter(word_list).items(), key=lambda j: j[::-1])
long_word = max(word_list, key=len)
print(f'often word - {often_word}\nlong word - {long_word}')
