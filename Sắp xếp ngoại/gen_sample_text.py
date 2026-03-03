import struct
import random

# Tạo 10 số thực ngẫu nhiên
numbers = [random.uniform(-100, 100) for _ in range(10)]

with open("sample_data.bin", "wb") as f:
    for num in numbers:
        f.write(struct.pack('d', num))

print("Đã tạo file sample_data.bin với 10 số thực:")
print(numbers)
