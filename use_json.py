# coding=utf-8
import json

numbers = [1, 3, 4, 5, 6, 7, 9]
with open("C:\Users\Administrator\Desktop\exc1.txt", "w") as file_obj:
    json.dump(numbers, file_obj)

with open("C:\Users\Administrator\Desktop\exc1.txt") as file_obj:
    number = json.load(file_obj)
    print number
