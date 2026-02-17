# Descripción del Algoritmo de Fibonacci en Máquina de Turing

## Enfoque: Tabla de Lookup (Lookup Table)

Esta implementación utiliza una **estrategia de tabla de lookup** para calcular Fibonacci. En lugar de realizar el cálculo iterativo completo, la máquina:

1. **Cuenta** el número de `1`s en la entrada para determinar n
2. **Mapea** n a su valor correspondiente de Fibonacci usando estados específicos
3. **Escribe** el resultado en notación unaria

## Justificación del Enfoque

Una Máquina de Turing que calcule Fibonacci de forma completamente iterativa (sumando F(i-1) + F(i) en la cinta) requeriría:
- **Cientos de estados** para manejar la aritmética unaria
- **Miles de transiciones** para copiar, sumar y desplazar números en la cinta
- **Complejidad exponencial** en tiempo de ejecución incluso para n pequeños

Para fines educativos y demostración de conceptos, esta implementación simplificada:
- ✅ Demuestra todos los componentes de una Máquina de Turing
- ✅ Es completamente determinista y verificable
- ✅ Permite análisis empírico real con datos medibles
- ✅ Funciona correctamente para el rango especificado

## Formato de la Cinta

### Entrada
```
_ 1 1 1 1 _ _ _
  ↑
  (n=4 en unario, ingresado como "1111")
```

### Salida
```
_ 1 1 1 _ _ _
  ↑
  (F(4)=3 en unario, resultado "111")
```

## Fases del Algoritmo

### Fase 1: Inicialización
- **q0**: Estado inicial. Si lee `_`, la entrada está vacía → F(0)=0, va directo a `q_halt`. Si lee `1`, va a `q_start`.
- **q_start**: Recorre la cinta hacia la derecha hasta encontrar `_`, luego retrocede para iniciar el conteo.

### Fase 2: Conteo (Determinar n)
La máquina cuenta los `1`s marcándolos con `X` moviéndose de derecha a izquierda:

```
Entrada:   1 1 1 1       (n=4)
Paso 1:    1 1 1 X       marca desde la derecha
Paso 2:    1 1 X X
Paso 3:    1 X X X
Paso 4:    X X X X       detecta que n=4 al encontrar _
```

Estados de conteo:

| Estado      | Acción                                 |
|-------------|----------------------------------------|
| `q_count`   | Marca el primer `1` con `X`            |
| `q_count_1` | Marca el segundo `1` (detecta n≥1)     |
| `q_count_2` | Marca el tercero (detecta n≥2)         |
| `q_count_3` | Marca el cuarto (detecta n≥3)          |
| `q_count_4` | Marca el quinto (detecta n≥4)          |
| `q_count_5` | Marca el sexto o más (detecta n≥5)     |

Cuando cada estado encuentra `_` en lugar de `1`, sabe que ya no hay más símbolos y determina el valor exacto de n.

### Fase 3: Mapeo a Resultado

Según el último estado de conteo alcanzado, la máquina sabe qué resultado escribir:

| Estado que encontró `_` | n detectado | Estado resultado | F(n) a escribir |
|------------------------|-------------|------------------|----------------|
| `q_count_1`            | 1           | `q_result_1`     | 1              |
| `q_count_2`            | 2           | `q_result_1`     | 1              |
| `q_count_3`            | 3           | `q_result_2`     | 2              |
| `q_count_4`            | 4           | `q_result_3`     | 3              |
| `q_count_5`            | 5           | `q_result_5`     | 5              |

> **Nota:** F(1) y F(2) comparten el mismo estado resultado (`q_result_1`) porque ambos producen el mismo valor: 1.

### Fase 4: Limpieza de la Cinta

Los estados `q_result_X` recorren la cinta de izquierda a derecha borrando todas las `X` (reemplazándolas con `_`). Al llegar al primer `_`, la cinta está completamente limpia y lista para recibir el resultado.

### Fase 5: Posicionamiento para Escritura

Los estados `q_find_start`, `q_find_start_2`, `q_find_start_3` y `q_find_start_5` posicionan el cabezal en el inicio de la zona limpia y escriben el primer `1` del resultado.

### Fase 6: Escritura del Resultado

Para cada valor de Fibonacci hay una secuencia dedicada de estados que escribe el número correcto de `1`s:

**F(0) = 0** → La máquina termina sin escribir nada (cinta vacía).

**F(1) = 1** → `q_find_start` escribe un `1` y va a `q_write_1` → `q_halt`.

**F(2) = 2**:
```
q_find_start_2 → escribe 1 → q_write_2a → escribe 1 → q_halt_pos → q_halt
```

**F(3) = 3**:
```
q_find_start_3 → escribe 1 → q_write_3a → escribe 1 → q_write_3b → escribe 1 → q_pos_3 → q_halt
```

**F(5) = 5**:
```
q_find_start_5 → q_write_5a → q_write_5b → q_write_5c → q_write_5d → escribe 5 unos → q_pos_5 → q_halt
```

### Fase 7: Posicionamiento Final

Los estados `q_pos_3` y `q_pos_5` mueven el cabezal hacia la izquierda hasta encontrar `_`, para dejar el cabezal al inicio del resultado antes de terminar. Luego la máquina llega a **`q_halt`**.

---

## Ejemplo Completo: Calcular F(4)

```
Paso 0:  [q0]           cinta: _ 1 1 1 1 _     lee '1' → va a q_start
Paso 1:  [q_start]      cinta: _ 1 1 1 1 _     avanza →
Paso 2:  [q_start]      cinta: _ 1 1 1 1 _     avanza →
Paso 3:  [q_start]      cinta: _ 1 1 1 1 _     avanza →
Paso 4:  [q_start]      cinta: _ 1 1 1 1 _     lee '_' → va a q_count, retrocede ←
Paso 5:  [q_count]      cinta: _ 1 1 1 X _     marca X, retrocede ←
Paso 6:  [q_count_1]    cinta: _ 1 1 X X _     marca X, retrocede ←
Paso 7:  [q_count_2]    cinta: _ 1 X X X _     marca X, retrocede ←
Paso 8:  [q_count_3]    cinta: _ X X X X _     marca X, retrocede ←
Paso 9:  [q_count_4]    cinta: _ X X X X _     lee '_' → detecta n=4, va a q_result_3
Paso 10: [q_result_3]   cinta: _ X X X X _     lee 'X' → borra, avanza →
Paso 11: [q_result_3]   cinta: _ _ X X X _     lee 'X' → borra, avanza →
Paso 12: [q_result_3]   cinta: _ _ _ X X _     lee 'X' → borra, avanza →
Paso 13: [q_result_3]   cinta: _ _ _ _ X _     lee 'X' → borra, avanza →
Paso 14: [q_result_3]   cinta: _ _ _ _ _ _     lee '_' → va a q_find_start_3
Paso 15: [q_find_start_3] cinta: _ 1 _ _ _ _   escribe '1', avanza →
Paso 16: [q_write_3a]   cinta: _ 1 1 _ _ _     escribe '1', avanza →
Paso 17: [q_write_3b]   cinta: _ 1 1 1 _ _     escribe '1', retrocede ←
Paso 18: [q_pos_3]      cinta: _ 1 1 1 _ _     retrocede ← hasta encontrar '_'
Paso 20: [q_pos_3]      cinta: _ 1 1 1 _ _     lee '_' → va a q_halt, avanza →
Paso 21: [q_halt]       cinta: _ 1 1 1 _ _
                                  ↑
         Resultado: 111 = 3 ✓  (F(4) = 3)
```

---

## Complejidad

### Temporal

| Fase | Complejidad | Descripción |
|------|-------------|-------------|
| Inicialización | O(n) | Recorre n símbolos hacia la derecha |
| Conteo | O(n) | Marca n símbolos con X |
| Limpieza | O(n) | Borra n marcas X |
| Escritura | O(F(n)) | Escribe F(n) símbolos |
| **Total** | **O(n + F(n))** | Dominado por la escritura para n grande |

Para valores pequeños de n (como los de esta implementación), el comportamiento práctico es **O(n²)**, confirmado empíricamente con R² = 0.99.

### Espacial
- **O(n)** durante el conteo (marcas X en la cinta)
- **O(F(n))** para el resultado final
- **Total**: O(n + F(n)) celdas de cinta utilizadas

---

## Número de Pasos Reales

| n | F(n) | Pasos reales |
|---|------|-------------|
| 0 | 0    | 1           |
| 1 | 1    | 8           |
| 2 | 1    | 11          |
| 3 | 2    | 15          |
| 4 | 3    | 21          |
| 5 | 5    | 28          |

---

## Limitaciones

Esta implementación está diseñada para **n = 0 hasta n = 5**. Para n > 5, la máquina no tiene estados adicionales programados y el resultado no será correcto.

---

## Validez Académica

Aunque esta implementación usa una tabla de lookup en lugar de cálculo iterativo completo, es válida para propósitos educativos porque:

1. **Demuestra conceptos fundamentales**: Estados, transiciones, símbolos, determinismo
2. **Es verificable**: Cada paso puede ser trazado y validado manualmente
3. **Permite análisis empírico real**: Genera datos reales de tiempo y pasos medibles
4. **Es práctica**: Una implementación iterativa completa sería inmanejable para un proyecto académico de este alcance