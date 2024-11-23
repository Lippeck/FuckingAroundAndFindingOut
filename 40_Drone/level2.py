from input_file_reader import FileHandler
from drone import Drone
import os

def do_the_thing(drone, task):
    for acc in task:
        if isinstance(acc, list):
            acc = sum(acc)
        drone.set_acc(acc)
        drone.fly()
    return drone.height

if __name__ == "__main__":
    input_directory = '40_Drone/level_2'
    output_directory = '40_Drone/level_2/solutions'
    
    file_handler = FileHandler(input_directory)
    file_handler.read_files()
    tasks_dict = file_handler.get_tasks()
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for filename, tasks in tasks_dict.items():
        
        solution = []
        for task in tasks:
            drone = Drone(0, 0)
            height = do_the_thing(drone, task)
            solution.append(height)
        output_file_path = os.path.join(output_directory, f"{filename}_solution.out")
        file_handler.write_solution_file(solution, output_file_path)
