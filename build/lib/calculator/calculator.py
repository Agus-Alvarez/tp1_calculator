import logging

# Configuración básica del sistema de registros
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class complex_calculator:
    def __init__(self, real, imag):
    
        # Inicializa el número complejo con la parte real e imaginaria.
        
        if not isinstance(real, (int, float)) or not isinstance(imag, (int, float)):
            logging.error("ERROR: Las entradas deben ser números")
            raise ValueError("ERROR: Las entradas deben ser números")
        
        self.real = real
        self.imag = imag
        logging.info(f"Se creó un número complejo: ({self.real}, {self.imag})")
    
    def add(self, other):
    
        # Suma dos números complejos.

        if not isinstance(other, complex_calculator):
            logging.error("ERROR: El objeto pasado no es un número complejo")
            return "ERROR: El objeto pasado no es un número complejo"
        
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        logging.info(f"Suma exitosa: ({self.real}, {self.imag}) + ({other.real}, {other.imag}) = ({real_part}, {imag_part})")
        return real_part, imag_part
    
    def subtract(self, other):
    
        # Resta dos números complejos.

        if not isinstance(other, complex_calculator):
            logging.error("ERROR: El objeto pasado no es un número complejo")
            return "ERROR: El objeto pasado no es un número complejo"
        
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        logging.info(f"Resta exitosa: ({self.real}, {self.imag}) - ({other.real}, {other.imag}) = ({real_part}, {imag_part})")
        return real_part, imag_part
    
    def multiply(self, other):
    
        # Multiplica dos números complejos.
    
        if not isinstance(other, complex_calculator):
            logging.error("ERROR: El objeto pasado no es un número complejo")
            return "ERROR: El objeto pasado no es un número complejo"
        
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        logging.info(f"Multiplicación exitosa: ({self.real}, {self.imag}) * ({other.real}, {other.imag}) = ({real_part}, {imag_part})")
        return real_part, imag_part
    
    def divide(self, other):
    
        # Divide dos números complejos.
    
        if not isinstance(other, complex_calculator):
            logging.error("ERROR: El objeto pasado no es un número complejo")
            return "ERROR: El objeto pasado no es un número complejo"
        
        denominator = other.real**2 + other.imag**2  # (c^2 + d^2)
        if denominator == 0:
            logging.error("ERROR: División por cero no permitida")
            raise ZeroDivisionError("No se puede dividir por cero")
        
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        logging.info(f"División exitosa: ({self.real}, {self.imag}) / ({other.real}, {other.imag}) = ({real_part}, {imag_part})")
        return real_part, imag_part

    def __str__(self):
        
        # Representación en cadena del número complejo.
        
        return f"({self.real}, {self.imag})"
