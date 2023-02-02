#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name_user = input("Enter name: ")
age_user = input("Enter age: ")
city_user = input("Enter city: ")

print(f"Today you are {age_user} years old! Welcome to {city_user}, {name_user}.")
print("Today you are {} years old! Welcome to {}, {}.".format(age_user,city_user,name_user))
print("Today you are %(age)d years old! Welcome to %(city)s, %(name)s." % {"name":name_user, "age":int(age_user), "city":city_user})