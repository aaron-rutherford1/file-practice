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

    # File Operations Practice - v1.0

print("=== FILE OPERATIONS PRACTICE ===")
print("1. Write mode (overwrites)")
print("2. Append mode (adds to end)")
print("3. Read mode (display file)")

choice = input("\nChoose mode (1-3): ")

if choice == "1":
    text = input("Enter text to write: ")
    with open("test_output.txt", "w") as file:
        file.write(text + "\n")
    print("✓ File written (overwrites old content)")

elif choice == "2":
    text = input("Enter text to append: ")
    with open("test_output.txt", "a") as file:
        file.write(text + "\n")
    print("✓ Text appended (keeps old content)")

elif choice == "3":
    try:
        with open("test_output.txt", "r") as file:
            content = file.read()
        print("\n--- FILE CONTENTS ---")
        print(content)
    except FileNotFoundError:
        print("No file found yet! Use option 1 or 2 first.")

else:
    print("Invalid choice!")