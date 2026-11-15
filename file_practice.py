 #File Operations Practice - v0.1

print("=== FILE PRACTICE ===")
print("Learning file operations!")

# File Operations Practice - v0.2

print("=== FILE PRACTICE ===")
print("Testing WRITE mode")

# Write to a file
with open("output.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is write mode.\n")

print("✓ Data written to output.txt")

# File Operations Practice - v0.3

print("=== FILE PRACTICE ===")

# First, write some data
print("1. Testing WRITE mode")
with open("output.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2.\n")
print("✓ Data written")

# Now read it back
print("\n2. Testing READ mode")
with open("output.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)

# File Operations Practice - v0.4

print("=== FILE PRACTICE ===")

# Write initial data
print("1. Creating file with WRITE mode")
with open("output.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
print("✓ Initial file created")

# Read what we wrote
print("\n2. Reading with READ mode")
with open("output.txt", "r") as file:
    print(file.read())

# Append more data
print("3. Adding more with APPEND mode")
with open("output.txt", "a") as file:
    file.write("Line 3 - appended!\n")
    file.write("Line 4 - appended!\n")
print("✓ Data appended")

# Read again to see all lines
print("\n4. Reading final result")
with open("output.txt", "r") as file:
    print(file.read())