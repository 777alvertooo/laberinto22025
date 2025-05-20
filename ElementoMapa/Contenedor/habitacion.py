from ElementoMapa.Contenedor.contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, ente):
        ente.setPosicion(self)
        print("Se encuentra ahora en la habitacion",self.ref)

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)
    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def aceptar(self, visitor):
        print("Visitar habitación ", str(self.ref))
        visitor.visitarHabitacion(self)
        for ch in self.objChildren:
            ch.aceptar(visitor)
        self.form.aceptar(visitor)

    
    def esHabitacion(self):
        return True
    
    def __str__(self):
        info= "En la habitacion " + str(self.ref) +" tenemos estos elementos:" + str(self.form) 
        
        if len(self.objChildren)>0:
            dt = info + "\n [DETALLE DE LOS HIJOS]:"
            for n in self.objChildren:
                dt = dt + "\n["+str(n)+"]"
        return dt