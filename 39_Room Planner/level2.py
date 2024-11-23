import os

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    num_tasks = int(lines[0].strip())
    tasks = []
    for line in lines[1:num_tasks + 1]:
        x, y, z = map(int, line.strip().split())
        tasks.append((x, y, z))
    return tasks

def place_desks(x, y, z):
    matrix = [['.' for _ in range(x)] for _ in range(y)]
    desk_count = 0
    for i in range(y):
        for j in range(0, x - 2, 3):
            if desk_count < z:
                desk_count += 1
                desk_str = str(desk_count)
                matrix[i][j] = desk_str
                matrix[i][j + 1] = desk_str
                matrix[i][j + 2] = desk_str
    return matrix


def print_matrix(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(row) + '\n')

def main():
    input_dir = 'level_2'
    output_dir = 'level2_answer'
    os.makedirs(output_dir, exist_ok=True)
    
    for input_file in os.listdir(input_dir):
        if input_file.endswith('.in'):
            input_path = os.path.join(input_dir, input_file)
            tasks = read_input(input_path)
            output_file = f"{os.path.splitext(input_file)[0]}.out"
            output_path = os.path.join(output_dir, output_file)
            with open(output_path, 'w') as output:
                for x, y, z in tasks:
                    matrix = place_desks(x, y, z)
                    for row in matrix:
                        output.write(' '.join(row) + '\n')
                    output.write('\n')

if __name__ == "__main__":
    main()