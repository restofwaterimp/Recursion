import net from 'net';

const jsonData = {
    "method": "subtract", 
    "params": [78, 23], 
    "param_types": ['int', 'int'],
    "id": 3
 }


const client = net.createConnection({path : '/tmp/socket_link'},() =>{
    console.log('conncted');
    //reviece
    client.on('data', (data) => {
        console.log('recieved from server :' , data.toString());
    });
    //disconnect
    client.on('end', () =>{
        console.log('dissconected.');
    });
    //revieved error
    client.on('error', (err) => {
        console.log(err.message);
    });
});

// client.write("{
//     "method": "subtract", 
//     "params": [42, 23], 
//     "param_types": [int, int],
//     "id": 1
//  }")

 client.write(JSON.stringify(jsonData));

// 'config.json'という名前のJSONファイルを読み込む

// config = json.load(open('config.json'))

// configの'filepath'キーで指定されたパスのファイルを読み取りモード(r)で開く

// f = open(config['filepath'], 'r')

// continue named pipe
// if existing pipe , True , False
// flag = True
// let flag

// while(flag){
//     try{
//         const status = constfs.statSync(config['filepath'])
//         if (!status.isDirectory()){
//             flag = False
//         }
//         let data = f.read()
//         //if data is not empty , this contents output
//         if (data.len() != 0)
//             console.log('Data received from pipe: "{}"'.format(data))

//     }
//     catch(err){
//         console.log(err, "Don't exists filepath")
//     }
//     finally{
//         console.log("finish")
//     }
// }
// After it is not existed pipe, close file.
// It is important for program to release resources

// f.close()
    