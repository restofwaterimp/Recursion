import sys
#sys.stdout.flush()
# sys.stdout.buffer.write(b'Hello Jupiter')
sys.stdout.buffer.write(b'What is your favarite food?\n')
# 貯蓄しているbufferの内容を全て出力する
sys.stdout.flush()
# food = input('What is your favarite food?\n')
food = sys.stdin.buffer.readline()
#byte から　文字列にでコードが必要なため、decode()メソッドをつけている
# print('Thanks for lettin me your favarite food is ' + food.decode())