import os
import argparse
import re

"""
Removes use less lines from the .stl text files and reforms sentences. 
This saves time in taking notes as you can focus on adding snap shots and your 
interpretation while saving the exact english used by the presenter
"""

current_dir = os.path.dirname(os.path.realpath(__file__))


def is_useless_line(line):
    if line == "":
        return True
    if re.match("^\d*$", line):
        return True
    if re.match("^[\d\d:].*$", line):
        return True
    return False


def transform(folder):
    if not os.path.exists(folder):
        print(f"{folder} not found")
        return

    for file in os.listdir(folder):
        _, file_extension = os.path.splitext(file)
        if file_extension != ".srt":
            continue
        file_path = os.path.join(folder, file)
        print(f"Opening {file_path}")
        with open(os.path.join(folder, file), "r") as file_contents:
            with open(os.path.join(current_dir, "temp", file), "w") as writer:
                lines = file_contents.readlines()
                output_line = ""
                for line in lines:
                    line = line.rstrip().lstrip()
                    if is_useless_line(line):
                        continue
                    output_line = f"{output_line} {line}"
                    if output_line[-1] in ["?", "."]:
                        writer.write(output_line.lstrip() + "\n")
                        # print(output_line.lstrip())
                        output_line = ""


def main():
    parser = argparse.ArgumentParser(description="Convert srt files to text for note taking")
    parser.add_argument("folder", metavar="N", type=str, help="file path")
    args = parser.parse_args()
    transform(args.folder)


if __name__ == "__main__":
    main()