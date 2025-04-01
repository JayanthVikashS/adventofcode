# Day 1: Sonar Sweep-Part_1

# Read the sonar sweep report from the puzzle input file
with open("input.txt") as sonar_report_file:
    seafloor_depth_readings = [int(line.strip()) for line in sonar_report_file.readlines()]

# Initialize the counter to track depth that increases
num_times_depth_increased = 0

# Compare each and every depth measurement with the previous one
for i in range(1, len(seafloor_depth_readings)):
    current_depth = seafloor_depth_readings[i]
    previous_depth = seafloor_depth_readings[i - 1]

    if current_depth > previous_depth:
        num_times_depth_increased += 1

# For displaying the final count of increases
print("Number of times the depth increased:", num_times_depth_increased)
