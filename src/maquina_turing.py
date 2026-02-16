import json
from src.cinta import Cinta


class MaquinaTuring:
    """
    Implementación de una Máquina de Turing determinista.
    """
    
    def __init__(self, archivo_config):
        """
        Inicializa la máquina de Turing desde un archivo de configuración.
        
        Args:
            archivo_config (str): Ruta al archivo JSON de configuración
        """
        self.cargar_configuracion(archivo_config)
        self.cinta = None
        self.estado_actual = None
        self.pasos = 0
        self.historial = []
    
    def cargar_configuracion(self, archivo_config):
        """Carga la configuración de la máquina desde un archivo JSON."""
        with open(archivo_config, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        self.nombre = config.get('nombre', 'Máquina de Turing')
        self.estados = config['estados']
        self.estado_inicial = config['estado_inicial']
        self.estados_finales = config['estados_finales']
        self.simbolos_cinta = config['simbolos_cinta']
        
        # Convertir transiciones a diccionario
        self.transiciones = {}
        for t in config['transiciones']:
            clave = (t['estado_actual'], t['simbolo_leido'])
            valor = (t['nuevo_estado'], t['simbolo_escribir'], t['direccion'])
            self.transiciones[clave] = valor
    
    def inicializar(self, entrada):
        """
        Inicializa la máquina con una cadena de entrada.
        
        Args:
            entrada (str): Cadena de entrada para la cinta
        """
        self.cinta = Cinta(entrada, simbolo_blanco='_')
        self.estado_actual = self.estado_inicial
        self.pasos = 0
        self.historial = []
        
        # Guardar configuración inicial
        self.guardar_configuracion()
    
    def paso(self):
        """
        Ejecuta un paso de la máquina de Turing.
        
        Returns:
            bool: True si la máquina continúa, False si se detiene
        """
        if self.estado_actual in self.estados_finales:
            return False
        
        simbolo_actual = self.cinta.leer()
        clave = (self.estado_actual, simbolo_actual)
        
        if clave not in self.transiciones:
            print(f"⚠️  No hay transición definida para ({self.estado_actual}, '{simbolo_actual}')")
            return False
        
        nuevo_estado, simbolo_escribir, direccion = self.transiciones[clave]
        
        # Ejecutar transición
        self.cinta.escribir(simbolo_escribir)
        self.cinta.mover_cabezal(direccion)
        self.estado_actual = nuevo_estado
        self.pasos += 1
        
        # Guardar configuración
        self.guardar_configuracion()
        
        return True
    
    def ejecutar(self, max_pasos=1000, mostrar_pasos=False):
        """
        Ejecuta la máquina hasta que se detenga o alcance el máximo de pasos.
        
        Args:
            max_pasos (int): Número máximo de pasos a ejecutar
            mostrar_pasos (bool): Si True, muestra cada paso en la consola
        
        Returns:
            bool: True si terminó exitosamente, False si excedió el límite
        """
        while self.pasos < max_pasos:
            if mostrar_pasos:
                self.mostrar_configuracion()
            
            if not self.paso():
                if mostrar_pasos:
                    self.mostrar_configuracion()
                return True
        
        print(f"⚠️  Se alcanzó el límite de {max_pasos} pasos")
        return False
    
    def guardar_configuracion(self):
        """Guarda la configuración actual en el historial."""
        config = {
            'paso': self.pasos,
            'estado': self.estado_actual,
            'posicion': self.cinta.posicion_cabezal,
            'cinta': self.cinta.obtener_contenido(),
            'simbolo_actual': self.cinta.leer()
        }
        self.historial.append(config)
    
    def mostrar_configuracion(self):
        """Muestra la configuración actual de la máquina."""
        print(f"\n--- Paso {self.pasos} ---")
        print(f"Estado: {self.estado_actual}")
        print(str(self.cinta))
        print(f"Símbolo leído: '{self.cinta.leer()}'")
    
    def obtener_resultado(self):
        """Retorna el contenido final de la cinta."""
        return self.cinta.obtener_contenido()
    
    def obtener_historial(self):
        """Retorna el historial completo de configuraciones."""
        return self.historial