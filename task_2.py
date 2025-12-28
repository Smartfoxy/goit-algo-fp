import math
import matplotlib.pyplot as plt

def pifagor_tree(n):
    angle = math.pi / 2
    length_factor = 0.7
    angle_factor =  math.pi / 4

    plt.figure(figsize=(6, 6))
    plt.axis("off")
    
    line(0, 0, angle, 1, length_factor, angle_factor, int(n))
    
    plt.axis("equal")
    plt.show()


def line(x0 , y0, angle, length, length_factor, angle_factor, n):
    x1 = x0 + length * math.cos(angle)
    y1 = y0 + length * math.sin(angle)
    x = [x0, x1]
    y = [y0, y1]

    plt.plot(x, y)
    n -= 1
    if n > 0:
        line(x1, y1, angle + angle_factor, length * length_factor, length_factor, angle_factor, n)
        line(x1, y1, angle - angle_factor, length * length_factor, length_factor, angle_factor, n)



n = input("Set Pifagor tree level:")
pifagor_tree(n)