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

def place_desks(x, y, z, desk_size):
    matrix = [['0' for _ in range(x)] for _ in range(y)]
    desk_count = 1
    i = 0
    while i < y:
        j = 0
        while j < x:
            if desk_count <= z:
                desk_str = str(desk_count)
                matrix, j, desk_count = place_desk(matrix, i,j,desk_size, desk_str, desk_count)
            j += 1
        i += 1
    return matrix

def place_desk(matrix, i, j, desk_size, desk_str, desk_count):
    if j + desk_size[0] <= len(matrix[0]):
        matrix[i][j] = desk_str
        matrix[i][j + 1] = desk_str
        matrix[i][j + 2] = desk_str
        j = j + desk_size[0] - 1
        desk_count += 1
    elif j + desk_size[1] <= len(matrix[0]) and i + desk_size[0] <= len(matrix) and matrix[i][j] == '0' and matrix[i + 1][j] == '0' and matrix[i + 2][j] == '0':
        matrix[i][j] = desk_str
        matrix[i + 1][j] = desk_str
        matrix[i + 2][j] = desk_str
        j = j + desk_size[1] - 1
        desk_count += 1
    return matrix, j, desk_count

def print_matrix(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(' '.join(row) + '\n')

def main():
    desk_size = [3,1]
    input_dir = 'level_3'
    output_dir = 'level3_answer'
    os.makedirs(output_dir, exist_ok=True)
    
    for input_file in os.listdir(input_dir):
        if input_file.endswith('.in'):
            input_path = os.path.join(input_dir, input_file)
            tasks = read_input(input_path)
            output_file = f"{os.path.splitext(input_file)[0]}.out"
            output_path = os.path.join(output_dir, output_file)
            with open(output_path, 'w') as output:
                for x, y, z in tasks:
                    matrix = place_desks(x, y, z, desk_size)
                    for row in matrix:
                        output.write(' '.join(row) + '\n')
                    output.write('\n')

if __name__ == "__main__":
    main()