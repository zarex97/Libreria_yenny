import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=180, height=40, radius=20, bg='#013220', fg='white', font=("Helvetica", 12, "bold"), **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, bg=parent['bg'], highlightthickness=0, **kwargs)
        self.command = command
        self.bg = bg
        self.fg = fg
        self.font = font
        self.text = text
        self.radius = radius

        self.create_rounded_rectangle(0, 0, width, height, radius, fill=self.bg)
        self.create_text(width//2, height//2, text=self.text, fill=self.fg, font=self.font)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def create_rounded_rectangle(self, x1, y1, x2, y2, r=25, **kwargs):
        points = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

    def _on_press(self, event):
        self.create_rounded_rectangle(0, 0, self.winfo_width(), self.winfo_height(), self.radius, fill="#013220")
        self.create_text(self.winfo_width()//2, self.winfo_height()//2, text=self.text, fill=self.fg, font=self.font)

    def _on_release(self, event):
        self.create_rounded_rectangle(0, 0, self.winfo_width(), self.winfo_height(), self.radius, fill=self.bg)
        self.create_text(self.winfo_width()//2, self.winfo_height()//2, text=self.text, fill=self.fg, font=self.font)
        if self.command:
            self.command()

def apply_styles(frame):
    frame.configure(bg='#013220')  
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(bg='#013220', fg='#ffffff', font=("Helvetica", 12))
        elif isinstance(widget, tk.Entry):
            widget.configure(bg='white', fg='black', font=("Helvetica", 12), relief='flat', bd=5, highlightthickness=0, insertbackground='black')
            widget.bind("<FocusIn>", lambda e: widget.configure(relief='solid', highlightbackground='#013220', highlightcolor='#013220'))
            widget.bind("<FocusOut>", lambda e: widget.configure(relief='flat'))
        elif isinstance(widget, tk.Frame):
            apply_styles(widget)
