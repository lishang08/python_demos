# coding=utf-8

# file read operation, use try...finally to ensure the file can be closed in the exception case
try:
    f = open("D:/fulishang/study/python/python_demos/file_handler/filehandler_test.txt", 'r')
    print(f.read())
finally:
    if f:
        # close file in case conflict
        f.close()
