from scapy.all import rdpcap, IP, TCP, UDP, ICMP
from scapy.layers.http import HTTPRequest # Mantido por segurança, mas não será usado para a contagem principal

# Caminho do arquivo PCAP
pcap_file = "C:/Users/Dell/OneDrive/Documentos/CursoPython/FaculdadePython/DoS (1).pcap"

# IPs envolvidos
ip_attacker = "192.168.56.110"
ip_target = "192.168.56.102"

# Carregar os pacotes
try:
    packets = rdpcap(pcap_file)
except FileNotFoundError:
    print(f"Erro: O arquivo PCAP não foi encontrado no caminho especificado: {pcap_file}")
    exit()

# Contador específico para o payload ICMP, conforme a dica do professor
total_icmp_payload = 0

for pkt in packets:
    # Filtra por pacotes IP do atacante para o alvo
    # E agora, crucialmente, verifica se o pacote é ICMP
    if pkt.haslayer(IP) and pkt[IP].src == ip_attacker and pkt[IP].dst == ip_target and pkt.haslayer(ICMP):
        
        # Para o "ping da morte", o tamanho relevante é o payload do ICMP.
        # Scapy representa o restante dos dados após o cabeçalho ICMP como seu payload.
        # Pacotes ICMP podem ter um campo de dados (payload) que é preenchido.
        # Em um ataque de "ping da morte", esse payload é deliberadamente grande.
        
        # Verifica se existe um payload na camada ICMP
        if hasattr(pkt[ICMP], 'payload') and pkt[ICMP].payload:
            total_icmp_payload += len(pkt[ICMP].payload)
        
        # Nota: O ping da morte geralmente envolve fragmentação IP.
        # O Scapy reassembla pacotes fragmentados por padrão quando lê o PCAP,
        # então 'len(pkt[ICMP].payload)' deve dar o tamanho do payload reassemblado.
        # Se houver pacotes ICMP que não tem payload, eles serão contados como 0.

# O protocolo é ICMP, e o dado é o payload total.
protocol = "icmp"
total_payload = total_icmp_payload

# Exibir a flag no formato solicitado
print(f"Flag: mauactf{{{protocol}:{total_payload}bytes}}")