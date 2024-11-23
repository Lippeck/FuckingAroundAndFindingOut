from input_file_reader import FileHandler
import os

def calculate_task_sums(tasks):
    return [sum(task) for task in tasks]

if __name__ == "__main__":
    input_directory = '40_Drone/level_1'
    output_directory = '40_Drone/level_1/solutions'
    
    file_handler = FileHandler(input_directory)
    file_handler.read_files()
    tasks_dict = file_handler.get_tasks()
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename, tasks in tasks_dict.items():
        task_sums = calculate_task_sums(tasks)
        output_file_path = os.path.join(output_directory, f"{filename}_solution.out")
        file_handler.write_solution_file(task_sums, output_file_path)

