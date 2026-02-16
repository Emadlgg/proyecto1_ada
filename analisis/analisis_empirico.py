import time
import matplotlib.pyplot as plt
import numpy as np
from src.maquina_turing import MaquinaTuring


def numero_a_unario(n):
    """Convierte un número a representación unaria."""
    if n <= 0:
        return '_'
    return '1' * n


def medir_tiempo_ejecucion(n):
    """
    Mide el tiempo de ejecución para calcular F(n).
    
    Args:
        n (int): Índice de Fibonacci
    
    Returns:
        tuple: (tiempo_ejecucion, numero_pasos)
    """
    entrada = numero_a_unario(n)
    
    # Ejecutar múltiples veces para obtener tiempos medibles
    repeticiones = 100  # Ejecutar 100 veces para promediar
    
    tiempo_inicio = time.perf_counter()  # Usar perf_counter para mayor precisión
    for _ in range(repeticiones):
        maquina_temp = MaquinaTuring('config/maquina_fibonacci.json')
        maquina_temp.inicializar(entrada)
        maquina_temp.ejecutar(max_pasos=1000, mostrar_pasos=False)
    tiempo_fin = time.perf_counter()
    
    tiempo_promedio = (tiempo_fin - tiempo_inicio) / repeticiones
    
    # Obtener número de pasos de una ejecución
    maquina = MaquinaTuring('config/maquina_fibonacci.json')
    maquina.inicializar(entrada)
    maquina.ejecutar(max_pasos=1000, mostrar_pasos=False)
    
    return tiempo_promedio, maquina.pasos


def analisis_empirico():
    """
    Realiza un análisis empírico de los tiempos de ejecución.
    """
    print("="*60)
    print("ANÁLISIS EMPÍRICO - MÁQUINA DE TURING FIBONACCI")
    print("="*60)
    
    # Valores de n a probar
    valores_n = [0, 1, 2, 3, 4, 5]
    tiempos = []
    pasos_lista = []
    
    print("\nEjecutando pruebas (100 repeticiones por valor para mayor precisión)...")
    print(f"{'n':<5} {'F(n)':<10} {'Pasos':<10} {'Tiempo promedio (ms)':<20}")
    print("-"*60)
    
    for n in valores_n:
        tiempo, pasos = medir_tiempo_ejecucion(n)
        tiempos.append(tiempo * 1000)  # Convertir a milisegundos
        pasos_lista.append(pasos)
        
        # Calcular F(n) para referencia
        if n <= 0:
            fib = 0
        elif n == 1:
            fib = 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            fib = b
        
        print(f"{n:<5} {fib:<10} {pasos:<10} {tiempo*1000:<20.6f}")
    
    # Crear gráficas
    crear_graficas(valores_n, tiempos, pasos_lista)
    
    # Regresión polinomial
    realizar_regresion(valores_n, tiempos)


def crear_graficas(valores_n, tiempos, pasos):
    """
    Crea gráficas de dispersión para visualizar los resultados.
    
    Args:
        valores_n (list): Lista de valores de n
        tiempos (list): Lista de tiempos de ejecución en milisegundos
        pasos (list): Lista de número de pasos
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfica 1: Tiempo vs Tamaño de entrada
    ax1.scatter(valores_n, tiempos, color='blue', s=100, alpha=0.6, edgecolors='black')
    ax1.plot(valores_n, tiempos, color='lightblue', linestyle='--', alpha=0.5)
    ax1.set_xlabel('Tamaño de entrada (n)', fontsize=12)
    ax1.set_ylabel('Tiempo de ejecución (milisegundos)', fontsize=12)
    ax1.set_title('Tiempo de Ejecución vs Tamaño de Entrada', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Pasos vs Tamaño de entrada
    ax2.scatter(valores_n, pasos, color='green', s=100, alpha=0.6, edgecolors='black')
    ax2.plot(valores_n, pasos, color='lightgreen', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Tamaño de entrada (n)', fontsize=12)
    ax2.set_ylabel('Número de pasos', fontsize=12)
    ax2.set_title('Número de Pasos vs Tamaño de Entrada', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analisis/grafica_dispersion.png', dpi=300, bbox_inches='tight')
    print("\n✅ Gráfica guardada en: analisis/grafica_dispersion.png")
    plt.show()


def realizar_regresion(valores_n, tiempos):
    """
    Realiza regresión polinomial sobre los datos.
    
    Args:
        valores_n (list): Lista de valores de n
        tiempos (list): Lista de tiempos de ejecución en milisegundos
    """
    print("\n" + "="*60)
    print("REGRESIÓN POLINOMIAL")
    print("="*60)
    
    # Probar diferentes grados de polinomios
    grados = [1, 2, 3]
    
    for grado in grados:
        coeficientes = np.polyfit(valores_n, tiempos, grado)
        polinomio = np.poly1d(coeficientes)
        
        # Calcular R²
        y_pred = polinomio(valores_n)
        ss_res = np.sum((np.array(tiempos) - y_pred) ** 2)
        ss_tot = np.sum((np.array(tiempos) - np.mean(tiempos)) ** 2)
        
        # Evitar división por cero
        if ss_tot != 0:
            r_cuadrado = 1 - (ss_res / ss_tot)
        else:
            r_cuadrado = 0
        
        print(f"\nGrado {grado}:")
        print(f"  Ecuación: {polinomio}")
        print(f"  R² = {r_cuadrado:.6f}")
    
    # Graficar mejor ajuste
    mejor_grado = 2
    coeficientes = np.polyfit(valores_n, tiempos, mejor_grado)
    polinomio = np.poly1d(coeficientes)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(valores_n, tiempos, color='blue', s=100, alpha=0.6, edgecolors='black', label='Datos observados')
    
    x_continuo = np.linspace(min(valores_n), max(valores_n), 100)
    y_continuo = polinomio(x_continuo)
    plt.plot(x_continuo, y_continuo, color='red', linewidth=2, label=f'Ajuste polinomial (grado {mejor_grado})')
    
    plt.xlabel('Tamaño de entrada (n)', fontsize=12)
    plt.ylabel('Tiempo de ejecución (milisegundos)', fontsize=12)
    plt.title('Regresión Polinomial del Tiempo de Ejecución', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    plt.savefig('analisis/regresion_polinomial.png', dpi=300, bbox_inches='tight')
    print("\n✅ Gráfica de regresión guardada en: analisis/regresion_polinomial.png")
    plt.show()


if __name__ == "__main__":
    analisis_empirico()