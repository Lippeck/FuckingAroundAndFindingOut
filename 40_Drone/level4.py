from input_file_reader import FileHandler3
from drone import Drone, DroneController
import os

def do_the_thing(drone_controller):
    drone_controller.reach_height()
    drone_controller.wait_until_drone_drops()
    drone_controller.land_safely()
    
    #drone.controller.land_safely()
    return drone_controller.get_accelerations_applied()

if __name__ == "__main__":
    input_directory = '40_Drone/level_4'
    output_directory = '40_Drone/level_4/solutions'
    
    file_handler = FileHandler3(input_directory)
    file_handler.read_files()
    tasks_dict = file_handler.get_tasks()
    
    print(tasks_dict)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        
    for filename, tasks in tasks_dict.items():
        solution = []
        for task in tasks:
            x_target = task[0]
            height_target = task[1]
            max_ticks = task[2]
            print(x_target)
            for height in task: 
                drone = Drone(0, 0, 0, 10, 0, 0)
                drone_controller = DroneController(drone, target_height=height, min_acc=0, max_acc=20, max_ticks=0, x_target=x_target)
                accelerations = do_the_thing(drone_controller)
                solution.append(accelerations)
        output_file_path = os.path.join(output_directory, f"{filename}_solution.out")
        #file_handler.write_solution_file(solution, output_file_path)


