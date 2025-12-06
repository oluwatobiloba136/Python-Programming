# # # print("Hello world")

# # productName = 'Computer'

# # fruits = ['banana', 'apple', 'orange']

# # fruits[1] = 'lemon'

# # print(fruits)

# # words = ["Python", "is", " Awesome"]
# # sentence = " ".join(words)

# # print(sentence)

# # # name = input("What is your name? ")
# # # age = input("What is your age? ")
# # # print("Hello, your name is " + name)

# # name =  "John"
# # age = 30
# # print("My name is {} and I am {} years old".format(name, age))
# # print(f"My name is {name} and I am {age} years old")

# # # LIST
# # my_list = [1,2,3, " apple", "banana",True]
# # print(my_list)
# # my_list.append("cherry")
# # print(my_list)
# # my_list.extend([4,5])
# # print(my_list)
# # my_list.insert(3, "grape")
# # print(my_list)
# # my_list.remove("banana")
# # print(my_list)
# # my_list.pop(3)
# # print(my_list)
# # del my_list[1]
# # print(my_list)
# # # pop , remove , del

# # # index 
# # print(my_list[-1])

# # sub_list =  my_list[2:5]
# # print(sub_list)
# # print(len(my_list))

# # print("apple" in my_list)


# # DICTIONARY
# my_dict = {"name": "Tobi", "age": 33, "city":"Calgary"}
# print(my_dict["age"])

# print(my_dict.get("city", "not found"))

# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# Tuple 
# fruits = ("apple", "banana", "orange", "berry")
# print(fruits[-1])

# print(fruits[1:])
# print(fruits[1:4])
# print(fruits[:3])

# tuple1 = (1,2,3)
# tuple2 = (4,5,6)
# combined_tuple = tuple1 + tuple2
# print(combined_tuple)

# repeated = (1,2) * 3
# print(repeated)

# words = ("hello", "world", )

# numbers  = (1,2,3,3,5)
# print(max(numbers))
# print(sum(numbers))

# SET

# my_set = {1,2,3, "apple", "banana", False}
# print(my_set)

# dup_list = [1,3,5,4,4,6,3,1,1]
# another_set = set(dup_list)
# my_set.add("orange")
# my_set.remove(False)
# print(my_set)
# my_set.discard("apple")
# print(my_set)

# # union 
# set1 = {1,2,3}
# set2 = {3,4,5}
# union_set = set1.union(set2)
# union_set = set1 | set2
# print(union_set)

# # intersection 
# intersection_set =  set1.intersection(set2) 
# intersection_set =  set1 & set2 
# print(intersection_set)

# # difference
# difference_set = set1.difference(set2)
# difference_set =  set1 - set2
# print(difference_set)


# if, elif, else 
# age = 18 
# if age < 18:
#     print("You are a minor")
# elif age == 18:
#     print("You just become an adult")
# else:
#     print("You are an adult")

# for loop
# for number in range(1, 6):
#     print(number)


# my_dict = {"name": "Tobi", "age": 33, "city":"Calgary"}
# for key in my_dict:
#     print(key)

# for key, val in my_dict.items():
#     print(key, val)


# while loop 

# count = 1 
# while count <=5:
#     print(count)
#     count = count +1

# nested for loop  
# for i in range(1,5):  #outer loop
#     for j in range(1,5):
#         print (f"{i} x {j}  = {i*j}")

# Break , continue , pass 


# funtions 
# parameter-- argument -- return values

# Lambda function  
# lambda parameters : expression  

# double =  lambda x:x*2
# print(double(5))

# map function 
# map (function, iterable)
# numb = [1,2,3,4]

# doubled = map(lambda x:x*2, numb)
# print(list(doubled))

# File Handling
# file = open("filename", "mode")

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open('example.txt', 'w')
# file.write("This is a line from program")
# file.close()


# try:
#     file = open('example.txt', 'x')
#     file.write("This will only write if the file does not exist")
#     file.close()
# except FileExistsError:
#     print("File already exists")


