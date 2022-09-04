music_count, commands = int(input()), input()
cur_list = [i for i in range(1, music_count + 1)]
cur_select_num = 1
for c in commands:
    if c == 'U':
        # 处理当前列表
        if music_count > 4:
            if cur_select_num == cur_list[0]:
                # 如果当前选中是列表第一首
                if cur_select_num == 1:
                    # 当前选中的是总的第一首
                    cur_list.clear()
                    cur_list = [i for i in range(music_count - 4 + 1, music_count + 1)]
                else:
                    # 每一个选项减1
                    cur_list = list(map(lambda x: x - 1, cur_list))
            else:
                pass
        # 处理当前选择的歌曲
        if cur_select_num == 1:
            cur_select_num = music_count
        else:
            cur_select_num -= 1
    if c == 'D':
        # 处理当前列表
        if music_count > 4:
            if cur_select_num == cur_list[-1]:
                # 如果当前选中是列表最后一首
                if cur_select_num == music_count:
                    # 当前选中的是总的最后一首
                    cur_list.clear()
                    cur_list = [i for i in range(1, 5)]
                else:
                    # 每一个选项加1
                    cur_list = list(map(lambda x: x + 1, cur_list))
            else:
                pass
        # 处理当前选择的歌曲
        if cur_select_num == music_count:
            cur_select_num = 1
        else:
            cur_select_num += 1
print(' '.join(map(lambda x: str(x), cur_list)))
print(cur_select_num)
