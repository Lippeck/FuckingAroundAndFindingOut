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

def read_patterns(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n\n')
    patterns = []
    for pattern in lines:
        patterns.append([list(row) for row in pattern.split('\n')])
    return patterns

def do_the_thing1(x, y, z, patterns):
    matrix = [['.' for _ in range(x)] for _ in range(y)]
    desk_count = 1
    split_matrix_into_patterns(matrix, patterns)
    
def split_matrix_into_patterns(matrix, patterns):
    
    


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
    desk_size = [2,1]
    input_dir = 'level_5'
    output_dir = 'level5_answer'
    os.makedirs(output_dir, exist_ok=True)
    
    patterns = read_patterns('patterns.in')
    
    # Print all patterns
    for pattern in patterns:
        print(create_pattern(pattern))
    
    
    for input_file in os.listdir(input_dir):
        if input_file.endswith('.in'):
            input_path = os.path.join(input_dir, input_file)
            tasks = read_input(input_path)
            output_file = f"{os.path.splitext(input_file)[0]}.out"
            output_path = os.path.join(output_dir, output_file)
            with open(output_path, 'w') as output:
                for x, y, z in tasks:
                    solutions = []
                    matrix, desk_count = do_the_thing1(x, y, z,patterns)
                    
                    if desk_count < z:
                        output.write(f"Could not place all desks {z} we placed {desk_count[1]}\n")
                    result = create_pattern(matrix)
                    for row in matrix:
                        output.write(result)
                    output.write('\n')

if __name__ == "__main__":
    main()