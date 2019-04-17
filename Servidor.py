
import socket
import os 
import datetime as dt
import threading as th
import sys

    
def requestMessage (con,cliente,extensionDict,shareFolder):
    
    print ("Aguardando requisição...")
    mensagem = con.recv(1048576).decode('utf-8') #Recebe as informações em bites

    msg = mensagem.split("\n")
    request['operation'] = msg[0]
    
    del(msg[0])
    
    print(request['operation'])

    #debug variable
    cont = 0

    for line in msg:
        cont = cont+1
        print ('linha...',line)
        lineSplit = line.split(': ')
        try:
            key = lineSplit[0]
            valor = lineSplit[1]
            request[key] = valor
        except:
            break

    try:
        filepath = request['operation'].split()[1]
    except:
        filepath='servConfig/400.html'
        
    if filepath == '/':
        nameFile = request['operation'].split()

        file = open(shareFolder + '/Index.html','rb')

        fileByte = file.read()

        respostaString = '\nHTTP/1.1 200 Ok \r\n' #traz o index

        resposta = {
            "Location" : "http://localhost:7000/",
            'date' : str(dt.datetime.now()),
            'Server' : 'server',
            'Content-Type' : 'text/html',
            'Content-Lenght' : str(len(fileByte))

        }
        for key,valor in resposta.items():
            respostaString = respostaString + key+': '+ valor + '\r\n'

        respostaString = respostaString + '\r\n'
        con.send( respostaString.encode('utf-8') + fileByte )

    else:
            
        if os.path.isfile(shareFolder + filepath) :
            file = open(shareFolder + filepath,'rb')
            respostaString = '\nHTTP/1.1 200 okk! \r\n' #arquivos
            fileByte = file.read()
            index = filepath.rfind('.')
            keyExtension = filepath[index:]
        else:
            file = open('servConfig/404.html','rb')
            respostaString = '\nHTTP/1.1 404 Not Found! \r\n'
            fileByte = file.read()
            keyExtension = '.html'

        resposta = {
            "Location" : "http://localhost:7000/",
            'date' : str(dt.datetime.now()),
            'Server' : 'server',
            'Content-Type' : extensionDict[keyExtension],
            'Content-Length' : str(len(fileByte))

        }

        for key,valor in resposta.items():
            respostaString = respostaString + key+': '+ valor + '\r\n'
        
        respostaString = respostaString + '\r\n'
        file.close()
        con.sendall( respostaString.encode('utf-8') + fileByte )
    con.close()

    
request = {}
host = 'localhost'#host = '0.0.0.0'
port = int(sys.argv[1])#port = 8080

shareFolder = sys.argv[2]
loadextensions = open('servConfig/extension.txt','r')
extensionDict = {}

for line in loadextensions:
    keyValue = line.split('\t')
    index = keyValue[1].find('\r\n')
    extensionDict[keyValue[0]] = keyValue[1][:index]
    
loadextensions.close()


addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr) #vicula o ip a porta
serv_socket.listen(10) #número de clientes por vez


file = ''
fileByte = ''
cons = set()
cont = 0
while True:    
    con, cliente = serv_socket.accept() ###Escutando
    print ('conectado...')
    cons.add(con)
    th.Thread(target=requestMessage,args=(con, cliente, extensionDict,shareFolder)).start()
    
