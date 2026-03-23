import random
import numpy as np 

def funcion_objetivo(x, y):
    return 20 + x**2 + y**2 - 10*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y)) 

def crear_poblacion(tamano):
    return [(random.uniform(-3, 7), random.uniform(-3, 7)) for _ in range(tamano)]

def evaluar_poblacion(poblacion):
    return [funcion_objetivo(ind[0], ind[1]) for ind in poblacion]

def seleccion_ruleta(poblacion, valores_objetivo):
    pesos = [1.0 / (v + 1e-6) for v in valores_objetivo]
    return random.choices(poblacion, weights=pesos, k=2)

def seleccion_tournament(n, poblacion):
    padres= []
    for i in range (2):
        pos_padres = random.choices(poblacion, weights=None, k=n)
        menor= funcion_objetivo (pos_padres [0][0], pos_padres [0][1])
        padre = pos_padres [0][0], pos_padres [0][1]
        for i in range(1,n):
            if funcion_objetivo (pos_padres [i][0], pos_padres [i][1]) < menor:
                menor = funcion_objetivo (pos_padres [i][0], pos_padres [i][1])
                padre = pos_padres [i][0], pos_padres [i][1]
        padres.append(padre)
    return padres

def cruzar(padre1, padre2, prob_cruce):
    if random.random() < prob_cruce:
        hijo_x = (padre1[0], padre2[1])
        if random.random() > 0.2:
            hijo_x = (padre1[0], padre2[0])

        hijo_y = (padre2[0], padre1[1])
        if random.random() > 0.2:
            hijo_y = (padre2[1], padre1[1])

        return (hijo_x, hijo_y)
    return (padre1, padre2)

def mutar(individuo, tasa_mutacion=0.1):
    ind_nuevo=individuo
    if random.random() < tasa_mutacion:
        if random.random() <0.2: 
            ind_nuevo= (individuo[0], random.uniform(-3, 7))
        if random.random()<0.2:
            ind_nuevo = (random.uniform(-3, 7), ind_nuevo[1])
    return ind_nuevo

# Parametros
tamano_poblacion = 50
generaciones = 1000
poblacion = crear_poblacion(tamano_poblacion)

for gen in range(generaciones):
    valores_objetivo = evaluar_poblacion(poblacion)
    
    mejor_valor = min(valores_objetivo)
    if gen % 10 == 0:
        print(f"Gen {gen}: Mejor = {mejor_valor:.4f}")

    nueva_poblacion = []
    for _ in range(tamano_poblacion):
        #padre1, padre2 = seleccion_ruleta(poblacion, valores_objetivo)
        padre1, padre2 = seleccion_tournament(6, poblacion)
        
        hijo = cruzar(padre1, padre2)
        hijo_mutado = mutar(hijo,0.1)
        nueva_poblacion.append(hijo_mutado)

    poblacion = nueva_poblacion

# Resultado
valores_finales = evaluar_poblacion(poblacion)
mejor_ind = poblacion[np.argmin(valores_finales)]
print(f"\n--- Final ---")
print(f"Mejor individuo: {mejor_ind}")
print(f"Resultado: {min(valores_finales):.6f}")