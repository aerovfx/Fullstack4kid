# Đọc xâu S từ tệp tin XAU42.INP
with open('XAU42.INP', 'r') as file_in:
    S = file_in.readline().strip()

# Tìm vị trí pos
pos = -1
for i in range(len(S) - 1):
    if S[i] < S[i+1]:
        pos = i

if pos == -1:
    # Ghi "IMPOSSIBLE" vào tệp tin XAU42.OUT
    with open('XAU42.OUT', 'w') as file_out:
        file_out.write("IMPOSSIBLE")
else:
    # Tìm vị trí max_pos
    max_pos = -1
    for j in range(pos+1, len(S)):
        if S[j] > S[pos]:
            max_pos = j

    # Hoán vị S[pos] và S[max_pos]
    S = list(S)
    S[pos], S[max_pos] = S[max_pos], S[pos]

    # Đảo ngược các phần tử từ pos+1 đến cuối của xâu S
    S = S[:pos+1] + S[pos+1:][::-1]

    # Ghi xâu S vào tệp tin XAU42.OUT
    with open('XAU42.OUT', 'w') as file_out:
        file_out.write("".join(S))
