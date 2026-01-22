import requests
import socket
import ipaddress

dominio = "www.ifrn.edu.br"
timeout = 15


def resolver_ip(dominio):
    """Resolve domínio para IPv4 usando getaddrinfo"""
    try:
        infos = socket.getaddrinfo(dominio, None, socket.AF_INET)
        ip = infos[0][4][0]
        print(f"[+] IP resolvido para {dominio}: {ip}")
        return ip
    except socket.gaierror as e:
        print(f"[!] Erro ao resolver domínio: {e}")
        return None


def consultar_rdap_ip(ip):
    """Consulta RDAP e retorna o bloco CIDR"""
    print(f"[+] Consultando RDAP para o IP {ip} ...")

    url = f"https://rdap.registro.br/ip/{ip}"
    resposta = requests.get(url, timeout=timeout)

    if resposta.status_code != 200:
        print(f"[!] Erro RDAP IP: Status {resposta.status_code}")
        return None

    dados = resposta.json()

    cidrs = dados.get("cidr0_cidrs", [])
    if not cidrs:
        print("[!] CIDR não encontrado no RDAP")
        return None

    prefix = cidrs[0]["v4prefix"]
    length = cidrs[0]["length"]
    cidr = f"{prefix}/{length}"

    print(f"[+] Bloco CIDR encontrado: {cidr}")
    return cidr


def listar_ips(cidr):
    """Lista todos os IPs do bloco"""
    print("[+] Listando IPs do bloco...")
    rede = ipaddress.ip_network(cidr, strict=False)
    ips = list(rede.hosts())
    print(f"[+] Total de IPs: {len(ips)}")
    return ips


def dns_reverso(ip):
    """DNS reverso (PTR)"""
    try:
        hostname, _, _ = socket.gethostbyaddr(str(ip))
        return hostname
    except socket.herror:
        return None


def main():
    print("=== Descoberta de Bloco CIDR + DNS Reverso ===\n")

    ip = resolver_ip(dominio)
    if not ip:
        return

    cidr = consultar_rdap_ip(ip)
    if not cidr:
        return

    ips = listar_ips(cidr)

    print("\n--- DNS Reverso (IP → Domínio) ---")
    for ip in ips:
        ptr = dns_reverso(ip)
        if ptr:
            print(f"{ip} -> {ptr}")
        else:
            print(f"{ip} -> sem PTR")


if __name__ == "__main__":
    main()
