from time import time
from threading import Thread
from main_part import *


def encryption_ans_check(text, key):
    k1 = subkey(key)[0]
    k2 = subkey(key)[1]
    ip = permutation(text)
    fk1 = round_function(ip, k1)
    sw = swap(fk1)
    fk2 = round_function(sw, k2)
    ip_reverse = permutation_reverse(fk2)
    return ip_reverse

# 破解实现函数
def crack(num, Tid, iText, iCipher, ans):
    print("开始破解")
    scale = int(1024 / num)
    flag = 0
    for index in range(Tid * scale, (Tid + 1) * scale):
        temp_key = str(bin(index)[2:].zfill(10))
        temp_ans = encryption_ans_check(iText, temp_key)
        solved_ans = ''.join(str(i) for i in temp_ans)
        if solved_ans == iCipher:
            ans.append(temp_key)
            print("找到的密钥为: " + temp_key)
            flag = 1
    if flag == 0:
        print("未找到密钥\n")
        return -1


# 多线程破解函数
def crack_multithreading(number, plaintext, ciphertext, keys):
    threads = []
    for n in range(number):
        thread = Thread(target=crack, args=(number, n, plaintext, ciphertext, keys))
        threads.append(thread)
    for i in range(number):
        threads[i].start()
    for j in range(number):
        threads[j].join()


keys = []
start = time()
crack(1, 0, '00000011', '11001110', keys)
end = time()
print('破解用时：' + str(end-start) + 's')


# 暴力破解：带时间戳，单线程及多线程
keys_single = []
keys_double = []
keys_multiple = []

print('-'*50 + '\n单线程：')
start_single = time()
crack(1, 0, '00000011', '11001110', ans=keys_single)
end_single = time()


print('-'*50 + '\n多线程：')
start_multiple = time()

crack_multithreading(20, '00000011', '11001110', keys=keys_multiple)

end_multiple = time()

print('-'*50)
print('单线程破解用时：' + str(end_single-start_single) + 's')
print('多线程破解用时：' + str(end_multiple-start_multiple) + 's')