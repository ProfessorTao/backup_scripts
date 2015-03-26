

import os, sys

if __name__ == '__main__':
    each_log_folder_path = os.getcwd()
    print each_log_folder_path

    for item in os.walk(each_log_folder_path):
        if not item[2]:
            # empty folder
            continue

        for name in item[2]:
            if not name[-3:] == '.pl':                
                continue

            print name
            fp = open(name, 'r+')
            b_modify = False
            content_list = fp.readlines()
            for index, line in enumerate(content_list):
                if '8306' in line:
                    line = line.replace('8306', '3306')
                    content_list[index] = line
                    b_modify = True

            if b_modify:
                fp.seek(0)
                fp.writelines(content_list)
                print ' -> mofify file %s' % name

            fp.close()
        # end of for name in item[2]

        continue # only root directory
    # end of os.walk


