def extract_words(line):
    words = line.split()
    non_numeric_words = [word for word in words if not word.isdigit()]
    return non_numeric_words

def read_input_file():
    with open("CHONCHUOI.INP", "r") as file_input:
        lines = file_input.readlines()
    return lines

def write_output_file(words):
    with open("CHONCHUOI.OUT", "w") as file_output:
        for word in words:
            file_output.write(word + " ")
        file_output.write("\n")

def main():
    lines = read_input_file()

    all_words = []

    for line in lines:
        line = line.strip()
        words = extract_words(line)
        all_words.extend(words)

    write_output_file(all_words)

main()
