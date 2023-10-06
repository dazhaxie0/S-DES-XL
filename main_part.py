
# 初始置换
def permutation(origin):
    p_box = [2, 6, 3, 1, 4, 8, 5, 7]
    p_result = []
    for index in range(8):
        p_result.append(int(origin[p_box[index] - 1]))
    return p_result


# 二次置换
def permutation_reverse(origin):
    p_box = [4, 1, 3, 5, 7, 2, 8, 6]
    p_reverse_result = []
    for index in range(8):
        p_reverse_result.append(int(origin[p_box[index] - 1]))
    return p_reverse_result


# 左右互换操作
def swap(origin):
    right = []
    left = []
    for index in range(4):
        right.append(origin[index])
    for index in range(4):
        left.append(origin[index + 4])
    return left + right


# 密钥的生成
def subkey(origin):
    p_10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p_8 = [6, 3, 7, 4, 8, 5, 10, 9]
    leftShift01 = [2, 3, 4, 5, 1]
    leftShift02 = [3, 4, 5, 1, 2]
    temp = []
    # 按p10轮转对密钥进行处理
    for i in range(10):
        temp.append(int(origin[p_10[i] - 1]))
    k1 = []
    k2 = []
    temp01 = []
    temp02 = []
    temp03 = []
    temp04 = []
    # 获得k1
    # 对密钥的左半边进行leftShift1
    for i in range(5):
        temp01.append(temp[leftShift01[i] - 1])
    # 对密钥的右半边进行leftShift1
    for i in range(5):
        temp02.append(temp[leftShift01[i] + 4])
    # 合并得到子密钥k1
    for i in range(8):
        k1.append((temp01 + temp02)[p_8[i] - 1])
    # 计算并获得k2
    for i in range(5):
        temp03.append(temp[leftShift02[i] - 1])
    for i in range(5):
        temp04.append(temp[leftShift02[i] + 4])
    for i in range(8):
        k2.append((temp03 + temp04)[p_8[i] - 1])
    return [k1, k2]


# 二进制转换
def binary(a):
    if a == 3:
        return [1, 1]
    elif a == 2:
        return [1, 0]
    elif a == 1:
        return [0, 1]
    else:
        return [0, 0]


# F函数
def round_function(originKey, k):
    # 将输入的内容分成L和R，其中origin_split是L
    origin = []
    origin_split = []
    for index in range(4):
        origin_split.append(int(originKey[index]))
    for index in range(4):
        origin.append(int(originKey[index + 4]))
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    S1 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 0, 2]]
    S2 = [[0, 1, 2, 3],
          [2, 3, 1, 0],
          [3, 0, 1, 2],
          [2, 1, 0, 3]]
    P4 = [2, 4, 3, 1]
    key_right = []
    # 对R半边进行拓展
    for index in range(8):
        key_right.append(int(origin[EP[index] - 1]))
    # 进行轮转置换
    for index in range(8):
        if k[index] == key_right[index]:
            key_right[index] = 0
        else:
            key_right[index] = 1
    # 找到在矩阵中对应位置
    flag01 = key_right[0] * 2 + key_right[3] * 1
    flag02 = key_right[1] * 2 + key_right[2] * 1
    flag03 = key_right[4] * 2 + key_right[7] * 1
    flag04 = key_right[5] * 2 + key_right[6] * 1
    key_right01 = S1[flag01][flag02]
    key_right02 = S2[flag03][flag04]
    ans = binary(key_right01) + binary(key_right02)
    key_left = []
    # 轮转
    for index in range(4):
        key_left.append(ans[P4[index] - 1])
    # 异或
    for index in range(4):
        if key_left[index] == origin_split[index]:
            key_left[index] = 0
        else:
            key_left[index] = 1
    # 左右合并
    return key_left + origin

# 加密
def encryption(text,key):

        k1 = subkey(key)[0]
        k2 = subkey(key)[1]
        ip = permutation(text)
        fk1 = round_function(ip, k1)
        sw = swap(fk1)
        fk2 = round_function(sw, k2)
        ip_reverse = permutation_reverse(fk2)
        ip_str = ''.join(str(i) for i in ip_reverse)
        return ip_str


# 解密
def decryption(text,key):

        k1 = subkey(key)[0]
        k2 = subkey(key)[1]
        ip = permutation(text)
        fk2 = round_function(ip, k2)
        sw = swap(fk2)
        fk1 = round_function(sw, k1)
        ip_reverse = permutation_reverse(fk1)
        return ip_reverse

#测试
def test():
    plain_text = input("请输入明文：")
    key = input("请输入密钥：")
    cipher_text = encryption(plain_text,key)
    print("加密密文",cipher_text)
    print("密文解密",decryption(cipher_text,key))

#test()
