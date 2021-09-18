import os
import shutil
from glob import glob


# def mycopyfile(frompath, target):
#         fpath, fname = os.path.split(frompath)
#         if not os.path.exists(target):
#             os.makedirs(target)
#         shutil.copy(frompath, target + fname)
#         print("copy %s -> %s" % (frompath, target))
#
#
# src_dir = 'D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\\tea\Makefile.in'
# dst_dir = 'D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\\tea\doc/'
# src_file_list = glob(src_dir + '*')
# for srcfile in src_file_list:
#     mycopyfile(srcfile, dst_dir)

# def mymovefile(frompath, target):
#         fpath, fname = os.path.split(frompath)
#         if not os.path.exists(target):
#             os.makedirs(target)
#         shutil.move(frompath, target + fname)
#         print("copy %s -> %s" % (frompath, target))
#
#
# from_dir = 'D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\\tea\doc'
# from_file_list = glob(from_dir + '*')
# to_dir = 'D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\\tea\\tclconfig/'
# for srcfile in from_file_list:
#     mymovefile(srcfile, to_dir)
# from_dir = 'D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\\tea\win'
# from_file_list = glob(from_dir + '*')
# for srcfile in from_file_list:
#     mymovefile(srcfile, to_dir)



def del_file(path_data):
    for i in os.listdir(path_data) :
        file_data = path_data + "\\" + i
        if os.path.isfile(file_data) == True:
            os.remove(file_data)
        else:
            del_file(file_data)
            os.rmdir(file_data)
path_data = r"D:\学习\数据库系统\dblabs\labs\sqlite-autoconf-3230100\tea"
del_file(path_data)
