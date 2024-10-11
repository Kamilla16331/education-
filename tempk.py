# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

# Пример задания из изображения (вариант 1):
A = np.array([[3, -7, 2], [-3, 4, 1], [2, 3, -1]])
B = np.array([[1, -7], [0, 3], [-1, 4]])
C = np.array([[1, -1, 4], [0, 1, 3]])
D = np.array([[3, 1, 4], [0, 3, 5]])

# a) Найдем матрицы 2C + 5D и C - 3D
result_1 = 2 * C + 5 * D
result_2 = C - 3 * D

print("2C + 5D =\n", result_1)
print("C - 3D =\n", result_2)

# б) Найдем транспонированную матрицу B^T
B_transposed = B.T
print("Транспонированная матрица B^T =\n", B_transposed)

# Проверим возможность умножения AB и BC
# AB возможно, если количество столбцов в A равно количеству строк в B
if A.shape[1] == B.shape[0]:
    AB = np.dot(A, B)
    print("AB =\n", AB)
else:
    print("Умножение A на B невозможно")

# BC возможно, если количество столбцов в B равно количеству строк в C
if B.shape[1] == C.shape[0]:
    BC = np.dot(B, C)
    print("BC =\n", BC)
else:
    print("Умножение B на C невозможно")

# в) Найдем обратную матрицу A^-1, если она существует
try:
    A_inv = np.linalg.inv(A)
    print("Обратная матрица A^-1 =\n", A_inv)
except np.linalg.LinAlgError:
    print("Матрица A необратима")
