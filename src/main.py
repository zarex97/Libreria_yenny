import tkinter as tk
from ui.login import LoginFrame
from ui.admin import AdminFrame
from ui.registro import RegistroFrame
from ui.pedidos import PedidosFrame
from ui.productos import ProductosFrame
from ui.agregar import AgregarFrame


def show_frame(frame):
    frame.tkraise()  


root = tk.Tk()
root.title("Aplicación")
root.geometry("800x600")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

login_frame = LoginFrame(root, show_frame)
admin_frame = AdminFrame(root, show_frame)
registro_frame = RegistroFrame(root, show_frame)
pedidos_frame = PedidosFrame(root, show_frame)
productos_frame = ProductosFrame(root, show_frame)
agregar_frame = AgregarFrame(root, show_frame)


login_frame.grid(row=0, column=0, sticky='nsew', in_=root)
admin_frame.grid(row=0, column=0, sticky='nsew', in_=root)
registro_frame.grid(row=0, column=0, sticky='nsew', in_=root)
pedidos_frame.grid(row=0, column=0, sticky='nsew', in_=root)
productos_frame.grid(row=0, column=0, sticky='nsew', in_=root)

show_frame(login_frame)

root.mainloop()
