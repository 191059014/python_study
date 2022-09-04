comand_res_dict = {
    "reset": "reset what",
    "reset board": "board fault",
    "board add": "where to add",
    "board delete": "no board at all",
    "reboot backplane": "impossible",
    "backplane abort": "install first",
}


def filter_command(arr):
    matchs = []
    for k in comand_res_dict.keys():
        c_arr = k.split()
        if len(arr) == len(c_arr):
            all_match = True
            for i in range(len(arr)):
                if not c_arr[i].startswith(arr[i]):
                    all_match = False
                    break
            if all_match:
                matchs.append(k)
    if len(matchs) == 1:
        return comand_res_dict[matchs[0]]


while True:
    try:
        arr = input().split()
        res = filter_command(arr)
        if res:
            print(res)
        else:
            print("unknown command")
    except:
        break
