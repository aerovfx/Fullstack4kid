Đọc xâu S từ tệp tin XAU42.INP. <br/>
pos = -1<br/>
for i từ 0 đến độ dài của S - 2:<br/>
    if S[i] < S[i+1]:<br/>
        pos = i<br/>

Nếu pos = -1:<br/>
    Ghi "IMPOSSIBLE" vào tệp tin XAU42.OUT.<br/>
Ngược lại:<br/>
    max_pos = -1<br/>
    for j từ pos+1 đến độ dài của S:<br/>
        if S[j] > S[pos]:<br/>
            max_pos = j<br/>

    Hoán vị S[pos] và S[max_pos] <br/>
    Đảo ngược các phần tử từ pos+1 đến cuối của xâu S <br/>
    Ghi xâu S vào tệp tin XAU42.OUT <br/>
