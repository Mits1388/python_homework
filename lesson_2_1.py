#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
print("Method first")
first_text = input("Enter text: ")
print(first_text.replace(" ", "-"))
print("Method second")
second_text = input("Enter text: ")
text_start = second_text.split(' ')
text_end = "-".join(text_start)
print(text_end)