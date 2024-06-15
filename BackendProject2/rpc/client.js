import net from 'net';

const jsonDataerrorFunc = {
    "method": "subtract", 
    "params": [78, 23], 
    "param_types": ['int', 'int'],
    "id": 3
 }

 const jsonDataanagram = {
    "method" : "validAnagram",
    "params": ["abcdef2", "gfedcba"], 
    "param_types": ['str', 'str'],
    "id": 4

 }

 const jsonDatanroot = {
    "method" : "nroot",
    "params": [6, 64],   
    "param_types": ['int', 'int'],
    "id": 5

 }

 const jsonDatareverse = {
    "method" : "reverse",
    "params": ["kk2toznb"],   
    "param_types": ['str'],
    "id": 5

 }

 const jsonDatasort = {
    "method" : "sort",
    "params": [["axt","abc","bbc","cs3" ]],   
    "param_types": ['list'],
    "id": 6

 }

const client = net.createConnection({path : '/tmp/socket_link'}, async () =>{
    console.log('conncted');

    const sendData = (data) => {
        console.log(data)
        client.write(JSON.stringify(data))
        console.log("OK")
    };

    // Exxample Data
    const jsonDataArray =[
        jsonDataerrorFunc,
        jsonDataanagram,
        jsonDatanroot,
        jsonDatareverse,
        jsonDatasort
    ];

    //jsonDataArray.forEach(data => sendData(data));
    
    const sandDataWithDelay = async (dataArray, delay) => {
        // if (!Array.isArray(dataArray)) {
        //     console.error('dataArray is not an array');
        //     return;
        // }
     
        for (const data of dataArray) {
            sendData(data);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    };

    //send data delay 1000 ms
    await sandDataWithDelay(jsonDataArray, 1000);

    
});

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

