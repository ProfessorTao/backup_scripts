#encoding:utf-8

import os

CUR_PATH = os.path.dirname(os.path.abspath(__file__))

'''
以下内容的返回值为True or False
exists()  指定路径（文件或目录）是否存在
isabs()   指定路径是否为绝对路径
isdir()   指定路径是否存在且为一个目录
isfile()  指定路径是否存在且为一个文件
samefile() 两个路径名是否指向同一个文件
'''


def func_make_dir(folder_path):
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)
# end of def func_make_dir


def traverse_folder(folder_path, filter_str = None):
    result_files_list = []

    for item in os.walk(folder_path):
        root, dirs, files = item
        if '\\' in root:
            root = root.replace('\\', '/')

        for file_name in files:
            if filter_str:
                if not filter_str in file_name:
                 continue # 过滤文件 or 文件夹
    
            # file
            result_files_list.append( '%s/%s' % (root, file_name) )
        # end of for file_name

        # 不需要递归遍历，因为os.walk已经帮忙做了
        #for dir_name in dirs:
        #    sub_folder_name = '%s/%s' % (folder_path, dir_name)
        #    traverse_folder(sub_folder_name)
    # end of for item

    return result_files_list
# end of def
