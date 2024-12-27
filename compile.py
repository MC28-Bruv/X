import sys
import os

# Check if a text file was provided
if len(sys.argv) != 2:
    print("Please provide a text file to display.")
    sys.exit(1)

# Get the text file path
text_file_path = sys.argv[1]

# Read the content of the text file
with open(text_file_path, 'r', encoding='utf-8') as text_file:
    content = text_file.read()

# Display the content in the console
print(content)

# Function to convert string to binary
def string_to_binary(s):
    return ' '.join(format(ord(char), '08b') for char in s)

# Convert the content to binary
binary_content = string_to_binary(content)

# Save the binary content to a file with the same name but with .x extension in the same folder
binary_file_path = os.path.splitext(text_file_path)[0] + '.x'
with open(binary_file_path, 'w', encoding='utf-8') as binary_file:
    binary_file.write(binary_content)

print(f"The content of {os.path.basename(text_file_path)} has been converted and saved to {os.path.basename(binary_file_path)}")
