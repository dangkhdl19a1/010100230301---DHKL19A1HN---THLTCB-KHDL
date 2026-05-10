# 8.1
def la_nguyen_to(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
cap_sinh_doi = [(n, n+2) for n in range(2, 998) if la_nguyen_to(n) and la_nguyen_to(n+2)]
print("Các cặp số nguyên tố sinh đôi < 1000:")
for cap in cap_sinh_doi:
    print(cap, end="  ")

# 8.2
def giai_thua(n):
    if n == 0 or n == 1: return 1
    return n * giai_thua(n - 1)
n = int(input("\nNhập n để tính n!: "))
print(f"{n}! = {giai_thua(n)}")

# 8.3
def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n - r)
def to_hop(n, r):
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))
n, r = int(input("Nhập n: ")), int(input("Nhập r: "))
print(f"P({n},{r}) = {hoan_vi(n, r)}")
print(f"C({n},{r}) = {to_hop(n, r)}")

# 8.4
def cubesum(n):
    return sum(int(c)**3 for c in str(n))
n = int(input("Nhập số nguyên: "))
print(f"Tổng lập phương các chữ số của {n}: {cubesum(n)}")

# 8.5
def isArmstrong(n):
    so_chu_so = len(str(n))
    return sum(int(c)**so_chu_so for c in str(n)) == n
print("Các số Armstrong từ 1 đến 9999:")
armstrong = [n for n in range(1, 10000) if isArmstrong(n)]
print(armstrong)

# 8.6
def sumPdivisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
n = int(input("Nhập số nguyên dương: "))
print(f"Tổng ước số thực sự của {n}: {sumPdivisors(n)}")

# 8.7
def isAmicable(a, b):
    return a != b and sumPdivisors(a) == b and sumPdivisors(b) == a
a, b = int(input("Nhập số a: ")), int(input("Nhập số b: "))
if isAmicable(a, b):
    print(f"({a}, {b}) là cặp số Amicable")
else:
    print(f"({a}, {b}) không phải cặp số Amicable")

# 8.8
mang = list(map(int, input("Nhập mảng (cách nhau bởi dấu cách): ").split()))
so_chan = list(filter(lambda x: x % 2 == 0, mang))
so_le   = list(filter(lambda x: x % 2 != 0, mang))
print("Số chẵn:", so_chan)
print("Số lẻ: ", so_le)

# 8.9
lap_phuong = list(map(lambda x: x**3, mang))
print("Lập phương các phần tử:", lap_phuong)

# 8.10
chan_lap_phuong = list(map(lambda x: x**3, filter(lambda x: x % 2 == 0, mang)))
le_binh_phuong  = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, mang)))
print("Số chẵn → lập phương:", chan_lap_phuong)
print("Số lẻ  → bình phương:", le_binh_phuong)