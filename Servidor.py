import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 5000

print('Iniciado serviço ...')

try:
    tcp.bind((HOST, PORT))
    tcp.listen(1) #número de cliente que pode lidar por vez
except socket.error as e:
    print(str(e))


while True:
    con, cliente = tcp.accept() #aceita requisções e guarda a conexão e IP do cliente
    print('Conectado por', cliente) #informa o ip do cliente que se conectou
    while True:
        dados = con.recv(1024) #recebe e armazena a mensagem do cliente
        if not dados: break
        con.send(b'......:'+ dados) #retorna o dado enviado pelo cliente
con.close()
