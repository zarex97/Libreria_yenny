import tkinter as tk
from tkinter import ttk

def apply_styles(widget):
    """Applies general styles to the given widget and its children."""
    for child in widget.winfo_children():
        if isinstance(child, (tk.Label, tk.Button)):
            child.config(
                font=("Helvetica", 12),
                bg="#f2f2f2",
                fg="#333333"
            )
        if isinstance(child, tk.Entry):
            child.config(
                font=("Helvetica", 12),
                bg="#ffffff",
                fg="#333333",
                bd=2,
                relief="groove"
            )
        if isinstance(child, tk.Frame):
            child.config(
                bg="#f2f2f2"
            )
        apply_styles(child)
