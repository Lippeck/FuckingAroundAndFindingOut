import os
from rectpack import newPacker

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    num_tasks = int(lines[0].strip())
    tasks = []
    for line in lines[1:num_tasks + 1]:
        x, y, z = map(int, line.strip().split())
        tasks.append((x, y, z))
    return tasks

def read_patterns(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n\n')
    patterns = []
    for pattern in lines:
        patterns.append([list(row) for row in pattern.split('\n')])
    return patterns


def do_the_thing(matrix, z, desk_matrix):
    matrix, _ = transpose_matrix_if_longer_then_wide(matrix)
    desk_matrix, _ = transpose_matrix_if_longer_then_wide(desk_matrix)
    desk_size = [len(desk_matrix), len(desk_matrix[0])]
    desk_length = len(desk_matrix[0])
    print(desk_length)
    x,y  = len(matrix[0]), len(matrix)
    desk_count = 0
    i = 0
    while i < y:
        j = 0
        while j < x:
            if desk_count <= z:
                desk_placed = False

                matrix,_, desk_placed1 = try_to_find_suitable_placement(matrix, i, x - j - desk_size[0], transpose_matrix(replace_desk_char(desk_matrix,'2')))
                matrix,_, desk_placed2 = try_to_find_suitable_placement(matrix, y - i - desk_size[1], j, transpose_matrix(replace_desk_char(desk_matrix,'3')))
                desk_count += desk_placed1 + desk_placed2
                
                if not desk_placed1 and not desk_placed2:
                    matrix,_, desk_placed3 = try_to_place_desk(matrix, i, j, replace_desk_char(desk_matrix,'1'))
                    matrix,_, desk_placed4 = try_to_place_desk(matrix, y - i - desk_size[0], x - j - desk_size[1], replace_desk_char(desk_matrix, '4'))
                    desk_count += desk_placed3 + desk_placed4
                
            j += 1
        i += 1
    #matrix = transpose_matrix(matrix) if flipped else matrix
    return matrix, desk_count

def try_to_find_suitable_placement(matrix, i, j, desk_matrix):
    if get_amount_of_specific_char(matrix, '.', 'row', i) % len(desk_matrix[0]) == 0 and get_amount_of_specific_char(matrix, '.', 'column', j) % len(desk_matrix) == 0:
        return try_to_place_desk(matrix, i, j, desk_matrix)
    return matrix, j, False
    
def get_amount_of_specific_char(matrix, char, axis, index):
    count = 0
    if axis == 'row':
        count = matrix[index].count(char)
    elif axis == 'column':
        count = sum(1 for row in matrix if row[index] == char)
    return count

def replace_desk_char(desk_matrix, new_char):
    return [[new_char if cell == 'X' else cell for cell in row] for row in desk_matrix]    
    return desk_matrix

def transpose_matrix_if_longer_then_wide(matrix):
    if len(matrix) > len(matrix[0]):
        return transpose_matrix(matrix), True
    return matrix, False
int
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def try_to_place_desk(matrix, i, j, desk_matrix):
    desk_size = [len(desk_matrix), len(desk_matrix[0])]
    desk_placed = False
    if j + desk_size[1] <= len(matrix[0]) and i + desk_size[0] <= len(matrix) and not deskDoesCollide(matrix, i, j, desk_size):
        for x in range(desk_size[1]):
            for y in range(desk_size[0]):
                matrix[i + y][j + x] = desk_matrix[y][x]
        desk_placed = True
        j += desk_size[1] - 1
    return matrix, j, desk_placed

def deskDoesCollide(matrix, i, j, desk_placement):
    for y in range(desk_placement[0]):
        for x in range(desk_placement[1]):
            if (i + y < 0 or j + x < 0) or (i + y >= len(matrix) or j + x >= len(matrix[0])):
                continue
            if matrix[i+y][j+x] != '.':
                return True
    return False

def print_matrix(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(''.join(row) + '\n')

def create_pattern(pattern):
    result = ""
    for row in pattern:
        result += ''.join(row) + '\n'
    return result

def main():
    desk_matrix = [["X","X","0"],
                   ["0","0","0"]]
    #input_dir = 'debug'
    input_dir = 'debug'
    output_dir = 'level5_answer'
    os.makedirs(output_dir, exist_ok=True)
    
    for input_file in os.listdir(input_dir):
        if input_file.endswith('.in'):
            input_path = os.path.join(input_dir, input_file)
            tasks = read_input(input_path)
            output_file = f"{os.path.splitext(input_file)[0]}.out"
            output_path = os.path.join(output_dir, output_file)
            with open(output_path, 'w') as output:
                for x, y, z in tasks:
                    matrix = [['.' for _ in range(x+1)] for _ in range(y+1)]
                    matrix, desk_count = do_the_thing(matrix , z, desk_matrix)
                    #rint(len(matrix), len(matrix[0]), z)
                    if desk_count < z:
                        output.write(f"Could not place all desks {z} for Matrix {len(matrix[0])}x{len(matrix)} we placed {desk_count}\n")
                    result = create_pattern(matrix)
                    output.write(result)
                    output.write('\n')

if __name__ == "__main__":
    main()