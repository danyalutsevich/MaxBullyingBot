import os

def main():
    # Get the file name
    filename = input("Enter the file name: ").strip()

    # Check if file exists
    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        exit()

    # Open file for appending
    infile = open(filename, "a")

    # Add words to the file
    while True:
        
        word = input("Enter a word (<Enter> to quit): ").strip()
        if len(word) == 0:
            break
        infile.write(word + "")

    infile.close()