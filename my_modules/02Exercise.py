def print_file_content(file: str):
    with open(file) as f:
        for line in f:
            print(line)


def write_list_to_file(filename: str, text):
    with open(filename, "a") as f:
        f.write(text)


if __name__ == "__main__":
    print_file_content("../../data/country_codes.csv")
    write_list_to_file("textfile.txt")

