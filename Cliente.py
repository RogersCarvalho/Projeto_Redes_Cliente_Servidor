import socket


serverHOST = '127.0.0.1'
serverPORT = 5000


mensagem = [b'Ola mundo xxxx']

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((serverHOST, serverPORT))


'''for linha in mensagem:
    tcp.send(linha) #envia mensagem para o servidor
    data = tcp.recv(1024) #resposta do servidor
    print('Cliente recebeu a mensagem enviada para o servidor: ', data) # imprime a resposta do servidor'''


while True:
    cmds = input("$ ")
    sends = bytes(cmds, "utf-8")
    tcp.send(sends)
    data = tcp.recv(1024).decode("utf-8")
    print(" Resposta do servidor {}".format(data))
    continue
s.close()









