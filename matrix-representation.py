import tkinter as tk

class Game:
    def __init__(self, size):
        self.size = size
        self.root = tk.Tk()
        self.root.title("Game")
        self.root.geometry("800x800")
        self.root.resizable(False, False)
        # Initialize matrix as a list of lists containing labels
        self.matrix = [[None for _ in range(size)] for _ in range(size)]

    def add_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                # Create Label, set initial number, place on grid, and assign to matrix directly
                label = tk.Label(self.root, text=str(i * self.size + j + 1), width=5, font=('Arial', 60), borderwidth=2, relief="groove")
                label.grid(row=i, column=j, padx=30, pady=30)
                self.matrix[i][j] = label

    def run(self):
        self.add_matrix()  # Populate the matrix with Label widgets before starting the main loop
        self.root.mainloop()


if __name__ == "__main__":
    game = Game(3)
    game.run()
