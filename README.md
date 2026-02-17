# 🤖 Máquina de Turing - Calculadora de Fibonacci

> Simulador de Máquina de Turing determinista de una cinta que calcula la sucesión de Fibonacci en notación unaria, con análisis empírico de complejidad temporal.

## 🎥 Video de Presentación

> 📺 **[Ver video en YouTube](https://youtu.be/rmD1uM6GoO4)**

---

## 📌 Descripción del Proyecto

Este proyecto implementa una **Máquina de Turing determinista de una cinta** capaz de calcular la sucesión de Fibonacci. Fue desarrollado como proyecto académico para el curso de **Análisis de Algoritmos** de la Universidad del Valle de Guatemala.

### ¿Qué es una Máquina de Turing?

Una Máquina de Turing es un modelo matemático de computación que consiste en:
- Una **cinta infinita** dividida en celdas, cada una con un símbolo
- Un **cabezal** que lee y escribe símbolos y se mueve izquierda o derecha
- Un conjunto de **estados** (incluyendo estado inicial y estados finales)
- Una **tabla de transiciones** que define el comportamiento de la máquina

### Enfoque de Implementación

La máquina usa una estrategia de **tabla de lookup** para calcular Fibonacci:
1. **Cuenta** los `1`s en la entrada para determinar n
2. **Mapea** n a su valor de Fibonacci mediante estados específicos
3. **Escribe** el resultado en notación unaria en la cinta

### ¿Por qué solo hasta n = 5?

Esta implementación funciona correctamente para **n = 0 hasta n = 5**. Esto es una decisión de diseño deliberada: una Máquina de Turing completamente iterativa que sume F(i-1) + F(i) en la cinta requeriría:

- **Cientos de estados** para manejar la aritmética unaria
- **Miles de transiciones** para copiar, sumar y desplazar números en la cinta
- **Complejidad exponencial** en tiempo de ejecución incluso para n pequeños

Para los fines de este proyecto académico, esta implementación demuestra todos los conceptos fundamentales: **determinismo, estados, transiciones, y lectura/escritura en cinta**, con resultados verificables y análisis empírico real.

---

## 📋 Convenciones

### Representación de Números: Notación Unaria

El número n se representa escribiendo n veces el símbolo `1` en la cinta.

| Número | Representación |
|--------|---------------|
| 0      | _(vacío)_     |
| 1      | `1`           |
| 2      | `11`          |
| 3      | `111`         |
| 4      | `1111`        |
| 5      | `11111`       |

### Símbolos de la Cinta

| Símbolo | Significado |
|---------|-------------|
| `1`     | Unidad en notación unaria |
| `_`     | Celda vacía (símbolo blanco) |
| `X`     | Marcador temporal durante el conteo |

### Convención de Entrada

El usuario ingresa la entrada **directamente en notación unaria**:
- Para calcular F(4) → ingresar `1111`
- Para calcular F(0) → presionar Enter (entrada vacía)

### Convención de Salida

El resultado queda escrito en la cinta en notación unaria:
- F(4) = 3 → la cinta contiene `111`

### Tabla de Entradas y Salidas

| Entrada (unario) | n | F(n) | Salida (unario) | Pasos |
|-----------------|---|------|----------------|-------|
| _(vacío)_       | 0 | 0    | _(vacío)_      | 1     |
| `1`             | 1 | 1    | `1`            | 8     |
| `11`            | 2 | 1    | `1`            | 11    |
| `111`           | 3 | 2    | `11`           | 15    |
| `1111`          | 4 | 3    | `111`          | 21    |
| `11111`         | 5 | 5    | `11111`        | 28    |

---

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Dependencias

```
matplotlib==3.8.0
numpy==1.26.4
networkx==3.2.1
```

---

## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Emadlgg/proyecto1_ada.git
cd proyecto1_ada
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## 💻 Uso

### Ejecutar el simulador interactivo:
```bash
python -m src.simulador
```

Al iniciar, el programa **genera automáticamente los diagramas** si no existen todavía. Luego muestra el menú principal:

```
============================================================
SIMULADOR DE MÁQUINA DE TURING - FIBONACCI
============================================================
1. Calcular un número de Fibonacci
2. Calcular con visualización paso a paso
3. Ejecutar análisis empírico
4. Salir
============================================================
```

**Opción 1** — Calcula F(n) e imprime el resultado directamente.

**Opción 2** — Muestra cada paso de la simulación: estado actual, posición del cabezal y contenido de la cinta.

**Opción 3** — Ejecuta 100 repeticiones por valor, genera gráficas de dispersión y regresión polinomial.

### Ejecutar solo el análisis empírico:
```bash
python -m analisis.analisis_empirico
```

---

## 📁 Estructura del Proyecto

```
proyecto_turing_fibonacci/
│
├── config/
│   └── maquina_fibonacci.json    # Estados, transiciones y alfabeto
│
├── src/
│   ├── cinta.py                  # Cinta infinita con expansión dinámica
│   ├── maquina_turing.py         # Motor de ejecución de la máquina
│   ├── simulador.py              # Menú interactivo principal
│   └── generar_diagrama.py       # Generación automática de diagramas
│
├── analisis/
│   └── analisis_empirico.py      # Medición de tiempos y regresión polinomial
│
├── docs/
│   ├── convenciones.md           # Convenciones de la máquina
│   ├── descripcion_algoritmo.md  # Descripción detallada del algoritmo
│   ├── diagrama_estados.png      # Diagrama de estados (auto-generado)
│   └── tabla_transiciones.png    # Tabla de transiciones (auto-generado)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Componentes de la Máquina de Turing

### Estados

| Estado | Fase | Función |
|--------|------|---------|
| `q0` | Inicio | Estado inicial, detecta si hay entrada |
| `q_start` | Inicio | Recorre la cinta hacia la derecha hasta el final |
| `q_count` | Conteo | Marca el primer `1` con `X` |
| `q_count_1` a `q_count_5` | Conteo | Marca cada `1` adicional para contar n |
| `q_result_1` a `q_result_5` | Mapeo | Limpia las `X` según F(n) a escribir |
| `q_find_start` | Escritura | Regresa al inicio de la cinta |
| `q_write_*` | Escritura | Escribe el resultado en la cinta |
| `q_pos_*` | Posicionamiento | Posiciona el cabezal al inicio del resultado |
| `q_halt` | Final | Estado de aceptación |

### Fases del Algoritmo

```
Fase 1 — Inicialización:   q0 → q_start
Fase 2 — Conteo de n:      q_start → q_count → q_count_1 → ... → q_count_N
Fase 3 — Mapeo a F(n):     q_count_N → q_result_N
Fase 4 — Limpieza:         q_result_N limpia todas las X
Fase 5 — Escritura:        q_find_start → q_write_* escribe F(n) unos
Fase 6 — Posicionamiento:  q_pos_* → q_halt
```

### Ejemplo completo: Calcular F(3)

```
Paso 0:  [q0]        cinta: _ 1 1 1 _    lee '1', va a q_start
Paso 3:  [q_count]   cinta: _ 1 1 1 _    empieza a marcar desde la derecha
Paso 4:  [q_count_1] cinta: _ 1 1 X _    marca primer 1
Paso 5:  [q_count_2] cinta: _ 1 X X _    marca segundo 1
Paso 6:  [q_count_3] cinta: _ X X X _    marca tercer 1, detecta n=3
Paso 7:  [q_result_2]                    sabe que F(3)=2, limpia X
Paso 11: [q_find_start_2]               regresa al inicio limpio
Paso 12: [q_write_2a] cinta: _ 1 _ _    escribe primer 1
Paso 13: [q_write_2b] cinta: _ 1 1 _    escribe segundo 1
Paso 15: [q_halt]    cinta: _ 1 1 _
                              ↑
         Resultado: 11 = 2 ✓  (F(3) = 2)
```

---

## 📊 Análisis Empírico

El análisis ejecuta cada caso **100 veces** para obtener tiempos promedio precisos usando `time.perf_counter()`.

### Resultados

| n | F(n) | Pasos | Tiempo promedio |
|---|------|-------|----------------|
| 0 | 0    | 1     | ~0.10 ms       |
| 1 | 1    | 8     | ~0.12 ms       |
| 2 | 1    | 11    | ~0.13 ms       |
| 3 | 2    | 15    | ~0.13 ms       |
| 4 | 3    | 21    | ~0.13 ms       |
| 5 | 5    | 28    | ~0.13 ms       |

### Regresión Polinomial

| Grado | R²     | Conclusión |
|-------|--------|------------|
| 1     | ~0.39  | Ajuste lineal insuficiente |
| 2     | ~0.99  | ✅ Mejor ajuste — confirma **O(n²)** |
| 3     | ~0.99  | Similar al grado 2, sin mejora significativa |

**Complejidad temporal confirmada: O(n²)**

El modelo cuadrático con R² = 0.99 confirma que el tiempo de ejecución crece de forma cuadrática con el tamaño de la entrada.

---

## 📝 Entregables del Proyecto

| # | Entregable | Archivo |
|---|-----------|---------|
| 1 | Descripción de convenciones | `docs/convenciones.md` |
| 2 | Diagrama de la Máquina de Turing | `docs/diagrama_estados.png` |
| 3 | Tabla de transiciones | `docs/tabla_transiciones.png` |
| 4 | Archivo de componentes JSON | `config/maquina_fibonacci.json` |
| 5 | Programa en Python | `src/` |
| 6 | Análisis empírico con gráficas | `analisis/` |

---


**Universidad del Valle de Guatemala**  
Curso: Análisis de Algoritmos — 2026