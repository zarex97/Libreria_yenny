import tkinter as tk
from ui.login import LoginFrame
from ui.adminpanel import AdminFrame
from ui.registro import RegistroFrame
from ui.pedidos import PedidosFrame
from ui.productos import ProductosFrame
from ui.gestor import GestorFrame

# Configurar la aplicación tkinter
root = tk.Tk()
root.title("Aplicación de Gestión")
root.geometry("800x600")

# Función para cambiar de frame
def show_frame(frame):
    frame.tkraise()

# Crear y configurar los diferentes frames
login_frame = LoginFrame(root, lambda: show_frame(admin_frame))
admin_frame = AdminFrame(root, lambda: show_frame(gestor_frame))
registro_frame = RegistroFrame(root, lambda: show_frame(productos_frame))
pedidos_frame = PedidosFrame(root, lambda: show_frame(admin_frame))
productos_frame = ProductosFrame(root, lambda: show_frame(gestor_frame))  # Pasar lambda para cambiar de frame
gestor_frame = GestorFrame(root)  # Solo parent como argumento

# Mostrar el frame inicial
login_frame.grid(row=0, column=0, sticky='nsew')

# Asociar función de cambio de frame a cada frame que lo necesite
login_frame.show_frame = lambda: show_frame(admin_frame)
admin_frame.show_frame = lambda: show_frame(gestor_frame)
registro_frame.show_frame = lambda: show_frame(productos_frame)
pedidos_frame.show_frame = lambda: show_frame(admin_frame)
productos_frame.show_frame = lambda: show_frame(gestor_frame)

# Iniciar la aplicación
root.mainloop()
