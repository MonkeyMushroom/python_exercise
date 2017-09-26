import os

file_list = os.listdir(r"C:\Users\Administrator\Desktop\3.50")
print(file_list)

current_path = os.getcwd()
os.chdir(r"C:\Users\Administrator\Desktop\3.50")

for file_name in file_list:
    if file_name.__contains__("com.jyd.jyddz.encrypted.UMENG_CHANNEL.channel")\
            and file_name.__contains__("_signed_Aligned"):
        new_name = file_name.replace("com.jyd.jyddz.encrypted.UMENG_CHANNEL.channel", "jyddz") \
            .replace("_signed_Aligned", "")
        print(file_name + " -> " + new_name)
        if new_name not in file_list:
            os.rename(file_name, new_name)

os.chdir(current_path)
