import tkinter as tk
import time

class TimeCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Counter")

        
        self.problems = 0

        with open("count.txt") as f: 
            first_char = f.read(1)

            if not first_char:
                self.counter = 0
                self.minutes = 0
                self.hours = 0
                #self.problems = 0
            else:
                self.counter, self.minutes,self.hours = [int(num) for line in f for num in line.split(",")]
                #TO DO read and update problems solved
                #self.problems = f.readlines()[2]

        self.running = False
        
        self.label = tk.Label(root, text="Time: hours: "+ str(self.hours) +" minutes: " + str(self.minutes) + " seconds: "+str(self.counter), font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.labelproblem = tk.Label(root, text="Leetcode problems Solved: "+ str(self.problems), font=("Helvetica", 24))
        self.labelproblem.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.solved_button = tk.Button(root, text="Solved", command=self.solved)
        self.solved_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.update_time()

    def update_time(self):
        if self.running:
            self.counter += 1
            if self.counter > 59:
                self.minutes += 1
                self.counter = 0
            if self.minutes > 59:
                self.hours += 1
                self.minutes = 0
            self.label.config(text=f"Time: hours: {self.hours} minutes: {self.minutes} seconds: {self.counter}")
        self.labelproblem.config(text=f"Leetcode problems Solved: {self.problems}")
        self.root.after(1000, self.update_time)  # Update every second

    def start(self):
        """
        Starts the time counter if it is not already running
        """
        self.running = True
    
    def solved(self):
        self.problems += 1 
    def stop(self):
        with open("count.txt","w") as f: #in write mode
            f.write(",{},{},{}".format(self.counter, self.minutes, self.hours))
        self.running = False

    def reset(self):
        self.running = False
        self.counter = 0
        self.label.config(text="Time: 0")

if __name__ == "__main__":
    root = tk.Tk()
    time_counter = TimeCounter(root)
    root.mainloop()