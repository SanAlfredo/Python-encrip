import sys
import os
from cryptography.fernet import Fernet
from Ventana1 import Ui_MainWindow
from PyQt5.QtWidgets import *

class Correr_programa(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encripta.clicked.connect(self.Encriptador)
        self.ui.btn_desencripta.clicked.connect(self.Desencriptador)
    def Encriptador(self):
        texto=self.ui.txt_entrada.text()
        if texto:
            texto=str(texto).strip()
        path = os.getcwdb()
        path = path.decode()
        path = path + '\dato.kydat'
        try:
            file = open(path, 'rb')
            key = file.read()
            file.close()
        except:
            print("no se pudo abrir el documento")
        texto = texto.encode()
        f = Fernet(key)
        encriptado = f.encrypt(texto)
        encriptado = encriptado.decode()
        self.ui.lbl_respuesta.setText(encriptado)
    def Desencriptador(self):
        texto=self.ui.txt_entrada.text()
        if texto:
            texto=str(texto).strip()
        path = os.getcwdb()
        path = path.decode()
        path = path + '\dato.kydat'
        try:
            file = open(path, 'rb')
            key = file.read()
            file.close()
        except:
            print("no se pudo abrir el documento")
        f = Fernet(key)
        texto1 = texto.encode()
        desencriptado = f.decrypt(texto1)
        desencriptado = desencriptado.decode()
        self.ui.lbl_respuesta.setText(desencriptado)
        self.ui.txt_entrada.clear()
### ::::::::::: damos inicio a la aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Correr_programa()
    window.show()
    sys.exit(app.exec_())