
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Aplicacion:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("saudo.glade")

        fiestra=builder.get_object("FiestraPrincipal")
        self.txtNome = builder.get_object("txtNome")
        self.btnSaudo=builder.get_object("btnSaudo")
        self.lblTexto =builder.get_object("lblTexto")

        sinais = {"on_FiestraPrincipal_destroy": Gtk.main_quit,
                  "on___glade_unnamed_4_activate": self.onBtnSaudoClicked,
                  "on___glade_unnamed_3_clicked": self.ontxtNomeActivated}
        builder.connect_signals(sinais)
        fiestra.show_all()
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