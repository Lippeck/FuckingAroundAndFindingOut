def find_best_positions(room_size, object_size):
    room_x, room_y = room_size
    orientations = [object_size, object_size[::-1]]  # Try both orientations
    
    best_positions = []
    max_objects = 0
    
    for obj_x, obj_y in orientations:
        positions = []
        for x in range(0, room_x - obj_x - 1, obj_x + 1):
            for y in range(0, room_y - obj_y - 1, obj_y + 1):
                positions.append((x, y))
        
        if len(positions) > max_objects:
            max_objects = len(positions)
            best_positions = positions
    
    return best_positions

# Example usage
room_size = (10, 10)
object_size = [1, 2]
best_positions = find_best_positions(room_size, object_size)
print(f"The best positions for the objects are at: {best_positions}")
