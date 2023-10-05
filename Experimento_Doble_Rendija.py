# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to y 5to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Nicola Calderón, Jesús Pinzón, Juan Vera
# Fecha: 2023/10/05

# Programa de Simulación del Experimento de la Doble Rendija

from Libreria_Simulacion_Clasico_Cuantico import *

# Definimos el número de rendijas como n=2 y la matriz de relaciones como M para "disparar 1000 fotones" 
n = 2
M = [[0,0,0,0,0,0,0,0], [1/sqrt(2),0,0,0,0,0,0,0], [1/sqrt(2),0,0,0,0,0,0,0],\
    [0,(-1+1j)/sqrt(6),0,1,0,0,0,0], [0,(-1-1j)/sqrt(6),0,0,1,0,0,0], [0,(1-1j)/sqrt(6),(-1+1j)/sqrt(6),0,0,1,0,0],\
    [0,0,(-1-1j)/sqrt(6),0,0,0,1,0], [0,0,(1-1j)/sqrt(6),0,0,0,0,1]]
m = M

# La librería nos retorna la matriz m² y el vector de estados final
m2,xf = Sim_Exp_Ren_Part_Cuan(n,m)

# Procedemos a graficar los resultados probabilísticos del experimento
x = list(range(8))
y = [0]*8

for k in range(len(xf)):
    y[k] = linalg.norm(xf[k])
    
print(f"Eje x: {x}")
print(f"Eje y: {y}")
    
Graf_Exp(x,y)


# Nodos = [0, 1, 2, 3, 4, 5, 6, 7]
# Estado_Final = [0.0, 0.0, 0.0, 408.24829046386304, 408.24829046386304,\
#    3.466841006892044e-14, 408.24829046386304, 408.24829046386304]