def generate_building_pattern(height):
    max_width = len(bin(height)) - 2
    for i in range(height+1):
        binary_number = format(i, 'b')
        print(f"{' ' * (max_width - len(binary_number))}{binary_number}")

# Input
height = int(input())

# Generate building pattern with binary numbers
generate_building_pattern(height)
