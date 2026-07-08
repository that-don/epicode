from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP, ARP

print("=" * 80)
print("      SNIFFER DI RETE - DEMO")
print("=" * 80)
print("Premi CTRL+C per interrompere.\n")


def analizza_pacchetto(packet):

    print("-" * 80)

    # Ethernet
    if Ether in packet:
        ethernet = packet[Ether]
        print(f"MAC Sorgente      : {ethernet.src}")
        print(f"MAC Destinazione  : {ethernet.dst}")

    # ARP
    if ARP in packet:
        arp = packet[ARP]
        print("\nProtocollo : ARP")
        print(f"IP Mittente       : {arp.psrc}")
        print(f"IP Destinatario   : {arp.pdst}")
        return

    # IPv4
    if IP in packet:

        ip = packet[IP]

        print("\nProtocollo IP")
        print(f"IP Sorgente       : {ip.src}")
        print(f"IP Destinazione   : {ip.dst}")
        print(f"TTL               : {ip.ttl}")
        print(f"Lunghezza         : {len(packet)} byte")

        # TCP
        if TCP in packet:
            tcp = packet[TCP]

            print("\nTrasporto : TCP")
            print(f"Porta Sorgente    : {tcp.sport}")
            print(f"Porta Destinazione: {tcp.dport}")
            print(f"Flags             : {tcp.flags}")
            print(f"Sequence Number   : {tcp.seq}")

        # UDP
        elif UDP in packet:
            udp = packet[UDP]

            print("\nTrasporto : UDP")
            print(f"Porta Sorgente    : {udp.sport}")
            print(f"Porta Destinazione: {udp.dport}")

        # ICMP
        elif ICMP in packet:
            icmp = packet[ICMP]

            print("\nTrasporto : ICMP")
            print(f"Tipo              : {icmp.type}")
            print(f"Codice            : {icmp.code}")

        else:
            print("\nProtocollo non riconosciuto")


sniff(
    prn=analizza_pacchetto,
    store=False
)