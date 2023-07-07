import datetime
import itertools
import zipfile


def uncompress(zipfile_path, extract_path, pass_word):
    try:
        with zipfile.ZipFile(zipfile_path) as z_file:
            z_file.extractall(extract_path, pwd=pass_word.encode("utf-8"))
        return True
    except:
        return False


def crack(zipfile_path, extract_path, chars, pwd_min_length, pwd_max_length):
    for password_length in range(pwd_min_length, pwd_max_length + 1):
        print('尝试按%s位密码解压...' % str(password_length))
        result = False
        password = None
        for c in itertools.permutations(chars, password_length):
            password = ''.join(c)
            result = uncompress(zipfile_path, extract_path, password)
            if result:
                break
        if result:
            print('解压成功，密码为：%s' % password)
            break


if __name__ == '__main__':
    start = datetime.datetime.now()
    # zip文件位置
    zipfile_path = "E:\\2023年3月抖音热门 BGM.zip"
    # zip解压后位置
    extract_path = "E:\\"
    # 预测密码构成的字符串
    chars = "2368"  # "abcdefghijklmnopqrstuvwxyz0123456789"
    # 预测密码最小长度
    pwd_min_length = 4
    # 预测密码最大长度
    pwd_max_length = 4
    # 调用破解方法
    crack(zipfile_path, extract_path, chars, 4, pwd_max_length)
    end = datetime.datetime.now()
    print('总共耗时%s分钟' % ((end - start).microseconds // 1000 // 60))
