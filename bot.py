import socket
import time

# Configurações da Twitch
SERVER = "irc.chat.twitch.tv"
PORT = 6667  # Padrão IRC da Twitch
NICKNAME = "gemeodomall"  # Seu nome de usuário na Twitch
TOKEN = "oauth:5x8y3ahhvef1vo93ql9z7kp6w9cldc"  # OAuth gerado anteriormente
CHANNEL = "#scavote"  # Nome do canal (coloque com #)

# Conectar ao chat da Twitch via socket
sock = socket.socket()
sock.connect((SERVER, PORT))
sock.send(f"PASS {TOKEN}\r\n".encode("utf-8"))
sock.send(f"NICK {NICKNAME}\r\n".encode("utf-8"))
sock.send(f"JOIN {CHANNEL}\r\n".encode("utf-8"))

print(f"✅ Conectado ao canal {CHANNEL}!")

# Loop para receber mensagens e enviar respostas automáticas
while True:
    mensagem = "random"
    mensagem1 = "Ghast"
    # Espera 30 segundos e envia uma mensagem
    sock.send(f"PRIVMSG {CHANNEL} :{mensagem}\r\n".encode("utf-8"))
    print(f"📩 Mensagem enviada: {mensagem}")

    sock.send(f"PRIVMSG {CHANNEL} :{mensagem1}\r\n".encode("utf-8"))
    print(f"📩 Mensagem enviada: {mensagem1}")

    time.sleep(181)  

    