# coding=utf-8
from matplotlib import pyplot


def draw_line(x_values, y_values):
    """折线图"""
    pyplot.plot(x_values, y_values, linewidth=5)  # 指定线宽
    pyplot.title("Line Numbers", fontsize=24)  # 设置标题
    pyplot.xlabel("Values", fontsize=14)  # x轴标签
    pyplot.ylabel("Line of Values", fontsize=14)  # y轴标签
    pyplot.tick_params(axis="both", labelsize=14)  # 刻度大小
    pyplot.show()


x_values = list(range(0, 1000))
y_values = [x ** 2 for x in x_values]


# draw_line(x_values, y_values)


def draw_scatter(x_values, y_values):
    """散点图"""
    # 横坐标，纵坐标， 点的颜色(也可以使用rgb，如(0,0,255))， 点的大小，轮廓颜色
    # pyplot.scatter(x_values, y_values, c="red", s=10, edgecolors=None)
    pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, s=10, edgecolors=None)
    pyplot.title("Scatter Numbers", fontsize=24)
    pyplot.xlabel("Value", fontsize=14)
    pyplot.ylabel("Scatter of Value", fontsize=14)
    # 指定了每个坐标轴的取值范围，函数axis() 要求提供四个值：x 和 y 坐标轴的最小值和最大值。
    # pyplot.axis([0, 100, 0, 10000])
    pyplot.tick_params(axis="both", which='major', labelsize=14)
    pyplot.show()


draw_scatter(x_values, y_values)
