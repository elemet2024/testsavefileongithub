# counter.py

# File to store the counter
counter_file = "loop_counter.txt"

# Function to read the counter from the file
def read_counter():
    try:
        with open(counter_file, "r") as f:
            content = f.read().strip()
            if content:  # Check if the file contains valid content
                return int(content)  # Convert content to integer
            else:
                return 0  # Default to 0 if file is empty
    except (FileNotFoundError, ValueError):
        return 0  # Default to 0 if file doesn't exist or has invalid content

# Function to write the counter to the file
def write_counter(count):
    with open(counter_file, "w") as f:
        f.write(str(count))

# Read the current total count from the file
current_total_count = read_counter()

# Add the loop count (1 to 7) to the current total count
for i in range(1, 8):
    print(f"Loop Count: {i}")
    current_total_count += 1

# Save the updated total count in the file
write_counter(current_total_count)

print(f"The total count after this run is {current_total_count} and saved in {counter_file}.")
