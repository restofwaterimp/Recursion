import os
import json

# 'config.json'という名前のJSONファイルを読み込む

config = json.load(open('config.json'))

#configの'filepath'キーで指定されたパスのファイルを読み取りモード(r)で開く

f = open(config['filepath'], 'r')

# continue named pipe
# if existing pipe , True , False
flag = True

while flag:
    if not os.path.exists(config['filepath']):
        flag = False
    # read file
    data = f.read()

    # if data is not empty , this contents output
    if len(data) != 0:
        print('Data received from pipe: "{}"'.format(data))

# After it is not existed pipe, close file.
# It is important for program to release resources
f.close()