import tkinter as tk
from tkinter import ttk, messagebox
from src.models.bookOrder import *
from src.ui.styles import apply_styles, RoundedButton

class PedidosFrame(tk.Frame):
    def __init__(self, parent, show_frame, user_id, role_id):
        super().__init__(parent)
        self.show_frame = show_frame
        self.user_id = user_id
        self.role_id = role_id
        self.create_widgets()
        apply_styles(self)

    def create_widgets(self):
        tk.Label(self, text="Pedidos", font=("Helvetica", 24, "bold")).pack(pady=20)

        self.pedido_listbox = tk.Listbox(self, font=("Helvetica", 12), height=10)
        self.pedido_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.update_orders()

        RoundedButton(self, text="Ver detalles", command=self.show_order_details, width=180, height=60, radius=30, bg='white', fg='#013220').pack(pady=10)
        if self.role_id == 1 :
            RoundedButton(self, text="Envio hecho", command=self.cancel_order, width=180, height=60, radius=30, bg='white', fg='#013220').pack(pady=10)
        elif self.role_id == 2 :
            RoundedButton(self, text="Envio hecho", command=self.cancel_order, width=180, height=60, radius=30, bg='white', fg='#013220').pack(pady=10)
              
        elif self.role_id == 3:
            RoundedButton(self, text="Cancelar pedido", command=self.cancel_order, width=180, height=60, radius=30, bg='white', fg='#013220').pack(pady=10)

        
        RoundedButton(self, text="Volver atrás", command=self.back, width=180, height=60, radius=30, bg='white', fg='#013220').pack(pady=10)

    def update_orders(self):
        self.pedido_listbox.delete(0, tk.END)

        orders = get_order(self.user_id, self.role_id)

        for order in orders:
            order_text = f"Pedido #{order[0]} - Usuario: {order[1]}, Fecha: {order[2]}, Valor: {order[3]}"
            self.pedido_listbox.insert(tk.END, order_text)

    def show_order_details(self):
        selected_order_index = self.pedido_listbox.curselection()
        if not selected_order_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un pedido de la lista")
            return

        selected_order_id = self.pedido_listbox.get(selected_order_index).split()[1][1:]
        order_details = get_order_details(selected_order_id)

        if not order_details:
            messagebox.showerror("Error", "No se encontraron detalles para el pedido seleccionado")
            return

        details_window = tk.Toplevel(self)
        details_window.title(f"Detalles del Pedido #{selected_order_id}")
        details_window.geometry("400x300")

        tk.Label(details_window, text=f"Detalles del Pedido #{selected_order_id}", font=("Helvetica", 16, "bold")).pack(pady=10)

        details_listbox = tk.Listbox(details_window, font=("Helvetica", 12), height=10)
        details_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        for detail in order_details:
            if len(detail) != 3:
                messagebox.showerror("Error", f"Formato inesperado de detalles del pedido: {detail}")
                continue
            detail_text = f"Libro: {detail[0]}, Cantidad: {detail[1]}, Precio: ${detail[2]:.2f}"
            details_listbox.insert(tk.END, detail_text)

    def cancel_order(self):
        selected_order_index = self.pedido_listbox.curselection()
        if not selected_order_index:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un pedido de la lista")
            return

        selected_order_id = self.pedido_listbox.get(selected_order_index).split()[1][1:]

        cancel_result = cancel_order(selected_order_id)
        
        if self.role_id == 1:
            if cancel_result:
                messagebox.showinfo("Pedido completado", f"El pedido #{selected_order_id} ha sido completado")
                self.update_orders()
            else:
                messagebox.showerror("Error", f"No se pudo completar el pedido #{selected_order_id}")        
        elif self.role_id == 2:
            if cancel_result:
                messagebox.showinfo("Pedido completado", f"El pedido #{selected_order_id} ha sido completado")
                self.update_orders()
            else:
                messagebox.showerror("Error", f"No se pudo completar el pedido #{selected_order_id}")    
        elif self.role_id == 3:
            if cancel_result:
                messagebox.showinfo("Pedido cancelado", f"El pedido #{selected_order_id} ha sido cancelado")
                self.update_orders()
            else:
                messagebox.showerror("Error", f"No se pudo cancelar el pedido #{selected_order_id}")  
        

                
                

    def back(self):
        self.show_frame(self.master.children["!adminframe"])

def cancel_order(order_id):
    
    try:
       
        delete_order(order_id)
        return True
    except Exception as e:
        print(f"Error al cancelar el pedido: {e}")
        return False
