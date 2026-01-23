#Seminário segurança de dados

📡 Análise de Infraestrutura de Domínios e Serviços Web

Este repositório reúne três algoritmos em Python voltados à análise de infraestrutura de redes e serviços web, utilizando técnicas de consulta RDAP, resolução DNS, DNS reverso e verificação de métodos HTTP suportados.

O objetivo é demonstrar, de forma prática, como coletar informações públicas sobre domínios, blocos IP e comportamento de servidores web, respeitando boas práticas e uso educacional.

🧩 Algoritmos Implementados
🔹 Algoritmo 1 — Consulta RDAP de Domínio
📌 Objetivo

Realizar uma consulta RDAP (Registration Data Access Protocol) para obter informações públicas de registro de um domínio.

🔍 Informações Coletadas

Titular do domínio

Responsável administrativo

Servidores DNS autoritativos

🛠️ Tecnologias Utilizadas

Python 3

Biblioteca requests

Serviço RDAP do registro.br

⚙️ Funcionamento

O script envia uma requisição HTTP GET para o endpoint RDAP do domínio.

Caso a resposta seja válida (HTTP 200), o JSON retornado é analisado.

As entidades do domínio são processadas para identificar:

Titular (registrant)

Responsável administrativo (administrative)

Os servidores DNS são listados a partir da resposta RDAP.

📤 Exemplo de Saída
--- Consulta RDAP de Domínio ---
Domínio: www.ufrn.edu.br
Titular: Universidade Federal do Rio Grande do Norte
Responsável: Não identificado
Servidores DNS:
 - ns1.ufrn.br
 - ns2.ufrn.br

🔹 Algoritmo 2 — Descoberta de Bloco CIDR e DNS Reverso
📌 Objetivo

Identificar o bloco CIDR ao qual um domínio pertence e realizar DNS reverso (PTR) em todos os IPs do bloco.

🔍 Etapas Executadas

Resolução do domínio para IPv4

Consulta RDAP do IP para obter o bloco CIDR

Listagem de todos os IPs válidos do bloco

Consulta DNS reversa (PTR) para cada IP

🛠️ Tecnologias Utilizadas

Python 3

requests

socket

ipaddress

Serviço RDAP do registro.br

⚙️ Funcionamento

O domínio é resolvido via getaddrinfo.

O IP obtido é consultado no RDAP para identificar o prefixo CIDR.

Todos os hosts do bloco são enumerados.

Para cada IP, tenta-se obter o nome associado via DNS reverso.

📤 Exemplo de Saída
[+] IP resolvido para www.ifrn.edu.br: 200.17.xxx.xxx
[+] Bloco CIDR encontrado: 200.17.160.0/20
[+] Total de IPs: 4094

--- DNS Reverso ---
200.17.160.10 -> servidor.ifrn.edu.br
200.17.160.11 -> sem PTR


📌 Observação: esse tipo de análise deve ser feito apenas para fins acadêmicos ou em ambientes autorizados.

🔹 Algoritmo 3 — Verificação de Métodos HTTP Permitidos
📌 Objetivo

Identificar quais métodos HTTP um servidor web aceita, auxiliando na análise de segurança e configuração do serviço.

🔍 Métodos Testados

OPTIONS

GET

POST

PUT

DELETE

TRACE

CONNECT

🛠️ Tecnologias Utilizadas

Python 3

Biblioteca requests

⚙️ Funcionamento

Para cada método HTTP, o script envia uma requisição ao servidor.

O código de status HTTP retornado é registrado.

É possível identificar métodos:

Permitidos (200, 204, 405)

Bloqueados ou não implementados (403, 501)

📤 Exemplo de Saída
GET -> 200 (OK)
POST -> 405 (Method Not Allowed)
TRACE -> 501 (Not Implemented)
CONNECT -> 403 (Forbidden)


📌 Importância: métodos como TRACE e CONNECT podem representar riscos se habilitados indevidamente.

🎯 Objetivo Educacional

Este projeto tem finalidade acadêmica e didática, auxiliando no entendimento de:

Funcionamento do protocolo RDAP

Estrutura de registros de domínios e IPs

Relação entre DNS direto e reverso

Configuração e exposição de métodos HTTP em servidores web

Introdução à análise de superfície de ataque

⚠️ Aviso Legal

Este repositório não deve ser utilizado para atividades ilegais.
Todas as análises devem ser realizadas apenas em domínios próprios, ambientes de teste ou sistemas com autorização explícita.

📚 Referências

RFC 7482 — Registration Data Access Protocol (RDAP)

https://registro.br

https://rdap.registro.br

OWASP — HTTP Methods Security
