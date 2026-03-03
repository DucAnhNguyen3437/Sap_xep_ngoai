import struct
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import List

class SortVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sắp xếp số thực trong tập tin nhị phân")
        self.file_path = None
        self.data = []
        self.sorted_data = []
        self.steps = []
        self.create_widgets()

    def create_widgets(self):
        self.btn_open = tk.Button(self.root, text="Chọn tập tin", command=self.open_file)
        self.btn_open.pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=5)

        self.btn_sort = tk.Button(self.root, text="Sắp xếp và minh họa", command=self.sort_and_visualize)
        self.btn_sort.pack(pady=5)

        self.btn_save = tk.Button(self.root, text="Lưu kết quả", command=self.save_file, state=tk.DISABLED)
        self.btn_save.pack(pady=5)

    def open_file(self):
        path = filedialog.askopenfilename(title="Chọn tập tin nhị phân", filetypes=[("Binary files", "*.bin"), ("All files", "*.*")])
        if not path:
            return
        self.file_path = path
        self.data = self.read_bin_file(path)
        self.show_data(self.data)
        self.btn_save.config(state=tk.DISABLED)

    def read_bin_file(self, path: str) -> List[float]:
        data = []
        try:
            with open(path, "rb") as f:
                while True:
                    bytes_ = f.read(8)
                    if not bytes_ or len(bytes_) < 8:
                        break
                    value = struct.unpack('d', bytes_)[0]
                    data.append(value)
        except Exception as e:
            messagebox.showerror("Lỗi đọc file", str(e))
        return data

    def show_data(self, data: List[float]):
        self.listbox.delete(0, tk.END)
        for i, v in enumerate(data):
            self.listbox.insert(tk.END, f"[{i}] {v}")

    def sort_and_visualize(self):
        if not self.data:
            messagebox.showwarning("Chưa có dữ liệu", "Vui lòng chọn tập tin dữ liệu trước.")
            return
        self.steps = []
        arr = self.data.copy()
        n = len(arr)
        # Bubble sort with step recording
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.steps.append(arr.copy())
        self.sorted_data = arr
        if len(self.data) <= 20:
            self.visualize_steps()
        else:
            self.show_data(self.sorted_data)
        self.btn_save.config(state=tk.NORMAL)

    def visualize_steps(self):
        if not self.steps:
            self.show_data(self.sorted_data)
            return
        self.current_step = 0
        self.show_data(self.steps[0])
        self.root.after(500, self.next_step)

    def next_step(self):
        self.current_step += 1
        if self.current_step < len(self.steps):
            self.show_data(self.steps[self.current_step])
            self.root.after(500, self.next_step)
        else:
            self.show_data(self.sorted_data)

    def save_file(self):
        if not self.sorted_data:
            return
        path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
        if not path:
            return
        try:
            with open(path, "wb") as f:
                for v in self.sorted_data:
                    f.write(struct.pack('d', v))
            messagebox.showinfo("Thành công", "Đã lưu file đã sắp xếp.")
        except Exception as e:
            messagebox.showerror("Lỗi lưu file", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizerApp(root)
    root.mainloop()
