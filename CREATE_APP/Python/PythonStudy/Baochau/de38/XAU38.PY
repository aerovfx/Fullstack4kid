#text = " Chào bạn.     Bạn khoẻ   không?"
# Output: "Chào bạn. Bạn khoẻ không?"
# hàm xoá khoảng trống
def space(text):
    text = ' '.join(text.split())
    return text
# đọc dữ liệu
with open('XAU38.INP', 'r') as file:
    text = file.read()
    
with open('XAU38.OUT', 'w') as file:
    result = space(text)
    file.write(str(result))