# =============================================================
# Aula 03 — Descobrindo o MAC da placa
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini (qualquer ESP32 serve)
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network

# Liga o rádio (sem conectar em rede nenhuma)
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)

mac = sta.config('mac')      # pega o endereço da placa (6 bytes)

# 1) Do jeito que o Python mostra (é este que vai no código!)
print("Para colar no código:", mac)

# 2) Quantos bytes tem?
print("Tamanho:", len(mac), "bytes")

# 3) Do jeito "bonito", que se vê em etiquetas e roteadores
partes = []
for b in mac:                     # passa por cada byte
    partes.append("%02x" % b)     # escreve em hexadecimal, sempre com 2 dígitos
print("Jeito bonito:", ":".join(partes))
