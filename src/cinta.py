class Cinta:
    """
    Representa la cinta infinita de la Máquina de Turing.
    """
    
    def __init__(self, entrada="", simbolo_blanco="_"):
        """
        Inicializa la cinta con una cadena de entrada.
        
        Args:
            entrada (str): Cadena inicial en la cinta
            simbolo_blanco (str): Símbolo que representa una celda vacía
        """
        self.simbolo_blanco = simbolo_blanco
        self.cinta = list(entrada) if entrada else [simbolo_blanco]
        self.posicion_cabezal = 0
        
        # Añadir espacios en blanco a los lados
        self.expandir_izquierda(10)
        self.expandir_derecha(10)
        self.posicion_cabezal = 10  # Ajustar posición inicial
    
    def expandir_izquierda(self, cantidad=10):
        """Expande la cinta hacia la izquierda."""
        self.cinta = [self.simbolo_blanco] * cantidad + self.cinta
    
    def expandir_derecha(self, cantidad=10):
        """Expande la cinta hacia la derecha."""
        self.cinta.extend([self.simbolo_blanco] * cantidad)
    
    def leer(self):
        """Lee el símbolo en la posición actual del cabezal."""
        # Expandir si es necesario
        if self.posicion_cabezal < 0:
            self.expandir_izquierda(10)
            self.posicion_cabezal += 10
        if self.posicion_cabezal >= len(self.cinta):
            self.expandir_derecha(10)
        
        return self.cinta[self.posicion_cabezal]
    
    def escribir(self, simbolo):
        """Escribe un símbolo en la posición actual del cabezal."""
        if self.posicion_cabezal < 0:
            self.expandir_izquierda(10)
            self.posicion_cabezal += 10
        if self.posicion_cabezal >= len(self.cinta):
            self.expandir_derecha(10)
        
        self.cinta[self.posicion_cabezal] = simbolo
    
    def mover_cabezal(self, direccion):
        """
        Mueve el cabezal en la dirección especificada.
        
        Args:
            direccion (str): 'L' (izquierda), 'R' (derecha), 'N' (no mover)
        """
        if direccion == 'L':
            self.posicion_cabezal -= 1
        elif direccion == 'R':
            self.posicion_cabezal += 1
        # 'N' no hace nada
    
    def obtener_contenido(self):
        """Retorna el contenido de la cinta como string, sin espacios en blanco en los extremos."""
        contenido = ''.join(self.cinta).strip(self.simbolo_blanco)
        return contenido if contenido else self.simbolo_blanco
    
    def __str__(self):
        """Representación visual de la cinta con el cabezal."""
        # Encontrar rango útil (sin muchos blancos)
        inicio = max(0, self.posicion_cabezal - 20)
        fin = min(len(self.cinta), self.posicion_cabezal + 20)
        
        cinta_visible = ''.join(self.cinta[inicio:fin])
        posicion_relativa = self.posicion_cabezal - inicio
        
        # Crear indicador del cabezal
        indicador = ' ' * posicion_relativa + '^'
        
        return f"Cinta: {cinta_visible}\n       {indicador}"