import numpy as np

# Solución por Regla de Cramer
def determinante(matriz):
    return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

def solve_system(matriz, resultados):
    det_A = determinante(matriz)
    det_X = determinante([[resultados[0], matriz[0][1]],
                        [resultados[1], matriz[1][1]]])
    det_Y = determinante([[matriz[0][0], resultados[0]],
                        [matriz[1][0], resultados[1]]])
    x = det_X/det_A
    y = det_Y/det_A
    return x, y

matriz = [[1, 3],
          [1.5, 2]]
resultados = [300, 350]

x1, y1 = solve_system(matriz, resultados)
print("Solución por Regla de Cramer")
print("x1 =", x1)
print("y1 =", y1)

# Solución con Numpy
A = np.array([[1, 3],
              [1.5, 2]])
b = np.array([300, 350])

x2, y2 = np.linalg.solve(A, b)

print("Solución con Numpy")
print("x2 =", x2)
print("y2 =", y2)
