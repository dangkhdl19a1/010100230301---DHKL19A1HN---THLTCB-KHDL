# ==================== BÀI 5.1 ====================
n = int(input("Nhập số nguyên dương: "))
nhi_phan = ""
tam = n
while tam > 0:
    nhi_phan = str(tam % 2) + nhi_phan
    tam //= 2
print(f"Nhị phân của {n}: {nhi_phan if nhi_phan else '0'}")

# ==================== BÀI 5.2 ====================
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
kq = ""
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        sub = str1[i:j]
        if sub in str2:
            if kq == "" or len(sub) < len(kq):
                kq = sub
            break  # đã tìm thấy độ dài ngắn nhất từ vị trí i
print("Chuỗi con chung ngắn nhất:", kq if kq else "Không có")

# ==================== BÀI 5.3 ====================
van_ban = input("Nhập chuỗi văn bản: ")
tu_khoa = input("Nhập từ khóa: ")
# Vị trí xuất hiện từ khóa
vi_tri = []
start = 0
while True:
    pos = van_ban.find(tu_khoa, start)
    if pos == -1:
        break
    vi_tri.append(pos)
    start = pos + 1
print("Vị trí xuất hiện:", vi_tri if vi_tri else "Không tìm thấy")
# Từ xuất hiện nhiều nhất
cac_tu = van_ban.split()
tan_suat = {}
for tu in cac_tu:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1
tu_nhieu_nhat = max(tan_suat, key=tan_suat.get) if tan_suat else ""
print(f"Từ xuất hiện nhiều nhất: '{tu_nhieu_nhat}' ({tan_suat.get(tu_nhieu_nhat, 0)} lần)")

# ==================== BÀI 5.4 ====================
xau = input("Nhập chuỗi: ")
chi_so = ""
for c in xau:
    if c.isdigit():
        chi_so += c
print("Chuỗi chỉ gồm số:", chi_so)
if chi_so:
    so = int(chi_so)
    nguyen_to = so > 1 and all(so % i != 0 for i in range(2, int(so**0.5) + 1))
    print(f"{so} là số nguyên tố" if nguyen_to else f"{so} không phải số nguyên tố")

# ==================== BÀI 5.5 ====================
s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")
tron = ""
for i in range(max(len(s1), len(s2))):
    if i < len(s1):
        tron += s1[i]
    if i < len(s2):
        tron += "-" + s2[i]
print("Chuỗi sau khi trộn:", tron.strip("-"))

# ==================== BÀI 5.6 ====================
xau = input("Nhập chuỗi: ")
dac_biet = {}
for c in xau:
    if not c.isalpha() and not c.isdigit():
        dac_biet[c] = dac_biet.get(c, 0) + 1
print("Thống kê ký tự đặc biệt:")
for k, v in dac_biet.items():
    print(f"  '{k}': {v} lần - {v/len(xau)*100:.2f}%")

# ==================== BÀI 5.7 ====================
xau = input("Nhập chuỗi: ")
hoa = thuong = so = db = 0
for c in xau:
    if c.isupper():   hoa += 1
    elif c.islower(): thuong += 1
    elif c.isdigit(): so += 1
    else:             db += 1
print(f"Chữ hoa: {hoa} | Chữ thường: {thuong} | Chữ số: {so} | Ký tự đặc biệt: {db}")

# ==================== BÀI 5.8 ====================
xau = input("Nhập chuỗi (>10 ký tự): ")
if len(xau) > 10:
    print("Vị trí 2→8:      ", xau[2:9])
    print("5 ký tự từ vị trí 5:", xau[5:10])
    print("3 ký tự cuối:    ", xau[-3:])
    print("Chữ hoa:         ", xau.upper())
    print("Chữ thường:      ", xau.lower())
    print("Đảo ngược:       ", xau[::-1])
else:
    print("Chuỗi phải dài hơn 10 ký tự!")

# ==================== BÀI 5.9 ====================
s1 = input("Nhập chuỗi gốc: ")
s2 = input("Nhập chuỗi mục tiêu: ")
m, n = len(s1), len(s2)
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(m+1): dp[i][0] = i
for j in range(n+1): dp[0][j] = j
for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
print(f"Số thao tác cần thiết (edit distance): {dp[m][n]}")

# ==================== BÀI 5.10 ====================
xau = input("Nhập chuỗi: ")
ket_qua = ""
for c in xau:
    if c != " ":
        ket_qua += c
print("Chuỗi sau khi xóa khoảng trắng:", ket_qua)