#mdファイルをHTMLファイルに変換するプログラムを作る

#markdownライブラリを利用する

import markdown
import sys

print(markdown.markdown("#1"))


#python3 file-converter.py markdown inputfile outputfile

if len(sys.argv) != 4:
    print("**** Error ***  invalid parameter. This program needs four parameters")
    exit()

if sys.argv[1] != "markdown":
    print("*** Error *** parameter error. First parameter is not 'markdown'")
    exit()

inputpath = sys.argv[2]
outputpath = sys.argv[3]
try:
    with open(inputpath) as f:
        content = f.read()

    newcontent = markdown.markdown(content)

    with open(outputpath, 'w') as o:
        o.write(newcontent)
    
except FileNotFoundError as e:
    print(e)

