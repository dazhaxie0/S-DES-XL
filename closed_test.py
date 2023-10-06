import random
from crack import crack


# 判断是否封闭
def is_close(plaintexts, ciphertext):
    keys = []
    target = []
    for plaintext in plaintexts:
        tmp_keys = []
        print('-' * 30)
        crack(1, 0, plaintext, ciphertext, tmp_keys)
        keys.append(tmp_keys)
    for i in range(len(keys)):
        if i == len(keys):
            break
        for j in range(i + 1, len(keys)):
            ini_notj = list(set(keys[i]) - set(keys[j]))
            inj_noti = list(set(keys[j]) - set(keys[i]))
            for key_i in ini_notj:
                if [plaintexts[i], key_i] not in target:
                    target.append([plaintexts[i], key_i])
            for key_j in inj_noti:
                if [plaintexts[j], key_j] not in target:
                    target.append([plaintexts[j], key_j])
    print('-' * 50)
    if not target:
        print('对该密文及明文对未找到不同的密钥')
    else:
        print('对于密文 ' + ciphertext + ' 可由以下不同的明文及密钥加密得到：')
        for p, k in target:
            print('明文：' + p + '    密钥：' + k)


# 生成随机明文分组
def generate_random_plaintext(number):
    plaintexts = []
    for n in range(number):
        decimal_number = random.randint(0, 255)
        plaintexts.append(str(bin(decimal_number)[2:].zfill(8)))
    print(plaintexts)
    return plaintexts


is_close(generate_random_plaintext(2), '01011111')



