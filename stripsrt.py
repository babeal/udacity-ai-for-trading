import os
import argparse
import re

"""
Removes line b
"""


def is_useless_line(line):
    if line == "":
        return True
    if re.match("^\d*$", line):
        return True
    if re.match("^[\d\d:].*$", line):
        return True
    return False


def transform(file):
    if not os.path.exists(file):
        print(f"{file} not found")
        return

    with open(file, "r") as file_contents:
        lines = file_contents.readlines()
        output_line = ""
        for line in lines:
            line = line.rstrip().lstrip()
            if is_useless_line(line):
                continue
            output_line = f"{output_line} {line}"
            if output_line[-1] in ["?", "."]:
                print(output_line)
                output_line = ""


def main():
    parser = argparse.ArgumentParser(description="Convert srt files to text for note taking")
    parser.add_argument("file", metavar="N", type=str, help="file path")
    args = parser.parse_args()
    transform(args.file)


if __name__ == "__main__":
    main()