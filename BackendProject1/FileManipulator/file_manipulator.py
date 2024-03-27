import sys

#引数チェック
if len(sys.argv) == 0:
    print("Invalid arguments. This program needs at least one word")
    exit

command = sys.argv[1]

# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
# replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

# open() メソッドの引数
# 'r': ファイルを読み込み専用モードで開きます。
# 'w': ファイルを書き込み専用モードで開きます。ファイルが存在しない場合、ファイルが作成されます。ファイルが既に存在する場合、上書きされます。
# 'x': ファイルを書き込み専用で開きます。ファイルが存在しない場合、ファイルが作成されます。ファイルが既に存在する場合は、エラーが発生します。
# 'a': ファイルを書き込み専用で開きます。ファイルが存在しない場合、ファイルが作成される。ファイルはアペンドモードで開かれ、新しいデータがファイルの末尾に追加されます。
# 'b': ファイルをバイナリモードで開きます。画像や音声ファイルなどのバイナリファイルの読み書きに使用します。
# 't': ファイルをテキストモードで開きます。これは、ファイルを開く際のデフォルトのモードです。
# '+': 読み書き両用でファイルを開きます。

'''
ファイル内容の逆転
'''
def filereverse(inputpath , outputpath):
    with open(inputpath) as f:
        # l_strinp = [s for s in f.readlines()]
        content = f.read()

        with open(outputpath, 'w') as o:
            o.writelines(reversed(content))
    print('file reverse')
    

'''
ファイルコピー
'''
def filecopy(inputpath , outputpath):
    with open(inputpath) as f:
        content = f.read()
        with open(outputpath, 'w')  as o:
            o.write(content)
    print('file copy')

'''
ファイル内容の繰り返し
'''
def filedupulicate(inputpath, count):
    if not count.isdigit():
        print('count is not number.Please input number')
        exit()

    with open(inputpath) as f:
            content = f.read()
    
    for i in range(int(count)):    
        with open(inputpath, 'a') as o:
            o.write(content) 

    print('file copy ', count, ' count.')

'''
指定文字列の置換
'''
def replaceContent(inputpath, originString, replaceString):
    with open(inputpath) as f:
            content = f.read()

    newcontent = content.replace(originString, replaceString)
    with open(inputpath, 'w') as o:
        o.write(newcontent)
    print('replace string')


try:
    if command == 'reverse':
        if len(sys.argv) < 4:
            print('***Error*** reverse command needs two word. input filepath, output filepath')
            exit()
        filereverse(sys.argv[2], sys.argv[3])    

    elif command == 'copy':
        if len(sys.argv) < 4:
            print('***Error*** copy command needs two word. input filepath, output filepath')
            exit()
        filecopy(sys.argv[2], sys.argv[3])
    elif command == 'duplicate-contents':
        if len(sys.argv) < 4:
            print('***Error*** duplicate-contents command needs four word. input filepath, output filepath, count')
            exit()
        filedupulicate(sys.argv[2], sys.argv[3])
    elif command == 'replace-string':
        if len(sys.argv) < 5:
            print('***Error*** replace-string command needs four word. input filepath, needle, new-string')
            exit()
        replaceContent(sys.argv[2], sys.argv[3], sys.argv[4])    
    else:
        print('invalid command')

except FileNotFoundError as e:
    print('error')
    print(e)
