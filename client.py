
import socket, sys

def main():
    try:
        #define address info, payload, and buffer size
        host = 'www.google.com'
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096
        
        #make the socket, get the ip, and connect
        #create a tcp socket
        print('Creating socket')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created successfully')
        
        print(f'Getting IP for {host}')
        remote_ip = socket.gethostbyname(host)
        print (f'Ip address of {host} is {remote_ip}')


        s.connect((remote_ip , port))
        print (f'Socket Connected to {host} on ip {remote_ip}')
        
        #send the data and shutdown
        print("Sending payload")
        s.sendall(payload.encode())
        print("Payload sent successfully")
        
        s.shutdown(socket.SHUT_WR)

        #continue accepting data until no more left
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                 break
            full_data += data
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()
if __name__ == "__main__":
    main()

