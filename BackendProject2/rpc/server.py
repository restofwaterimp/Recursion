import os
import socket
import math
import json
import builtins

def main():
    
    #Connection クラスをインスタンス化とソケット結合し、受信態勢
    socket = Connection()
    sock = socket.createsocket()
    connection , client_address = sock.accept()
    process = Process()


    while True:
        result = {}
        func_result = None
        #受信        
        data = process.recieveprocess(connection, client_address)
        
        #get function
        func = process.getFunction(data)
        if func is None:
            result["error"] = "invalid param : method Name"
            result["id"] = data["id"]
            process.sendclient(connection, result)
            continue

        #check paramName
        if not process.isValidateParam(data):
            result["error"] = "invalid param : parm"
            result["id"] = data["id"]
            process.sendclient(connection, result)
            continue
        
        # calculate
        if data["method"] in ["floor", "reverse", "sort"]:
            func_result = func(x = data["params"][0])
        elif data["method"] in ["nroot", "validAnagram"]:
            func_result = func(data["params"][0], data["params"][1])
        else:
            continue

        result["results"] = str(func_result)
        result["result_type"] = type(func_result).__name__
        result["id"] = data["id"]

        process.sendclient(connection, result)


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
        sock.listen(3)

        return sock

class Process:
    '''
    リクエストの処理とレスポンスの送信
    '''
    def __init__(self):
            self.calclatehandler = CalculatorHandler()
    
    def recieveprocess(self, connection, client_address=None):
        print('connection from', client_address)
        data = connection.recv(1024)

        #JSONファイルを読み込み、処理を返す
        #data_str = data.decode('utf-8')
        if data is None:
            return []
        data_str = json.loads(data.decode('utf-8'))
        print(f'Recieved JSON Data {data_str}')
        return data_str

    def getFunction(self, data: dict) -> callable:
        '''
        関数の取得
        '''
        return self.calclatehandler.getFunction(data)

    def isValidateParam(self, data: dict)-> bool:
        '''
        引数の確認
        '''
        return self.calclatehandler.isValidateparam(data)

    def sendclient(self, connect : socket.socket, data : dict):
        '''
        メッセージの送信
        '''
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
    def getFunction(self, data: dict) -> callable:

        # データがなければエラーを戻す
        if data is None:
            return None

        # 対象メソッドの指定がなければ、データを戻す 
        if  "method" not in data.keys(): return None
 
        if data["method"] in self.hashmap:
            return self.hashmap[data["method"]]
        else:
            return None
    
    def isValidateparam(self, data: dict) -> bool:
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


    # 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
    def floor(self, x : float) -> int:
        return int(math.ceil(x))
    
    def nroot(self, n : int , x : int) -> float:
        return math.pow(x , 1/n)

    def reverse(self ,x : str) -> str:
        revstr = ""
        n = len(x)
        for i in range(0,n):
            revstr = x[i] + revstr
        return revstr    

    def validAnagram(self, str1 : str, str2 : str) -> bool:
        n1 = len(str1)
        n2 = len(str2)
        if n1 != n2:return False
        for i in range(0, n1):
            if str1[i] != str2[n1-i-1]: return False
        return True
        
    def sort(self, x : list) -> str:
        return sorted(x)



if __name__ == '__main__':
    print('Starting the server')
    main()
    print('ShutDown the server')



