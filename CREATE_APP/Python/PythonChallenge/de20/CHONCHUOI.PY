# khối hàm tách chữ ra khỏi số
def tach(line):
    words = line.split()
    non_num_words = [word for word in words if word.isdigit()]
    return non_num_words

#print(extract_words('32 toi 21'))
# khối đọc dữ liệu từ file
with open('CHONCHUOI.INP', 'r') as file:
    lines = file.readlines()
all_lines = []

for line in lines:
    line = line.strip()
    words = tach(line)
    all_lines.append(' '.join(words))
lines = all_lines
# khối ghi dữ liệu ra file
with open('CHONCHUOI.OUT', 'w') as file:
    for i in range(len(lines)):
        file.write(lines[i].strip() + '\n')
# Chương trình chính

