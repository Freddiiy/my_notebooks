import argparse
import os.path
from os import listdir, walk


# 02 exercise 1
def print_file_content(file: str):
    with open(file) as f:
        for line in f:
            print(line)


def write_list_to_file(filename: str, text):
    with open(filename, "a") as file_obj:
        for word in text:
            file_obj.write(f"{word}\n")
            print(f"wrote {word} to file.")


def write_args_to_file(filename: str, *args):
    buffer = [i for i in args]
    write_list_to_file(filename, buffer)


def read_csv(input_file: str):
    buffer = ""
    with open(input_file, "r") as csv_file:
        for line in csv_file:
            buffer += f"{line}\n"
    return buffer


def write_csv(content, filename: str = "textfile.txt"):
    with open(filename, "w") as csv_file:
        csv_file.write(content)


def read_csv_cli():
    parser = argparse.ArgumentParser(description="A function that reads a csv file.")
    parser.add_argument("csv", help="Input the file.")
    parser.add_argument("--file", help="The file the data gets dumped to")
    args = parser.parse_args()
    csv_file = args.csv
    if not csv_file:
        csv_file = "../../data/employees.csv"

    file = args.file
    file_content_as_list = read_csv(csv_file)
    if file:
        write_csv(file_content_as_list)
    else:
        print(csv_file)
    read_csv(csv_file)


# 02 exercise 2
def get_file_names(folderpath: str, out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    files = [f for f in listdir(folderpath)]
    with open(out, "w") as output:
        for f in files:
            output.write(f"{f}\n")


def get_all_file_names(folderpath: str, out="output.txt"):
    f = []
    i_list = []
    for (root, dirs, files) in walk(folderpath):
        for name in files:
            f.append(os.path.join(root, name))
        for name in dirs:
            f.append(os.path.join(root, name))

    with open(out, "w") as output:
        for i in f:
            i_list.append(i)
            output.write(f"{i}\n")

    return i_list


def print_line_one(file_names):
    for f in file_names:
        with open(f, "r") as file:
            print(file.readline())


def print_emails(file_names):
    print(file_names)
    for f in file_names:
        if f.endswith(".csv") or f.endswith(".txt") or f.endswith("xml"):
            with open(f, "r") as file:
                for line in file:
                    if line.find("@") is not -1:
                        print(f"{line} in file: {file.name}")
        else:
            print(f"no email found or file {f} not working.")


if __name__ == "__main__":
    print_emails(get_all_file_names("../../data"))

