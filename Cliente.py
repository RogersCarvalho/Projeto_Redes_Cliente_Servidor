import socket

serverHOST = str(input('Host_Servidor:'))
#serverPORT = int(input('porta:'))

#serverHOST = '127.0.0.1'
serverPORT = 5000

#cria o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp.connect((serverHOST, serverPORT))
    print(f'Conectado ao servidor..', serverHOST)

    while True:
        cmds = input("Cliente envia mensagem: ")
        if cmds == 'q':
            break
            tcp.close()
        sends = bytes(cmds, "utf-8")
        tcp.send(sends)
        data = tcp.recv(1024).decode("utf-8")
        print("Servidor responde{}".format(data))
        continue

except socket.error as e:
    print('Erro:', str(e))
finally:
    tcp.close()



