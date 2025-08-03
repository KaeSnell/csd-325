# Mikaela Snell
# August 2nd, 2025
# Assignment 10.2 GUI ToDo
# This program modifies the Tkinter ToDo program
# Python Tkinter By Example (Love, github.com, 2018)


import tkinter as tk
import tkinter.messagebox as msg
from tkinter import Menu

class Todo(tk.Tk):
      def __init__(self, tasks=None):
          super().__init__()

          if not tasks:
              self.tasks = []
          else:
              self.tasks = tasks

          self.tasks_canvas = tk.Canvas(self, bg = "white")

          self.tasks_frame = tk.Frame(self.tasks_canvas)
          self.text_frame = tk.Frame(self)

          self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

          self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

          # Changed the title of the window
          self.title("Snell-ToDo")
          self.geometry("300x400")

          self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

          self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
          self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

          self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

          self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
          self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
          self.menu()
          self.task_create.focus_set()
          
        
          # Changed the label to provide instructions
          todo1 = tk.Label(self.tasks_frame, text="-- Right Click Tasks to Delete Them --", bg="pale green", fg="sea green", pady=10)
          # Changed the delete button to a right click
          todo1.bind("<Button-3>", self.remove_task)

          self.tasks.append(todo1)

          for task in self.tasks:
              task.pack(side=tk.TOP, fill=tk.X)

          self.bind("<Return>", self.add_task)
          self.bind("<Configure>", self.on_frame_configure)
          self.bind_all("<MouseWheel>", self.mouse_scroll)
          self.bind_all("<Button-4>", self.mouse_scroll)
          self.bind_all("<Button-5>", self.mouse_scroll)
          self.tasks_canvas.bind("<Configure>", self.task_width)

          # Changed the colour schemes
          self.colour_schemes = [{"bg": "pale green", "fg": "sea green"}, {"bg": "orchid1", "fg": "DarkOrchid4"}]

      def add_task(self, event=None):
          task_text = self.task_create.get(1.0,tk.END).strip()

          if len(task_text) > 0:
              new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

              self.set_task_colour(len(self.tasks), new_task)
            
              # Changed the delete button to a right click
              new_task.bind("<Button-3>", self.remove_task)
              new_task.pack(side=tk.TOP, fill=tk.X)

              self.tasks.append(new_task)

          self.task_create.delete(1.0, tk.END)

      def remove_task(self, event):
          task = event.widget
          if msg.askyesno('Really Delete?', 'Delete "' + task.cget("text") + '"?'):
              self.tasks.remove(event.widget)
              event.widget.destroy()
              self.recolour_tasks()

      def recolour_tasks(self):
          for index, task in enumerate(self.tasks):
              self.set_task_colour(index, task)

      def set_task_colour(self, position, task):
          _, task_style_choice = divmod(position, 2)

          my_scheme_choice = self.colour_schemes[task_style_choice]

          task.configure(bg=my_scheme_choice["bg"])
          task.configure(fg=my_scheme_choice["fg"])

      def on_frame_configure(self, event=None):
          self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

      def task_width(self, event):
          canvas_width = event.width
          self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

      def mouse_scroll(self, event):
          if event.delta:
              self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
          else:
              if event.num == 5:
                  move = 1
              else:
                  move = -1

              self.tasks_canvas.yview_scroll(move, "units")

      # Added a menu bar with an exit option
      def menu(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.confirm_exit)

      # Added a confirm exit function
      def confirm_exit(self):
        if msg.askyesno("Exit", "Are you sure you want to quit this program?"):
          self.destroy()

if __name__ == "__main__":
      todo = Todo()
      todo.mainloop()