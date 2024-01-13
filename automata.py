# Estados: sin-dinero, con-dinero, c1-servida, c2-servida, c3-servida.
# Acciones: pedir-dinero, pedir-codigo, esperar.
# Percepciones: dinero, c1, c2, c3, servida.

""" Conjunto de condiciones
    Necesarias para las acciones que necesita tomar el agente
"""
REGLAS = {  'sin-dinero' : 'pedir-dinero',
            'con-dinero' : 'pedir-codigo',
            'c1-servida' : 'esperar',
            'c2-servida'  : 'esperar',
            'c3-servida'  : 'esperar'}

""" Conjunto de operadores
    Acciones que realizará el agente de acuerdo a los dos primeros factores
"""
MODELO = {  ('sin-dinero','pedir-dinero','dinero')   : 'con-dinero',
            ( 'con-dinero' ,'pedir-codigo', 'c1')    : 'c1-servida',
            ( 'con-dinero' , 'pedir-codigo', 'c2')   : 'c2-servida',
            ( 'con-dinero', 'pedir-codigo', 'c3')    : 'c3-servida', 
            ( 'c1-servida','esperar','servida')      : 'sin-dinero',
            ( 'c2-servida','esperar ','servida')     : 'sin-dinero',
            ( 'c3-servida','esperar','servida')      : 'sin-dinero'}


class Agente:
    #Constructor para el modelo de agente
    def __init__ (self, modelo, reglas, estado_inicial='',accion_inicial='', **codigos): 
        self.modelo = modelo
        self.reglas = reglas
        self.estado_inicial = estado_inicial
        self.accion_inicial = accion_inicial
        self.accion = None
        self.estado = self.estado_inicial
        self.ult_accion = self.accion_inicial
        self.codigos = codigos
    
    def actuar(self, percepcion) :
        """Actua según la percepción, devolviendo una acción"""
        if not percepcion :
            return self.accion_inicial
        clave = (self.estado, self.ult_accion, percepcion)
        if clave not in self.modelo.keys(): #Si no encuentra una clave valida regresa al estado inicial
            self.accion = None
            self.estado = self.estado_inicial
            self.ult_accion =self.accion_inicial
            return self.accion_inicial
        self.estado = self.modelo[clave]
        if self.estado not in self.reglas.keys(): #Si no encuentra un estado valido regresa al estado inicial
            self.accion = None
            self.estado = self.estado_inicial
            self.ult_accion = self.accion_inicial
            return self.accion_inicial
        #Se hace el retorno de la accion tomada
        accion = self.reglas[self.estado]
        self.ult_accion = accion
        return accion