import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Six Axis Robot Arm")
        self.geometry("500x800")
        self.configure(bg='#620A71')
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create the title label
        title_label = tk.Label(self, text="Six Axis Robot Arm", font=("Helvetica", 30, "bold"), fg="#4B0082", bg='#620A71')  # Using a color code for "deep purple"
        title_label.pack(pady=20)
        
        # Create the slider containers
        for i in range(1, 7):
            self.create_slider_container(i)
        
        # Create the serial communication button
        serial_button = tk.Button(self, text="Serial Communication", command=self.open_serial_communication)
        serial_button.pack(pady=20)
    
    def create_slider_container(self, index):
        frame = tk.Frame(self, bg='#D4AFEE', bd=5, relief='ridge')
        frame.pack(pady=10, padx=20, fill='x')
        
        label = tk.Label(frame, text=f"Motor {index} with Control", font=("Helvetica", 18, "bold"), fg="#4B0082", bg='#D4AFEE')  # Using a color code for "deep purple"
        label.pack(pady=10)
        
        slider = ttk.Scale(frame, from_=0, to=100, orient='horizontal')
        slider.pack(pady=10, padx=20, fill='x')
    
    def open_serial_communication(self):
        # Function to handle serial communication
        print("Serial Communication Button Pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()
