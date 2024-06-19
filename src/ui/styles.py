import tkinter as tk

def apply_styles(widget):
    if isinstance(widget, tk.Tk) or isinstance(widget, tk.Frame):
        widget.config(bg="#00883E")  # Aplicar el fondo verde a la ventana principal y a los frames
    for child in widget.winfo_children():
        apply_styles(child)