from main_part import *

# 将ASCII字符串转换为二进制字符串
# 明文转成二进制
def ascii_to_binary(text):
    iBinary = ""
    for char in text:
        ascii_code = ord(char)
        binary_code = bin(ascii_code)[2:]  # 去掉二进制字符串前面的"0b"前缀
        if len(binary_code) > 8:
            return 0
        binary_code = binary_code.zfill(8)  # 在不足八位的二进制数前面填充零
        iBinary += binary_code
    return iBinary

# 将二进制字符串转换为ASCII字符串
def binary_to_ascii(binary_text):
    ascii_text = ''
    for i in range(0, len(binary_text), 8):
        ascii_char = chr(int(binary_text[i:i+8], 2))
        ascii_text += ascii_char
    return ascii_text

# 加密ASCII编码的明文
def encrypt_ascii(text, key):
    binary_text = ascii_to_binary(text)
    k1 = subkey(key)[0]
    k2 = subkey(key)[1]
    ip = permutation(binary_text)
    fk1 = round_function(ip, k1)
    sw = swap(fk1)
    fk2 = round_function(sw, k2)
    ip_reverse = permutation_reverse(fk2)
    ip_str = ''.join(str(i) for i in ip_reverse)
    return chr(int(ip_str, 2))

# 解密ASCII编码的密文
def decrypt_ascii(text, key):
    binary_cipherText = ascii_to_binary(text)
    temp_text = [binary_cipherText[i:i + 8] for i in range(0, len(binary_cipherText), 8)]
    for index in temp_text:
        k1 = subkey(key)[0]
        k2 = subkey(key)[1]
        ip = permutation(index)
        fk2 = round_function(ip, k2)
        sw = swap(fk2)
        fk1 = round_function(sw, k1)
        ip_reverse = permutation_reverse(fk1)
        ip_str = ''.join(str(i) for i in ip_reverse)
        return chr(int(ip_str, 2))


# 加密单个字符
def encrypt_char(char, key):
    binary_char = ascii_to_binary(char)
    encrypted_binary_char = encryption(binary_char, key)
    encrypted_char = binary_to_ascii(encrypted_binary_char)
    return encrypted_char

# 解密单个字符
def decrypt_char(char, key):
    binary_char = ascii_to_binary(char)
    decrypted_binary_char = decryption(binary_char, key)
    decrypted_char = binary_to_ascii(decrypted_binary_char)
    return decrypted_char


