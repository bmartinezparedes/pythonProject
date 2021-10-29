
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion:
    def __init__(self):
        wndFiestra=Gtk.Window()
        wndFiestra.set_title("A segunda aplicacion")
        caixaV= Gtk.Box()
        wndFiestra.add(caixaV)
        self.txtNome = Gtk.Entry()
        self.txtNome.set_text("Escribe o teu nome")
        caixaV.pack_end(self.txtNome,True,False,6)
        self.lblTexto=Gtk.Entry()
        self.lblTexto.set_text("Escribe o teu nome")
        caixaV.pack_end(self.lblTexto,True,True,6)
        self.btnSaudo=Gtk.Button()
        self.btnSaudo.set_label("Saudo")
        caixaV.pack_end(self.btnSaudo,False,False,6)
        wndFiestra.show_all()

        sinais = {"on_FiestraPrincipal_destroy": Gtk.main_quit,
                  "on___glade_unnamed_4_activate": self.onBtnSaudoClicked,
                  "on___glade_unnamed_3_clicked": self.ontxtNomeActivated}

    #aqui el boton introduce el nombre en el label
    def onBtnSaudoClicked(self,boton):
        self.introducirNombreEnLabel()

    #aqui el txt introduce el nombre en el label
    def ontxtNomeActivated(self,control):
        self.introducirNombreEnLabel()

    def introducirNombreEnLabel(self):
        nome = self.txtNome.get_text()
        self.lblTexto.set_text("Hola ".upper() + nome.upper())
if __name__=="__main__":
    Aplicacion()
    Gtk.main()