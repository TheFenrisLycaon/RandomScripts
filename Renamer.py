import os

path = str(input())
files = os.listdir(path)

# for i in files:
#     os.rename(path+i, path+'Karaoke - '+i+'.wav')

# print(files)

for i in files:
    j = i.find('-')
    k = i[j+2:]
    os.rename(path+i , path+k)


# for i in files:
#     k = i
#     j = i.replace('0', '')
#     os.rename(path+str(k), path+str(j))

# print(files)