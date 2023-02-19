# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

text = 'Hello world'
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
              '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}


def translation_morse(any_text):
    string = ''
    for i in text.upper():
        if i in morse_dict:
            string += morse_dict[i]
    return string


print(translation_morse(text))

# morse = []
# for i in text.upper().split(' '):
#     list_text = []
#     for j in i:
#         list_text.append(morse_dict[j])
#     morse.append(' '.join(list_text))
# print('    '.join(morse))
