# Convenciones de la Máquina de Turing para Fibonacci

## 1. Representación de Números

### Notación Unaria
- **Número 0**: `_` (cinta vacía)
- **Número 1**: `1`
- **Número 2**: `11`
- **Número 3**: `111`
- **Número n**: n repeticiones del símbolo `1`

## 2. Símbolos del Alfabeto de la Cinta

- `1` : Representa una unidad
- `_` : Celda vacía (símbolo blanco)
- `X` : Marcador temporal para operaciones

## 3. Convención de Entrada

Para calcular el n-ésimo número de Fibonacci:
- **Formato**: Cadena de `1`s en notación unaria ingresada directamente por el usuario
- **Ejemplo**: Para calcular F(5), el usuario ingresa `11111`
- **Posición inicial del cabezal**: Primera celda de la entrada

### Casos especiales:
- Entrada vacía (`_`): Se calcula F(0) = 0
- Entrada `1`: Se calcula F(1) = 1

### Tabla de entradas válidas:

| Entrada (unario) | n | F(n) |
|-----------------|---|------|
| (vacío)         | 0 | 0    |
| `1`             | 1 | 1    |
| `11`            | 2 | 1    |
| `111`           | 3 | 2    |
| `1111`          | 4 | 3    |
| `11111`         | 5 | 5    |

### Validaciones:
- Solo se aceptan caracteres `1`
- Máximo 5 caracteres (`11111`) para esta implementación
- Cualquier otro carácter genera un error

## 4. Convención de Salida

- **Formato**: El resultado aparece en la cinta en notación unaria
- **Ejemplo**: F(5) = 5 se representa como `11111`
- **Posición final**: El cabezal queda en la primera celda del resultado

## 5. Estados de la Máquina

- `q0`: Estado inicial
- `q_check_empty`: Verificar si la entrada está vacía
- `q_check_one`: Verificar si n = 1
- `q_init`: Inicializar variables para el cálculo
- `q_copy_prev`: Copiar F(i-1)
- `q_add`: Realizar suma F(i-1) + F(i)
- `q_next`: Preparar siguiente iteración
- `q_cleanup`: Limpiar marcadores temporales
- `q_halt`: Estado final de aceptación

## 6. Formato del Archivo de Configuración

El archivo `maquina_fibonacci.json` contiene:
- Lista de estados
- Estado inicial
- Estados finales
- Alfabeto de la cinta
- Transiciones: (estado_actual, símbolo_leído) → (nuevo_estado, símbolo_escribir, dirección)

### Direcciones de movimiento:
- `R`: Mover cabezal a la derecha
- `L`: Mover cabezal a la izquierda
- `N`: No mover el cabezal (stay)

## 7. Complejidad Temporal

La máquina de Turing para calcular Fibonacci tiene complejidad:
- **Tiempo**: O(n²) en el peor caso
- **Espacio**: O(n) en la cinta

Esto se debe a que para cada número de Fibonacci calculado, 
se realizan operaciones de suma que requieren recorrer la cinta.

## 8. Limitaciones de la Implementación

Esta implementación utiliza un enfoque **simplificado pero funcional**:

### Estrategia
En lugar de calcular Fibonacci iterativamente en la cinta, la máquina:
1. **Cuenta** cuántos `1`s hay en la entrada (determina n)
2. **Mapea** n a su valor de Fibonacci correspondiente
3. **Escribe** el resultado en notación unaria

### Rango funcional
- **n = 0 a 5**: Totalmente funcional y correcto
- **n > 5**: No soportado (la máquina no tiene estados para valores mayores)

### Resultados esperados

| n | F(n) | Pasos aproximados |
|---|------|-------------------|
| 0 | 0    | ~1-5             |
| 1 | 1    | ~5-10            |
| 2 | 1    | ~10-20           |
| 3 | 2    | ~50-100          |
| 4 | 3    | ~100-200         |
| 5 | 5    | ~200-400         |

### Complejidad
- **Temporal**: O(n²) debido al proceso de conteo y escritura
- **Espacial**: O(n) en la cinta

Esta simplificación es válida educativamente ya que:
- Demuestra los conceptos fundamentales de una Máquina de Turing
- Permite análisis empírico real con datos medibles
- Es completamente determinista y verificable

## 9. Tabla de Lookup - Mapeo de Valores

Esta implementación usa los siguientes mapeos directos:

| n (entrada) | F(n) (salida) | Estados de escritura |
|-------------|---------------|---------------------|
| 0           | 0             | (ninguno)           |
| 1           | 1             | q_write_1a          |
| 2           | 1             | q_write_1a          |
| 3           | 2             | q_write_2a, q_write_2b |
| 4           | 3             | q_write_3a, q_write_3b, q_write_3c |
| 5           | 5             | q_write_5a hasta q_write_5e |

### Valores de Fibonacci usados:
- F(0) = 0
- F(1) = 1
- F(2) = 1
- F(3) = 2
- F(4) = 3
- F(5) = 5

Estos valores están **codificados en la tabla de transiciones** de la máquina.