import tkinter as tk
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from ascll_part import *


# 定义按钮点击事件
def encrypt():
    plaintext = message_entry.get()
    key = key_entry.get()
    encode = combo.get()
    if not is_binary(10, key):
        tkinter.messagebox.showwarning('警告', '请输入 10bit 密钥！')
        return
    if encode == "--请选择输入编码语言--":
        tkinter.messagebox.showinfo('提示', '请选择输入编码语言')
        return
    elif encode == "Binary":
        if not is_binary(8, plaintext):
            tkinter.messagebox.showwarning('警告', '请输入 8bit 明文！')
            return
        ciphertext = encryption(plaintext, key)
    else:
        if not plaintext.isascii() or len(plaintext) != 1:
            tkinter.messagebox.showwarning('警告', '请输入 1Byte ASCII 明文！')
            return
        ciphertext = encrypt_ascii(plaintext, key)
    output_text.delete('1.0', tk.END)
    output_text.insert(END, '密文：' + ciphertext + "\n")

def decrypt():
    ciphertext = message_entry.get()
    key = key_entry.get()
    encode = combo.get()
    if not is_binary(10, key):
        tkinter.messagebox.showwarning('警告', '请输入 10bit 密钥！')
        return
    if encode == "--请选择输入编码语言--":
        tkinter.messagebox.showinfo('提示', '请选择输入编码语言')
        return
    elif encode == "Binary":
        if not is_binary(8, ciphertext):
            tkinter.messagebox.showwarning('警告', '请输入 8bit 密文！')
            return
        plaintext = decryption(ciphertext, key)
    else:
        if not ciphertext.isascii() or len(ciphertext) != 1:
            tkinter.messagebox.showwarning('警告', '请输入 1Byte ASCII 密文！')
            return
        plaintext = decrypt_ascii(ciphertext, key)
    plaintext_str = [str(i) for i in plaintext]
    output_text.delete('1.0', tk.END)
    output_text.insert(END, '明文：' + ''.join(plaintext_str) + "\n")

# 判断字符串是否是二进制，并且位数是否符合要求
def is_binary(bit_number, string):
    b = {'0', '1'}
    t = set(string)
    if b != t and t != {'0'} and t != {'1'}:
        return False
    if len(string) == bit_number:
        return True
    else:
        print(len(string))
        return False


root = tk.Tk()
root.title("S-DES加密解密")

style = Style(theme='sandstone')


# 居中
def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(500, 300)

# 创建中心标题
title_label = tk.Label(root, text='S-DES', font=("Times", 30, "bold"))
title_label.place(relx=.5, y=40, anchor='center')

# 创建下拉框
combo = ttk.Combobox(root, values=["--请选择输入编码语言--", "Binary", "ASCII"])
combo.current(0)
combo.place(relx=.5, y=86, anchor='center')

# 创建明文文本框及输入框
message_label = tk.Label(root, text="输入:")
message_label.place(x=130, rely=.4, anchor='center')
message_entry = tk.Entry(root)
message_entry.place(relx=.5, rely=.4, anchor='center')

# 创建密钥文本框及输入框
key_label = tk.Label(root, text="密钥:")
key_label.place(x=130, rely=.5, anchor='center')
key_entry = tk.Entry(root)
key_entry.place(relx=.5, rely=.5, anchor='center')

# 创建按钮
encryption_button = tk.Button(root, text="确认加密", command=encrypt)
encryption_button.place(relx=.4, y=190, anchor='center')
decryption_button = tk.Button(root, text="确认解密", command=decrypt)
decryption_button.place(relx=.6, y=190, anchor='center')


# 创建输出框控件
output_text = tk.Text(root, height=2, width=30)
output_text.place(relx=.5, rely=.8, anchor='center')


root.mainloop()