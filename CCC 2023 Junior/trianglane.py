c = int(input())
first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))

wet_areas = 0
tape_length = 0

for i in range(c):
    # Check if the current tile and its adjacent tile form a wet area
    if first_row[i] == 1:
        wet_areas += 1
        tape_length += 2  # Add 2 meters for the two sides of the current tile

        # Check if the wet area extends to the second row
        if i > 0 and second_row[i - 1] == 1:
            tape_length -= 1  # Subtract 1 meter for the shared side between two adjacent wet tiles in different rows
        if i < c - 1 and second_row[i] == 1:
            tape_length -= 1  # Subtract 1 meter for the shared side between two adjacent wet tiles in different rows

print(tape_length)