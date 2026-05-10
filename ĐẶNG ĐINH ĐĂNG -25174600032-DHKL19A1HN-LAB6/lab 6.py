# ==================== BÀI 6.1 ====================
n = int(input("Nhập n: "))
mang = [int(input(f"a[{i}]: ")) for i in range(n)]
chan = [x for x in mang if x % 2 == 0]
le   = [x for x in mang if x % 2 != 0]
print("Số chẵn:", chan, "| Tổng:", sum(chan))
print("Số lẻ: ", le,   "| Tổng:", sum(le))

# ==================== BÀI 6.2 ====================
def la_nguyen_to(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
def la_hoan_hao(n):
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n
n = int(input("Nhập n: "))
mang = [int(input(f"a[{i}]: ")) for i in range(n)]
ket_qua = [x for x in mang if la_nguyen_to(x) or la_hoan_hao(x)]
print("Số nguyên tố hoặc hoàn hảo:", ket_qua)

# ==================== BÀI 6.3 ====================
n = int(input("Nhập n: "))
day_so = [float(input(f"x[{i}]: ")) for i in range(n)]
print("Lớn nhất:", max(day_so))
print("Nhỏ nhất:", min(day_so))

# ==================== BÀI 6.4 ====================
n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
print("Fibonacci:", fib[:n])

# ==================== BÀI 6.5 ====================
nguyen_to_100 = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("Số nguyên tố < 100:", nguyen_to_100)

# ==================== BÀI 6.6 ====================
n = int(input("Nhập n: "))
day = [int(input(f"a[{i}]: ")) for i in range(n)]
sai_phan = [day[i+1] - day[i] for i in range(len(day) - 1)]
if len(set(sai_phan)) == 1:
    print(f"Là cấp số cộng với công sai d = {sai_phan[0]}")
else:
    print("Không phải cấp số cộng")

# ==================== BÀI 6.7 ====================
m, n = int(input("Số hàng m: ")), int(input("Số cột n: "))
ma_tran = [[int(input(f"a[{i}][{j}]: ")) for j in range(n)] for i in range(m)]
tong = sum(ma_tran[i][j] for i in range(m) for j in range(n))
print("Tổng các phần tử:", tong)

# ==================== BÀI 6.8 ====================
def nhap_ma_tran(ten, m, n):
    return [[int(input(f"{ten}[{i}][{j}]: ")) for j in range(n)] for i in range(m)]
m, k, n = int(input("m: ")), int(input("k: ")), int(input("n: "))
A = nhap_ma_tran("A", m, k)
B = nhap_ma_tran("B", k, n)
C = [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]
print("Tích A x B:")
[print(hang) for hang in C]

# ==================== BÀI 6.9 ====================
m, n = int(input("Số hàng m: ")), int(input("Số cột n: "))
A = [[int(input(f"a[{i}][{j}]: ")) for j in range(n)] for i in range(m)]
chuyen_vi = [[A[i][j] for i in range(m)] for j in range(n)]
print("Ma trận chuyển vị:")
[print(hang) for hang in chuyen_vi]
if m == n and all(A[i][j] == A[j][i] for i in range(m) for j in range(n)):
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")

# ==================== BÀI 6.10 ====================
def dinh_thuc(M):
    n = len(M)
    if n == 1: return M[0][0]
    if n == 2: return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    return sum((-1)**j * M[0][j] * dinh_thuc([[M[i][k] for k in range(n) if k!=j] for i in range(1,n)]) for j in range(n))
def ma_tran_con(M, r, c):
    return [[M[i][j] for j in range(len(M)) if j!=c] for i in range(len(M)) if i!=r]
n = int(input("Cấp ma trận n: "))
A = [[float(input(f"a[{i}][{j}]: ")) for j in range(n)] for i in range(n)]
det = dinh_thuc(A)
if det == 0:
    print("Ma trận suy biến, không có nghịch đảo")
else:
    phu_hop = [[(-1)**(i+j) * dinh_thuc(ma_tran_con(A,i,j)) for j in range(n)] for i in range(n)]
    ngich_dao = [[phu_hop[j][i]/det for j in range(n)] for i in range(n)]
    print("Ma trận nghịch đảo:")
    [print([round(x, 4) for x in hang]) for hang in ngich_dao]