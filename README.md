# Máquina de Turing - Calculadora de Fibonacci

Simulador de Máquina de Turing determinista que calcula la sucesión de Fibonacci en notación unaria.

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. Clona o descarga este proyecto

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar el simulador interactivo:
```bash
python -m src.simulador
```

### Ejecutar el análisis empírico:
```bash
python -m analisis.analisis_empirico
```

## 📁 Estructura del Proyecto
```
proyecto_turing_fibonacci/
├── config/
│   └── maquina_fibonacci.json    # Configuración de la máquina
├── src/
│   ├── cinta.py                  # Implementación de la cinta
│   ├── maquina_turing.py         # Máquina de Turing
│   └── simulador.py              # Simulador principal
├── analisis/
│   └── analisis_empirico.py      # Análisis de tiempos
├── docs/
│   └── convenciones.md           # Documentación de convenciones
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

## 📊 Entregables

1. ✅ Descripción de convenciones → `docs/convenciones.md`
2. ✅ Diagrama de la máquina → Ver archivo de configuración
3. ✅ Archivo de componentes → `config/maquina_fibonacci.json`
4. ✅ Programa en Python → `src/`
5. ✅ Análisis empírico → `analisis/analisis_empirico.py`

## 🎯 Ejemplos

Calcular F(5):
- Entrada: `11111` (5 en unario)
- Salida: `11111` (5 en unario)
- F(5) = 5

## 📝 Notas

- La máquina usa notación unaria para representar números
- El símbolo `_` representa celdas vacías
- El símbolo `#` se usa como separador
- El símbolo `X` se usa como marcador temporal