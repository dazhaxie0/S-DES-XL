# 开发手册

**文件说明**

```tex
- main_part.py：主要功能函数
    - subkey ：密钥生成
	- permutation ：置换函数
	- permutation_reverse ：二次置换
	- round_function ：F轮函数
	- encryption ：加密算法
	- decryption ：解密算法
	
- ascll_part.py：ASCII码部分
	- ascii_to_binary ：将ASCII字符串转换为二进制字符串
	- binary_to_ascii ：将二进制字符串转换为ASCII字符串
	- encrypt_ascii ：加密ASCII编码
	- decrypt_ascii ：解密ASCII编码
	
- crack.py：暴力破解部分函数，主要函数如下
	- crack ： 破解实现函数
	- crack_multithreading ： 多线程剖解函数
	
- UI.py：UI界面实现部分

```

