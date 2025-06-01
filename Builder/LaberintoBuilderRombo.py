from Builder.LaberintoBuilder import LaberintoBuilder
from Formas.Rombo import Rombo



class LaberintoBuilderRombo(LaberintoBuilder):

    def fabricarFormaEspecifica(self, forma_str: str):
        forma_str_lower = forma_str.lower().strip()
        forma_obj = None

        if forma_str_lower == "rombo":
            print(f"BUILDER: Fabricando forma Rombo (especificada como '{forma_str}').")
            forma_obj = Rombo()
        else:
            print(f"BUILDER WARN: Forma '{forma_str}' desconocida o no implementada. Usando Rombo por defecto.")
            forma_obj = Rombo() 
        if forma_obj and hasattr(forma_obj, 'agregarOrientacion'):
            forma_obj.agregarOrientacion(self.fabricarNoreste())
            forma_obj.agregarOrientacion(self.fabricarNoroeste())
            forma_obj.agregarOrientacion(self.fabricarSureste())
            forma_obj.agregarOrientacion(self.fabricarSuroeste())
        elif forma_obj:
            print(f"BUILDER ERROR: La forma '{type(forma_obj).__name__}' creada no tiene método 'agregarOrientacion'.")
        else:
            print(f"BUILDER ERROR CRÍTICO: No se pudo crear un objeto forma. Creando Rombo vacío.")
            return Rombo() 

        return forma_obj
    
    def obtenerObjeto(self, cadena_orientacion: str): 
        obj = None
        cadena_lower = cadena_orientacion.lower().strip()
        if cadena_lower == 'noreste': obj = self.fabricarNoreste()
        elif cadena_lower == 'noroeste': obj = self.fabricarNoroeste()
        elif cadena_lower == 'sureste': obj = self.fabricarSureste()
        elif cadena_lower == 'suroeste': obj = self.fabricarSuroeste()
        else: print(f"BUILDER WARN: Orientación '{cadena_orientacion}' desconocida en obtenerObjeto.")
        return obj