import socket


BYTES_TO_READ = 4096

def get(host, port):

    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"  # b = bytes; the double new lines notifies the end of header and the beginning of body; host.encode converts to bytes

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request)
        s.shutdown(socket.SHUT_WR)

        print("Waiting for response!")
        chunk = s.recv(BYTES_TO_READ)
        result = b"" + chunk
        while len(chunk) > 0:
            chunk = s.recv(BYTES_TO_READ)
            result += chunk

        return result


print(get("127.0.0.1", 8080))
