# LAB7
# 7.1
n = int(input("Nhập N: "))
d = {x: x**3 for x in range(1, n+1)}
print("Từ điển x³:", d)

# 7.2
sv = {}
n = int(input("Số sinh viên: "))
for _ in range(n):
    ten = input("Tên: ")
    diem = float(input("Điểm: "))
    sv[ten] = diem
def xep_loai(d):
    if d >= 9: return "A+"
    elif d >= 8: return "A"
    elif d >= 7: return "B"
    elif d >= 6: return "C"
    elif d >= 5: return "D"
    else: return "F"
phan_loai = {ten: (diem, xep_loai(diem)) for ten, diem in sv.items()}
print("Kết quả:", phan_loai)

# 7.3
tan_suat = {}
for ten, (diem, loai) in phan_loai.items():
    tan_suat[loai] = tan_suat.get(loai, 0) + 1
print("Thống kê học lực:", tan_suat)

# 7.4
van_ban = input("Nhập đoạn văn bản tiếng Anh: ").lower()
for ky_tu in ".,!?;:\"'":
    van_ban = van_ban.replace(ky_tu, "")
dem_tu = {}
for tu in van_ban.split():
    dem_tu[tu] = dem_tu.get(tu, 0) + 1
print("Tần suất từ:", dem_tu)

# 7.5
cao_nhat = max(dem_tu, key=dem_tu.get)
thap_nhat = min(dem_tu, key=dem_tu.get)
print(f"Từ xuất hiện nhiều nhất: '{cao_nhat}' ({dem_tu[cao_nhat]} lần)")
print(f"Từ xuất hiện ít nhất:   '{thap_nhat}' ({dem_tu[thap_nhat]} lần)")

# 7.6
inventory = {"backpack": ["rope", "torch", "map"], "gold": 50, "potion": 3}
inventory["pocket"] = ["key", "coin"]
inventory["gold"] += 20
print("Inventory sau cập nhật:", inventory)

# 7.7
inventory["backpack"].sort()
vat_pham_xoa = input("Nhập vật phẩm cần xóa khỏi backpack: ")
if vat_pham_xoa in inventory["backpack"]:
    inventory["backpack"].remove(vat_pham_xoa)
    print("Đã xóa. Backpack:", inventory["backpack"])
else:
    print("Không tìm thấy vật phẩm.")

# 7.8
ton_kho = {"Bút":  10, "Vở": 5, "Thước": 8}
don_gia = {"Bút": 5000, "Vở": 15000, "Thước": 8000}
print("-" * 35)
print(f"{'Mặt hàng':<12}{'SL':>5}{'Đơn giá':>10}{'Thành tiền':>12}")
print("-" * 35)
tong = 0
for mat_hang, sl in ton_kho.items():
    thanh_tien = sl * don_gia[mat_hang]
    tong += thanh_tien
    print(f"{mat_hang:<12}{sl:>5}{don_gia[mat_hang]:>10,}{thanh_tien:>12,}")
print("-" * 35)
print(f"{'TỔNG CỘNG':>27}{tong:>12,} đ")

# 7.9
da_ban = {"Bút": 4, "Vở": 2}
for mat_hang, so_luong in da_ban.items():
    if mat_hang in ton_kho:
        ton_kho[mat_hang] -= so_luong
print("Tồn kho sau giao dịch:")
for k, v in ton_kho.items():
    print(f"  {k}: {v} sản phẩm")

# 7.10
kho = {"Bút", "Vở", "Thước", "Tẩy", "Compa"}
da_chon = {"Bút", "Tẩy"}
chua_chon = kho - da_chon
print("Mặt hàng chưa được chọn mua:", chua_chon)