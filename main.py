# Практическое задание по теме: "Словари и множества"

# Работа со словарями:
my_dict ={'Yan' : 1977 ,'Bob' : 2004 , 'Katya' : 1998 , 'Alekc' : 1987}
print(my_dict)
print(my_dict ['Bob'])
my_dict ['Vitali' ] = 1971
print(my_dict.get('Nata'))
my_dict.update({'Noy': 2002,'Zoya': 1989,})
del my_dict['Yan']
print(my_dict.values())
# print(my_dict)
key_to_delete = 'Bob'
# Удаляем пару с выбранным ключом из словаря и сохраняем значение
deleted_value = my_dict.pop(key_to_delete)
# Выводим удаленное значение на экран
print("Удаленное значение:", deleted_value)
print(my_dict)

#  Работа с множествами:
my_set = {1,2,3,4,'Bob',4,55,"Vitali",True,2}
print(my_set)
element_to_add ={8,"Sonya", 6}
my_set.update(element_to_add)
my_set.discard(3)
print(my_set)