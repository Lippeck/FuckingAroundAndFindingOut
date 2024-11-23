import os

def process_tasks(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    num_tasks = int(lines[0].strip())
    results = []
    
    for i in range(1, num_tasks + 1):
        x, y = map(int, lines[i].strip().split())
        result = int((x / 3) * y)
        results.append(result)
    
    with open(output_file, 'w') as outfile:
        for result in results:
            outfile.write(f"{result}\n")

def process_all_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.in'):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace('.in', '.out'))
            process_tasks(input_file, output_file)

if __name__ == "__main__":
    process_all_files('level_1', 'level1_answer')