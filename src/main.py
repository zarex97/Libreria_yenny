import tkinter as tk

from src.ui.Abm_usuarios.abm_usuarios import ABMUsuariosFrame
from src.ui.pedidos import PedidosFrame
from src.ui.productos import ProductosFrame
from ui.login import LoginFrame
from ui.adminpanel import AdminFrame
from ui.registro import RegistroFrame
from src.ui.Abm_libros.abm_libros import ABMLibrosFrame


def show_frame(frame):
    frame.tkraise()


def on_login_success(user):
    root.current_user = user
    root.admin_frame = AdminFrame(root, show_frame, user)
    root.admin_frame.grid(row=0, column=0, sticky='nsew', in_=root)

    root.productos_frame = ProductosFrame(root, show_frame, user)
    root.productos_frame.grid(row=0, column=0, sticky='nsew', in_=root)

    root.pedidos_frame = PedidosFrame(root, show_frame, user)
    root.pedidos_frame.grid(row=0, column=0, sticky='nsew', in_=root)

    show_frame(root.admin_frame)


root = tk.Tk()
root.title("Aplicación")
root.geometry("800x600")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

login_frame = LoginFrame(root, show_frame, on_login_success)
registro_frame = RegistroFrame(root, show_frame, on_login_success)
abm_libros_frame = ABMLibrosFrame(root, show_frame)
abm_usuarios_frame = ABMUsuariosFrame(root, show_frame)

login_frame.grid(row=0, column=0, sticky='nsew', in_=root)
registro_frame.grid(row=0, column=0, sticky='nsew', in_=root)
abm_libros_frame.grid(row=0, column=0, sticky='nsew', in_=root)
abm_usuarios_frame.grid(row=0, column=0, sticky='nsew', in_=root)

show_frame(login_frame)

root.mainloop()
