# coding=utf-8
# 递归

def get_fibonacci(n):
    # 斐波拉契数列
    if n <= 2:
        return 1
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def get_factorial(n):
    # 阶乘
    if n == 1:
        return 1
    return n * get_factorial(n - 1)


def get_power(x, n):
    # 幂
    if n == 0:
        return 1
    return x * get_power(x, n - 1)


def search_by_dichotomy(n, lower, upper):
    # 二分法
    medium = (lower + upper) // 2
    print medium
    if n > medium:
        search_by_dichotomy(n, medium, upper)
    elif n < medium:
        search_by_dichotomy(n, lower, medium)
    else:
        print "Aha, I find it"
        return


# while True:
#     num = input("Please enter a number: ")
#     if num <= 0:
#         print "You must enter a number which greater than zero"
#     else:
#         a = get_fibonacci(num)
#         b = get_factorial(num)
#         c = get_power(num, num)
#         print "fibonacci " + str(a) + "\nfactorial " + str(b) + "\npower " + str(c)
#         break
search_by_dichotomy(201, 1, 1000000)
