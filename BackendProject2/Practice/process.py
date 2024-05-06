import os
import time

#rは読み取り専用、wは書きこみ専用
r, w = os.pipe()
# プロセスの複製
pid = os.fork()


# while True:
#     print('Runnign in the background')
#     time.sleep(2)

# pid が0より大きい場合、親プロセス
if pid > 0:
    #読み取り端を閉じる
    os.close(r)
    #現在のプロセスIDを取得
    message = 'Message from parent with pid {}'.format(os.getpid())
    #生成メッセージを表示
    print('Parent, sending out the message - {}'.format(message, os.getpid()))
    #メッセージをエンコードしてパイプに各
    os.write(w, message.encode('utf_8'))

# pidが0の場合、子プロセス
else:
    #書き込み端を閉じる
    os.close(w)

    print("Fork is 0, this is a Child PID:", os.getpid())
    #読み取り用のファイルsディスクリプタを開く
    f = os.fdopen(r)
    #パイプから読み取ったメッセージを表示
    print("Incoming string:", f.read())