import time
from src.maquina_turing import MaquinaTuring
import os


# Función para verificar y generar diagramas automáticamente
def verificar_y_generar_diagramas():
    """Verifica si existen los diagramas, si no, los genera."""
    diagrama_estados = 'docs/diagrama_estados.png'
    tabla_transiciones = 'docs/tabla_transiciones.png'
    
    # Verificar si los diagramas ya existen
    if os.path.exists(diagrama_estados) and os.path.exists(tabla_transiciones):
        return  # Ya existen, no hacer nada
    
    print("\n" + "="*60)
    print("📊 Generando diagramas de la Máquina de Turing...")
    print("="*60)
    
    try:
        from src.generar_diagrama import generar_diagrama_completo
        generar_diagrama_completo()
        print("Diagramas generados exitosamente\n")
    except Exception as e:
        print(f"Warning: No se pudieron generar los diagramas: {e}")
        print("Puedes generarlos manualmente ejecutando: python -m src.generar_diagrama\n")


def numero_a_unario(n):
    """
    Convierte un número entero a su representación unaria.
    
    Args:
        n (int): Número a convertir
    
    Returns:
        str: Representación unaria (ej: 3 -> '111')
    """
    if n <= 0:
        return '_'
    return '1' * n


def unario_a_numero(unario):
    """
    Convierte una representación unaria a número entero.
    
    Args:
        unario (str): Cadena en unario
    
    Returns:
        int: Número entero
    """
    if unario == '_' or unario == '':
        return 0
    return unario.count('1')


def fibonacci_python(n):
    """Calcula Fibonacci usando Python normal (para verificar resultados)."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def simular_fibonacci(n, mostrar_pasos=False):
    """
    Simula el cálculo de Fibonacci usando la Máquina de Turing.
    
    Args:
        n (int): El índice del número de Fibonacci a calcular
        mostrar_pasos (bool): Si True, muestra cada paso de la simulación
    
    Returns:
        tuple: (resultado, tiempo_ejecución, numero_pasos)
    """
    # Crear entrada en unario
    entrada = numero_a_unario(n)
    
    print(f"\n{'='*60}")
    print(f"Calculando F({n}) usando Máquina de Turing")
    print(f"{'='*60}")
    print(f"Entrada (unario): {entrada}")
    print(f"Fibonacci esperado: {fibonacci_python(n)}")
    
    # Inicializar máquina
    maquina = MaquinaTuring('config/maquina_fibonacci.json')
    maquina.inicializar(entrada)
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    exito = maquina.ejecutar(max_pasos=100000, mostrar_pasos=mostrar_pasos)
    tiempo_fin = time.time()
    
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    
    if exito:
        resultado_unario = maquina.obtener_resultado()
        resultado = unario_a_numero(resultado_unario)
        
        print(f"\n{'='*60}")
        print(f"Simulación completada!!")
        print(f"{'='*60}")
        print(f"Resultado (unario): {resultado_unario}")
        print(f"Resultado (decimal): {resultado}")
        print(f"Número de pasos: {maquina.pasos}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
        
        # Verificar
        esperado = fibonacci_python(n)
        if resultado == esperado:
            print(f"✓ Resultado correcto!")
        else:
            print(f"✗ Error: Se esperaba {esperado} pero se obtuvo {resultado}")
        
        return resultado, tiempo_ejecucion, maquina.pasos
    else:
        print("La simulación no completó exitosamente")
        return None, tiempo_ejecucion, maquina.pasos


def menu_principal():
    """Menú principal del simulador."""
    
    # Generar diagramas automáticamente si no existen
    verificar_y_generar_diagramas()
    
    while True:
        print("\n" + "="*60)
        print("SIMULADOR DE MÁQUINA DE TURING - FIBONACCI")
        print("="*60)
        print("1. Calcular un número de Fibonacci")
        print("2. Calcular con visualización paso a paso")
        print("3. Ejecutar análisis empírico")
        print("4. Salir")
        print("="*60)
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            entrada = input("\nIngrese la entrada en notación unaria (ej: para F(4) ingrese 1111, para F(0) presione Enter): ").strip()
            
            # Validar que solo tenga 1s o esté vacía
            if entrada != '' and not all(c == '1' for c in entrada):
                print("Entrada inválida. Solo se permiten 1s en notación unaria (ejemplo: 111)")
                continue
            
            # Convertir a n
            n = len(entrada)
            
            if n > 5:
                print(f"Esta implementación funciona para n ≤ 5 (máximo: 11111)")
                confirmar = input("¿Continuar de todos modos? (s/n): ")
                if confirmar.lower() != 's':
                    continue
            
            simular_fibonacci(n, mostrar_pasos=False)
        
        elif opcion == '2':
            entrada = input("\nIngrese la entrada en notación unaria (ej: para F(4) ingrese 1111, para F(0) presione Enter): ").strip()
            
            # Validar que solo tenga 1s o esté vacía
            if entrada != '' and not all(c == '1' for c in entrada):
                print("Entrada inválida. Solo se permiten 1s en notación unaria (ejemplo: 111)")
                continue
            
            # Convertir a n
            n = len(entrada)
            
            if n > 5:
                print(f"Esta implementación funciona para n ≤ 5 (máximo: 11111)")
                confirmar = input("¿Continuar de todos modos? (s/n): ")
                if confirmar.lower() != 's':
                    continue
            
            if n > 3:
                confirmar = input(f"Esta entrada generará varios pasos. ¿Continuar? (s/n): ")
                if confirmar.lower() != 's':
                    continue
            
            simular_fibonacci(n, mostrar_pasos=True)
        
        elif opcion == '3':
            print("\n" + "="*60)
            print("INICIANDO ANÁLISIS EMPÍRICO")
            print("="*60)
            
            try:
                from analisis.analisis_empirico import analisis_empirico
                analisis_empirico()
            except Exception as e:
                print(f"Error al ejecutar el análisis: {e}")
                import traceback
                traceback.print_exc()
        
        elif opcion == '4':
            print("\n¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")


if __name__ == "__main__":
    menu_principal()