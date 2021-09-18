"""生成激活码"""
import random

number = 20
length = 12


def made():  # 生成激活码
    use_code = [x for x in '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
    # use_code = list('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    # print(use_code)
    # print(random.choice(use_code))
    cdkey_list = []
    while len(cdkey_list) != number:
        key_str = ''
        while len(key_str) != 12:
            key_str += random.choice(use_code)
        if cdkey_list.count(key_str) == 0:
            cdkey_list.append(key_str)
    return cdkey_list


def main():
    print(made())


if __name__ == '__main__':
    main()
