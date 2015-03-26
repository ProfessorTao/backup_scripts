# coding:utf-8

def get_all_permutations(target_list):
    # 获取目标列表的全排列
    if len(target_list) <=1:
        yield target_list
    else:
        for perm in get_all_permutations(target_list[1:]):
            for i in range(len(target_list)):
                yield perm[:i] + target_list[0:1] + perm[i:]
# end of def  


def get_all_combinations(target_list):
    # 获取目标列表的全组合
    # 使用二进制数据来模拟全组合算法
    length = len(target_list)
    max = 2**length
    range_list = range(1, max, 1)

    for i in range_list:
        result_list = []
        pos = 0

        while (i):
            j = i % 2
            if 1 == j:
                result_list.append(target_list[pos])
            pos += 1
            i = i>>1
        # end of while

        yield result_list
    # end of for
# end of def
