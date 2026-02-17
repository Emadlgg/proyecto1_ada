import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import networkx as nx


def cargar_configuracion(archivo):
    """Carga la configuración de la máquina."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)


def crear_diagrama_estados(config, archivo_salida='docs/diagrama_estados.png'):
    """
    Crea un diagrama visual de estados de la Máquina de Turing.
    
    Args:
        config (dict): Configuración de la máquina
        archivo_salida (str): Ruta donde guardar el diagrama
    """
    # Crear grafo dirigido
    G = nx.MultiDiGraph()
    
    # Agregar nodos (estados)
    for estado in config['estados']:
        G.add_node(estado)
    
    # Agregar aristas (transiciones)
    transiciones_agrupadas = {}
    for t in config['transiciones']:
        origen = t['estado_actual']
        destino = t['nuevo_estado']
        simbolo_leido = t['simbolo_leido']
        simbolo_escribir = t['simbolo_escribir']
        direccion = t['direccion']
        
        etiqueta = f"{simbolo_leido}→{simbolo_escribir},{direccion}"
        
        clave = (origen, destino)
        if clave not in transiciones_agrupadas:
            transiciones_agrupadas[clave] = []
        transiciones_agrupadas[clave].append(etiqueta)
    
    # Agregar aristas agrupadas
    for (origen, destino), etiquetas in transiciones_agrupadas.items():
        etiqueta_completa = "\\n".join(etiquetas[:3])  # Limitar a 3 para legibilidad
        if len(etiquetas) > 3:
            etiqueta_completa += f"\\n... (+{len(etiquetas)-3})"
        G.add_edge(origen, destino, label=etiqueta_completa)
    
    # Crear layout
    plt.figure(figsize=(24, 16))
    
    # Usar layout circular para estados
    pos = nx.spring_layout(G, k=3, iterations=50, seed=42)
    
    # Dibujar nodos
    estado_inicial = config['estado_inicial']
    estados_finales = config['estados_finales']
    
    # Separar tipos de nodos
    nodos_normales = [n for n in G.nodes() if n != estado_inicial and n not in estados_finales]
    
    # Dibujar nodos normales
    nx.draw_networkx_nodes(G, pos, nodelist=nodos_normales, 
                          node_color='lightblue', node_size=3000, 
                          node_shape='o', edgecolors='black', linewidths=2)
    
    # Dibujar estado inicial
    nx.draw_networkx_nodes(G, pos, nodelist=[estado_inicial], 
                          node_color='lightgreen', node_size=3500, 
                          node_shape='o', edgecolors='darkgreen', linewidths=3)
    
    # Dibujar estados finales
    nx.draw_networkx_nodes(G, pos, nodelist=estados_finales, 
                          node_color='lightcoral', node_size=3500, 
                          node_shape='o', edgecolors='darkred', linewidths=3)
    
    # Doble círculo para estados finales
    for estado in estados_finales:
        x, y = pos[estado]
        circle = plt.Circle((x, y), 0.05, fill=False, edgecolor='darkred', linewidth=2)
        plt.gca().add_patch(circle)
    
    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    # Dibujar aristas con curvatura
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, 
                          arrowsize=20, arrowstyle='->', 
                          connectionstyle='arc3,rad=0.1', width=1.5)
    
    # Título y leyenda
    plt.title(config['nombre'], fontsize=20, fontweight='bold', pad=20)
    
    # Crear leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', 
                  markersize=15, label='Estado Inicial', markeredgecolor='darkgreen', markeredgewidth=2),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightcoral', 
                  markersize=15, label='Estado Final', markeredgecolor='darkred', markeredgewidth=2),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', 
                  markersize=15, label='Estado Normal', markeredgecolor='black', markeredgewidth=2)
    ]
    plt.legend(handles=legend_elements, loc='upper left', fontsize=12)
    
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Diagrama guardado en: {archivo_salida}")
    plt.close()


def crear_tabla_transiciones(config, archivo_salida='docs/tabla_transiciones.png'):
    """
    Crea una tabla visual de las transiciones.
    
    Args:
        config (dict): Configuración de la máquina
        archivo_salida (str): Ruta donde guardar la tabla
    """
    transiciones = config['transiciones']
    
    # Preparar datos para la tabla
    datos_tabla = []
    for i, t in enumerate(transiciones[:30], 1):  # Limitar a 30 para legibilidad
        datos_tabla.append([
            i,
            t['estado_actual'],
            t['simbolo_leido'],
            t['nuevo_estado'],
            t['simbolo_escribir'],
            t['direccion']
        ])
    
    if len(transiciones) > 30:
        datos_tabla.append(['...', '...', '...', '...', '...', '...'])
    
    fig, ax = plt.subplots(figsize=(14, max(10, len(datos_tabla) * 0.4)))
    ax.axis('tight')
    ax.axis('off')
    
    tabla = ax.table(cellText=datos_tabla,
                    colLabels=['#', 'Estado Actual', 'Símbolo Leído', 
                              'Nuevo Estado', 'Escribir', 'Mover'],
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.08, 0.2, 0.15, 0.2, 0.15, 0.12])
    
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(9)
    tabla.scale(1, 2)
    
    # Estilizar encabezado
    for i in range(6):
        tabla[(0, i)].set_facecolor('#4CAF50')
        tabla[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternar colores de filas
    for i in range(1, len(datos_tabla) + 1):
        for j in range(6):
            if i % 2 == 0:
                tabla[(i, j)].set_facecolor('#f0f0f0')
    
    plt.title(f'Tabla de Transiciones - {config["nombre"]}', 
             fontsize=16, fontweight='bold', pad=20)
    
    plt.savefig(archivo_salida, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Tabla de transiciones guardada en: {archivo_salida}")
    plt.close()


def generar_diagrama_completo():
    """Genera todos los diagramas de la máquina."""
    print("\n" + "="*60)
    print("GENERANDO DIAGRAMAS DE LA MÁQUINA DE TURING")
    print("="*60)
    
    config = cargar_configuracion('config/maquina_fibonacci.json')
    
    print(f"\nMáquina: {config['nombre']}")
    print(f"Total de estados: {len(config['estados'])}")
    print(f"Total de transiciones: {len(config['transiciones'])}")
    
    print("\nGenerando diagrama de estados...")
    crear_diagrama_estados(config)
    
    print("\nGenerando tabla de transiciones...")
    crear_tabla_transiciones(config)
    
    print("\n" + "="*60)
    print("DIAGRAMAS GENERADOS EXITOSAMENTE")
    print("="*60)
    print("\nArchivos creados:")
    print("  📄 docs/diagrama_estados.png")
    print("  📄 docs/tabla_transiciones.png")


if __name__ == "__main__":
    generar_diagrama_completo()