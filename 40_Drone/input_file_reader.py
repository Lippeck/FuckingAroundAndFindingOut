import os

class FileHandler:
    def __init__(self, directory_path):
        self.directory_path = os.path.abspath(directory_path)
        self.tasks = {}

    def read_files(self):
        if not os.path.isdir(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            if os.path.isfile(file_path):
                self.read_file(file_path, filename)

    def read_file(self, file_path, filename):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_tasks = int(lines[0].strip())
            self.tasks[filename] = [list(map(int, line.strip().split())) for line in lines[1:num_tasks + 1]]

    def get_tasks(self):
        return self.tasks
    
    def write_solution_file(self, task_sums, output_file_path):
        with open(output_file_path, 'w') as file:
            for task_sum in task_sums:
                file.write(f"{task_sum}\n")
                
                
class FileHandler2:
    
    def __init__(self, directory_path):
        self.directory_path = os.path.abspath(directory_path)
        self.tasks = {}
        self.max_ticks = {}

    def read_files(self):
        if not os.path.isdir(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            if os.path.isfile(file_path):
                self.read_file(file_path, filename)

    def read_file(self, file_path, filename):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_tasks = int(lines[0].strip())
            max_ticks = int(lines[1].strip())
            self.max_ticks[filename] = max_ticks
            self.tasks[filename] = [list(map(int, line.strip().split())) for line in lines[2:num_tasks + 2]]

    def get_tasks(self):
        return self.tasks
    
    def get_max_ticks(self):
        return self.max_ticks
    
    def write_solution_file(self, solutions, output_file_path):
        with open(output_file_path, 'w') as file:
            for sol in solutions:
                file.write(" ".join(map(str, sol)) + "\n")

import os

class FileHandler3:
    def __init__(self, directory_path):
        self.directory_path = os.path.abspath(directory_path)
        self.tasks = {}

    def read_files(self):
        if not os.path.isdir(self.directory_path):
            raise FileNotFoundError(f"Directory not found: {self.directory_path}")
        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)
            if os.path.isfile(file_path):
                self.read_file(file_path, filename)

    def read_file(self, file_path, filename):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_tasks = int(lines[0].strip())
            self.tasks[filename] = [list(map(int, line.strip().split())) for line in lines[1:num_tasks + 1]]

    def get_tasks(self):
        return self.tasks
    
    def write_solution_file(self, solutions, output_file_path):
        with open(output_file_path, 'w') as file:
            for sol in solutions:
                file.write(" ".join(map(str, f"{sol[0]},{sol[1]}")) + "\n")