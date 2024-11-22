import tkinter as tk
from views.view1 import View1
from views.view2 import View2
from views.view3 import View3
from views.view4 import View4
from views.view5 import View5
from bd.db_setup import DatabaseManager


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nominator")
        self.geometry("1500x800")
        self.resizable(False, False)

        db_manager = DatabaseManager()
        db_manager.create_database()

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (View1, View2, View3, View4, View5):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("View1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()

    app.mainloop()