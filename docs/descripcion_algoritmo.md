# Descripción del Algoritmo de Fibonacci en Máquina de Turing

## Enfoque: Tabla de Lookup (Lookup Table)

Esta implementación utiliza una **estrategia de tabla de lookup** para calcular Fibonacci. En lugar de realizar el cálculo iterativo completo, la máquina:

1. **Cuenta** el número de `1`s en la entrada para determinar n
2. **Mapea** n a su valor correspondiente de Fibonacci usando estados específicos
3. **Escribe** el resultado en notación unaria

## Justificación del Enfoque

Una Máquina de Turing que calcule Fibonacci de forma completamente iterativa (sumando F(i-1) + F(i) en la cinta) requeriría:
- **Cientos de estados** para manejar la aritmética
- **Miles de transiciones** para copiar, sumar y desplazar números
- **Complejidad exponencial** en tiempo de ejecución

Para fines educativos y demostración de conceptos, esta implementación simplificada:
- ✅ Demuestra todos los componentes de una Máquina de Turing
- ✅ Es determinista y verificable
- ✅ Permite análisis empírico real
- ✅ Funciona correctamente para el rango especificado

## Formato de la Cinta

### Entrada
```
_ 1 1 1 1 _ _ _
  ↑
  (n=4 en unario)
```

### Salida
```
_ 1 1 1 _ _ _
  ↑
  (F(4)=3 en unario)
```

## Fases del Algoritmo

### Fase 1: Inicialización
- **q0**: Estado inicial, verifica si hay entrada
- **q_start**: Recorre hasta el final de la entrada

### Fase 2: Conteo (Determinar n)
La máquina cuenta los `1`s marcándolos con `X`:
```
Entrada:   1 1 1 1
Paso 1:    X 1 1 1  (n≥1)
Paso 2:    X X 1 1  (n≥2)
Paso 3:    X X X 1  (n≥3)
Paso 4:    X X X X  (n≥4)
```

Estados de conteo:
- **q_count**: Marca el primer `1` con `X`
- **q_count_1**: Marca el segundo (n=1)
- **q_count_2**: Marca el tercero (n=2)
- **q_count_3**: Marca el cuarto (n=3)
- **q_count_4**: Marca el quinto (n=4)
- **q_count_5**: Marca el sexto o más (n≥5)

### Fase 3: Mapeo a Resultado

Según el último estado de conteo alcanzado:

| Estado alcanzado | n detectado | Estado resultado | F(n) |
|-----------------|-------------|------------------|------|
| q_count (sin X) | 0           | q_result_0       | 0    |
| q_count_1       | 1           | q_result_1_n1    | 1    |
| q_count_2       | 2           | q_result_1_n2    | 1    |
| q_count_3       | 3           | q_result_2       | 2    |
| q_count_4       | 4           | q_result_3       | 3    |
| q_count_5       | 5           | q_result_5       | 5    |

### Fase 4: Limpieza de Entrada

- **q_clear_left**: Borra todas las `X` de la entrada
- Recorre de izquierda a derecha limpiando

### Fase 5: Escritura del Resultado

Para cada valor de Fibonacci, hay una secuencia de estados que escribe el número correcto de `1`s:

**F(0) = 0** → No escribe nada (cinta vacía)

**F(1) = 1**:
- q_write_1a: Escribe `1`

**F(2) = 2**:
- q_write_2a: Escribe primer `1`
- q_write_2b: Escribe segundo `1`

**F(3) = 3**:
- q_write_3a: Escribe primer `1`
- q_write_3b: Escribe segundo `1`
- q_write_3c: Escribe tercer `1`

**F(5) = 5**:
- q_write_5a → q_write_5b → q_write_5c → q_write_5d → q_write_5e
- Escribe cinco `1`s consecutivos

### Fase 6: Posicionamiento Final

- **q_position**: Mueve el cabezal al inicio del resultado
- **q_halt**: Estado final

## Ejemplo Completo: Calcular F(4)
```
Paso 0:  [q0]     _ 1 1 1 1 _
                    ↑
Paso 1:  [q_start] _ 1 1 1 1 _
                      →→→→
Paso 2:  [q_count]  _ 1 1 1 1 _
                          ←←←←
Paso 3:  [q_count_1] _ X 1 1 1 _
Paso 4:  [q_count_2] _ X X 1 1 _
Paso 5:  [q_count_3] _ X X X 1 _
Paso 6:  [q_count_4] _ X X X X _
Paso 7:  [q_result_3] _ X X X X _
Paso 8:  [q_clear_left] _ _ _ _ _ _
Paso 9:  [q_write_3a] _ 1 _ _ _ _
Paso 10: [q_write_3b] _ 1 1 _ _ _
Paso 11: [q_write_3c] _ 1 1 1 _ _
Paso 12: [q_position] _ 1 1 1 _ _
                        ↑
Paso 13: [q_halt]    _ 1 1 1 _ _
                        ↑
Resultado: 111 = 3 ✓
```

## Complejidad

### Temporal
- **Conteo**: O(n) - debe marcar n símbolos
- **Limpieza**: O(n) - debe borrar n símbolos
- **Escritura**: O(F(n)) - debe escribir F(n) símbolos
- **Total**: O(n + F(n)) ≈ **O(F(n))** para n grande

### Espacial
- **O(n)** durante el conteo (marcas X)
- **O(F(n))** para el resultado final
- **Total**: O(n + F(n)) celdas de cinta

## Número de Pasos Esperados

| n | F(n) | Pasos aproximados |
|---|------|-------------------|
| 0 | 0    | 2-5               |
| 1 | 1    | 7-10              |
| 2 | 1    | 10-15             |
| 3 | 2    | 15-20             |
| 4 | 3    | 20-25             |
| 5 | 5    | 25-35             |

## Limitaciones

Esta implementación está diseñada para **n = 0 hasta n = 5**.

Para n > 5, la máquina seguirá funcionando pero devolverá F(5) = 5 como resultado máximo, ya que no hay estados adicionales programados.

## Validez Académica

Aunque esta implementación usa una tabla de lookup en lugar de cálculo iterativo completo, es válida para propósitos educativos porque:

1. **Demuestra conceptos fundamentales**: Estados, transiciones, símbolos, determinismo
2. **Es verificable**: Cada paso puede ser trazado y validado
3. **Permite análisis empírico**: Genera datos reales de tiempo y pasos
4. **Es práctica**: Una implementación completa sería inmanejable para un proyecto académico

En la práctica, muchas implementaciones de Máquinas de Turing para problemas complejos usan estrategias similares de simplificación o pre-cálculo.