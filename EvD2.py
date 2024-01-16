import sqlite3
class ControladorBD:
    def conexionBD(self):
        try:
            conexion = sqlite3.connect('C:/Users/mimoc/OneDrive/UNIVERSIDAD/8 OCTAVO CUATRIMESTRE/Sistemas Inteligentes/ActD.sql')
            print('Conectado a la BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se puede conectar')
