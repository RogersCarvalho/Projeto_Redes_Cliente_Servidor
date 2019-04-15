import socket

url = input('url:')

extensionFile = open('servConfig/extension.txt','r')
extensionDict = {}
for line in extensionFile:
    keyValue = line.split()
    extensionDict[keyValue[1]] = keyValue[0]
    

if url.find('/') < 0:
    url = url + '/'
    
indexOf = url.find('/')
host = url[:indexOf] #endereço
getOperation = url[indexOf:]

fileExtension = ''

if(getOperation == '/'):
    fileExtension = '.html'

else:
    indexOfPoint = getOperation.rfind('.')
    if (indexOfPoint < 0):
        fileExtension = '.html'
    else:
        fileExtension = getOperation[indexOfPoint:]

operation = 'GET ' + getOperation+ ' HTTP/1.1\r\n'

request = {
    'Host: ' : host,
    'Connection: ' : 'keep-alive',
    'Upgrade-Insecure-Requests: ' : '1',
    'User-Agent: ' : 'Client',
    'Acept-Encoding: ' : 'gzir, deflate, br',
    'Accept-Language: ' : 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
}


HOST = host.split(':')[0]

try :
    PORT = host.split(':')[1]
except:
    PORT = 80
    
addr = ((HOST,int(PORT)))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IP-TCP
client_socket.connect(addr)

stringRequest = operation
for k,v in request.items():
    stringRequest = stringRequest+ k + v + '\n'

client_socket.send(stringRequest.encode())


total_data=[]
while True:
    data = client_socket.recv(8192)
    if not data: break
    total_data.append(data)
response = b''.join(total_data)

header = response.decode(errors="ignore")
header = header[:header.rfind('\r\n\r\n')]

headerSplit = header.split('\r\n')
status = headerSplit[0]
del(headerSplit[0])
print(status)

headerDict = {}
for line in headerSplit:
    keyValue = line.split(': ')
    try:
        headerDict[keyValue[0]] = keyValue[1]
    except:
        break

saveBinFile = response[len(header)+4:]


if getOperation == '/':
    fileName= 'Index'
else:
    indexOfLBar = getOperation.rfind('/')
    fileName = getOperation[indexOfLBar:indexOfPoint]
    
downloadPath = 'downloads/' + fileName + fileExtension

fileName

if status.split()[1] == '200':
    download = None 
    if headerDict['Content-Type'] != 'text/html':
        download = open(downloadPath,'wb')
        download.write(saveBinFile)
        download.close()
    else:
        download = open(downloadPath,'w')
        decodeFile = saveBinFile.decode()
        download.write(decodeFile)
        download.close()
else:
    print('erro ao processar a requisição do arquivo')
   

