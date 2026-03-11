import os 
# Compatible underlying `os` module
# Works for all OSs

# way to interact with os
# acts as interface between you and your os

# List all of the supported classes/methods
# print(dir(os))

# cwd
# print(os.getcwd())

# cd
# os.chdir("/home")
# print(os.getcwd())

# mkdir - single level
# os.mkdir('mkdir')

# makedirs - multilevel
# os.makedirs('makedirs/mf/ss/sa')

# rmdir - single directory removal
# os.rmdir('mkdir')

# removedirs - remove directories recursively 
# os.removedirs('makedirs/mf/ss/sa')

# list directories - same folders files/dirs only
# print(os.listdir())
# print(os.listdir('/home'))
# print(os.listdir('/'))

# walk - gives files/dirs recursively 
# var = os.walk(os.getcwd()) # returns a generator . so we need to loop over it
# for i in var: 
#     print(i) # gives tuple with three things in it .. directory_path, folders, files
# for path, dirs, files in var: 
#     print(path)


# stat .. stats of any file
# stats = os.stat('./script.py')
# print(stats)
# os.stat_result(st_mode=33204, st_ino=11410748, st_dev=66309, st_nlink=1, st_uid=1000, st_gid=1000, st_size=2071, st_atime=1772960602, st_mtime=1772960589, st_ctime=1772960589)
# Extract datum
# print(stats.st_atime)
# print(stats.st_gid)
# print(stats.st_size, "bytes")


# Path manipulation
# file_name = "temp/file/new/abc.txt"
# print(os.path.basename(file_name))
# print(os.path.split(file_name)) # based on separator `/`
# print(os.path.dirname(file_name))

# print(os.path.exists("temp/file/new/abc.txt"))
# print(os.path.exists("/home/leo"))
# if (not os.path.exists('./testFolder')): os.mkdir('testFolder')



# To run any command of any os 

# os.system('ls') # for linux/mac
# os.system('dir') # for windows

# os.system('any_command')

# print(os.environ)