import os
year = input("Generate the file and folder structure for which year? ")

def CreateFile(filePath: str, fileContents: str):
    try:
        with open(filePath, 'x') as file:
            file.write(fileContents)
    except FileExistsError:
        print('File ' + filePath + ' already exists.')


days = ['0' + str(x) if x < 10 else str(x) for x in range(1,26)]

txts = [
    'test.txt',
    'input.txt'
]
pys = [
    'p1.py',
    'p2.py'
]
startCode = '''with open('path/test.txt') as file:
    lines = file.readlines()


'''

for day in days:
    fileContents = ''
    dir = year + '/' + day
    if not os.path.exists(dir):
        os.makedirs(dir)
    for file in txts:
        filePath = dir + '/' + file
        CreateFile(filePath, fileContents)
    for file in pys:
        filePath = dir + '/' + file
        fileContents = startCode.replace('path', dir)
        CreateFile(filePath, fileContents)