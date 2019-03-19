import socket


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 5000

print('Iniciado')

tcp.bind((HOST, PORT))

#número de cliente que pode lidar por vez
tcp.listen(5)


while True:
    con, cliente = tcp.accept() #aceita requisções e guarda a conexão e IP do cliente
    print('Concetado por', cliente) #informa o ip do cliente que se conectou
    while True:
        dados = con.recv(1024) #recebe e armazena os dados do cliente
        if not dados: break
        #print(cliente, dados)
        con.send(b'Eco=>'+ dados) #retorna o dado enviado pelo cliente

print('Finalizando conexao do cliente', cliente)
con.close()

