# coding=utf-8

def count_words(file_name):
    try:
        with open(file_name) as file_obj:
            content = file_obj.read()
    except Exception:
        print("File Not Found")
    else:
        words = content.split()
        print("The file has " + str(len(words)) + " words.")
        print(str(content.count("Alice")))


file_name = r"C:\Users\Administrator\Desktop\AliceInWonderland.txt"
count_words(file_name)
