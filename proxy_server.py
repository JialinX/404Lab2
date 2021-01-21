import socket,time,sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
	host = 'www.google.com'
	port = 80
	with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_start:
		print('Starting proxy server')
		proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		proxy_start.bind((HOST,PORT))
		proxy_start.listen(1)
		while True:
			conn,addr = proxy_start.accept()
			print('Connected by',addr)
			with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as proxy_end:

				send_full_data = conn.recv(BUFFER_SIZE)
				
				print('Getting IP for {}'.format(host))
				remote_ip = socket.gethostbyname(host)
				print('Ip address of {} is {}'.format(host,remote_ip))
				proxy_end.connect((remote_ip,port))
				
				print('Sending received data {} to {}'.format(send_full_data,host))
				proxy_end.sendall(send_full_data)
				proxy_end.shutdown(socket.SHUT_WR)

				data = proxy_end.recv(BUFFER_SIZE)
				print('Sending received data {} to client'.format(data))
				conn.send(data)

			conn.close()

if __name__ == "__main__":
	main()