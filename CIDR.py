import requests

dominio = "www.ufrn.edu.br"
url_rdap = f"https://rdap.registro.br/domain/{dominio}"

try:
    resposta = requests.get(url_rdap, timeout=15)

    if resposta.status_code == 200:
        dados = resposta.json()

        titular = "Não identificado"
        pais = "Não identificado"
        responsavel = "Não identificado"
        servidores_dns = []

        # Entidades (titular / responsável)
        for entity in dados.get("entities", []):
            roles = entity.get("roles", [])
            vcard = entity.get("vcardArray", [])

            if len(vcard) > 1:
                for item in vcard[1]:
                    if item[0] == "fn":
                        if "registrant" in roles:
                            titular = item[3]
                        if "administrative" in roles:
                            responsavel = item[3]

        # Nameservers
        for ns in dados.get("nameservers", []):
            servidores_dns.append(ns.get("ldhName"))

        print("--- Consulta RDAP de Domínio ---")
        print(f"Domínio: {dominio}")
        print(f"Titular: {titular}")
        print(f"Responsável: {responsavel}")
        print(f"Servidores DNS:")
        for ns in servidores_dns:
            print(f" - {ns}")

    else:
        print(f"Erro RDAP: Status {resposta.status_code}")

except Exception as e:
    print(f"Erro: {e}")
