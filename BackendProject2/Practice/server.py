import os
#jsonファイルの解析と生成
import json
config = json.load(open('config.json'))


#すでに同じ名前のパイプがある場合、削除する

if os.path.exists(config['filepath']):
    os.remove(config['filepath'])

#8進数、読み書き可能を表す
os.mkfifo(config['filepath'], 0o600)

print("FIFO named '% s' is created successfully." % config['filepath'])
print("Type in what you would like to send to clients")

# get user input and write named pipe
# until input 'exit'

flag = True

while flag:
    # get user input
    inputstr = input()

    if(inputstr == 'exit'):
        flag = False
    else:
        with open(config['filepath'], 'w') as f:
            f.write(inputstr)

# after program finish, remove named pipe
os.remove(config['filepath'])