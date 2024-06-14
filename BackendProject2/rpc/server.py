import os
import socket
import math
import json
import sys
import builtins

# ソケットをつなぐ
# JSONファイルを読み込む
# 関数のチェック 指定の関数名があるか
# パラメータチェック argの数,argの型

def main():
    
    #Connection クラスをインスタンス化
    socket = Connection()
    sock = socket.createsocket()
    func_result = None
    result = {}

    while True:
        result = {}
        connection , client_address = sock.accept()
        process = Process()
        data = process.recieveprocess(connection, client_address)
        
        calclatehandler = CalculatorHandler()
        func = calclatehandler.analysis(data)
        if func is None:
            result["error"] = "invalid paaram method Name"
            result["id"] = data["id"]
            process.sendclient(connection, result)
            break

        if data["method"] in ["floor", "reverse", "sort"]:
            print(data["params"][0])
            if not calclatehandler.validateparam(data):
                result["error"] = "invalid param"
                process.sendclient(connection, result)
                break
            func_result = func(x = data["params"][0])
        elif data["method"] in ["nroot", "validAnagram"]:
            if not calclatehandler.validateparam(data):
                result["error"] = "invalid param"
                process.sendclient(connection, result)
                break
            func_result = func(data["params"][0], data["params"][1])
        else:
            result["error"] = "invalid paaram"
            result["id"] = data["id"]
            process.sendclient(connection, result)
            break
        
        result["results"] = str(func_result)
        result["result_type"] = type(func_result).__name__
        result["id"] = data["id"]

        print(result)
        process.sendclient(connection, result)

        # if not calclatehandler.validateparam(data):
        #     result["error"] = "invalid param"
        #     process.sendclient(sock, result)
        #     break
        


class Connection:
    '''
    ソケットの接続とバインド
    '''   
    def __init__(self):
        None
    def createsocket(self) -> socket.socket:
        #ソケットの作成
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # socket server address
        server_address = '/tmp/socket_link'

        try:
            os.unlink(server_address)
        except FileNotFoundError:
            pass

        print('Stargin up no {}'.format(server_address))

        # connect socket with server address
        sock.bind(server_address)
        #接続待ち(同時接続数)
        sock.listen(1)

        return sock

class Process:
    '''
    リクエストの処理とレスポンスの送信
    '''
    def __init__(self):
        None
    
    def recieveprocess(self, connection, client_address=None):
        print('connection from', client_address)
        data = connection.recv(1024)

        #JSONファイルを読み込み、処理を返す
        #data_str = data.decode('utf-8')
        data_str = json.loads(data.decode('utf-8'))
        print(f'Recieved JSON Data {data_str}')
        return data_str


    def analysis(self, data):
        None

    def sendclient(self, connect : socket.socket, data : dict):
        encode_data = json.dumps(data).encode('utf-8')
        connect.sendall(encode_data)



class CalculatorHandler:
    '''
    式の評価などの実施
    '''
      # 対比表
    def __init__(self):
        self.log = {}
        self.hashmap = {
        "floor": self.floor,
        "nroot": self.nroot,
        "reverse": self.reverse,
        "validAnagram": self.validAnagram,
        "sort": self.sort
        }

    #送付されたチャットの文字より、対象のメソッドを解析
    def analysis(self, data: dict) -> callable:

        # データがなければエラーを戻す
        if data is None:
            return None

        # 対象メソッドの指定がなければ、データを戻す 
        if  "method" not in data.keys(): return None
 
        if data["method"] in self.hashmap:
            return self.hashmap[data["method"]]
        else:
            return None
    
    def validateparam(self, data: dict) -> bool:
        '''
        パラメータの数と引数を確認
        '''
        if len(data["params"]) != len(data["param_types"]):
            return False
        
        for param, param_type in zip(data["params"], data["param_types"]):
            
            type_name  = param_type
            actual_type = getattr(builtins, type_name)
            print("param : ", param)
            print("indicate type : " , type(param_type))
            print("indicate type : " , type(actual_type))
            if not isinstance(param, actual_type):
                return False
        return True


    # 110 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
    def floor(self, x : float) -> int:
        return int(math.ceil(x))
    
    def nroot(self, n : int , x : int) -> float:
        return math.pow(x , 1/n)

    def reverse(self ,s : str) -> str:
        n = len(s)
        mid = n // 2
        for i in range(0,mid):
            s[i], s[n-i-1] = s[n-i-1] , s[i]
        return s


    def validAnagram(self, str1 : str, str2 : str) -> bool:
        n1 = len(str1)
        n2 = len(str2)
        if n1 != n2:return False
        for i in range(0, n1):
            if str1[i] != str2[n-i-1]: return False
        return True
        
    def sort(self, strArr : str) -> str:
        return sorted(strArr)





#thirft を真似ながら記述するものとする
if __name__ == '__main__':
    handler = CalculatorHandler()
    #ソケットの作成
    #バインド
    #接続
    #リクエスト処理
    #レスポンスの送信


    print('Starting the server')
    main()
    print('Done')



