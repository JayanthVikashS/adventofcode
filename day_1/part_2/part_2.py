#  Day 1: Sonar Sweep -Part_2

# Read the sonar sweep report from the puzzle input file
with open("input.txt") as sonar_report_file:
    seafloor_depth_readings = [int(line.strip()) for line in sonar_report_file.readlines()]

# Initialize the counter for sliding window increases
num_times_window_sum_increased = 0

# Loop through the list using a sliding window of size 3
for i in range(len(seafloor_depth_readings) - 3):
    first_window_sum = sum(seafloor_depth_readings[i:i+3])
    second_window_sum = sum(seafloor_depth_readings[i+1:i+4])

    if second_window_sum > first_window_sum:
        num_times_window_sum_increased += 1

# For displaying the final count of increases
print("Number of times the 3-measurement sliding window sum increased:", num_times_window_sum_increased)
