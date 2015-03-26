#coding:utf-8

import os
import time_func

def remove_dir(dir_removed):  
     for root, dirs, files in os.walk(dir_removed, True, None, False):  
        #print root, dirs, files

        for each_dir in dirs:
            full_dir_path = os.path.join(root, each_dir)
            remove_dir(full_dir_path)

        for each_file in files:
            full_file_path = os.path.join(root, each_file)
            os.remove(full_file_path)

        # 删除主目录          
        os.removedirs(root)
    # end of for
# end of def


def remove_snapshot_files(date_str, local_dir, n_day_before = 1):
    n_after = -n_day_before
    n_day_before_date_str = time_func.get_datestr_after_target_datestr(date_str, n_after)
    local_path = '%s/%s' % (local_dir, n_day_before_date_str)

    if os.path.exists(local_path):
        remove_dir(local_path)
# end of def


if __name__ == '__main__':
    import sys
    date_str = sys.argv[1]

    local_dir = '/dev/shm/snapshot/mini_baidu/supply_id'
    remove_snapshot_files(date_str, local_dir)
