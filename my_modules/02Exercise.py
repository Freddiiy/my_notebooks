import argparse


def print_file_content(file: str):
    with open(file) as f:
        for line in f:
            print(line)


def write_list_to_file(filename: str, words):
    with open(filename, "a") as file_obj:
        for word in words:
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


if __name__ == "__main__":
    textfile = "textfile.txt"
    data_file = "../../data/employees.csv"
    words = ["This", "is", "a", "list"]
    # print_file_content(data_file)
    # write_list_to_file(textfile, words)
    # write_args_to_file(textfile, "Hello", "these", "are", "args")
    # read_csv(data_file)
    read_csv_cli()
