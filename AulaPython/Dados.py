import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlc

# inteiro = 87
# real = np.pi
# texto1 = '99'
# texto2 = 'Gatos Fofos'
# print(type(inteiro), type(real), type(texto1), type(texto2))
# print(inteiro, real, texto1, texto2)

# cores = 'rgcbmyk'
# label = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']

# n = int(input('Entre com um número inteiro: '))
# cor = n % len(cores)

# x = 200 + np.random.randn(100)
# plt.plot(x, color=cores[cor])

# plt.title(label[cor].upper(),fontsize=14)
# plt.show()

a = 28
b = 43

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")