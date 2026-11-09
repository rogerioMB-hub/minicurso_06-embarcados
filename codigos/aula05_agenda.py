# =============================================================
# Aula 05 — add_peer: a agenda de contatos
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini (qualquer ESP32 serve)
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network, espnow

# --- Prepara o rádio (Aula 04) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)
sta.active(True)
sta.disconnect()

# --- Liga o ESP-NOW ---
e = espnow.ESPNow()
e.active(True)

# >>> TROQUE pelo MAC do seu target (Aula 03) <<<
TARGET_MAC = b'\xaa\xbb\xcc\xdd\xee\xff'

# Um MAC que NÃO vamos colocar na agenda
OUTRO_MAC = b'\x11\x22\x33\x44\x55\x66'

# 1) Como está a agenda no começo?
print("1) Agenda no começo:", e.get_peers())

# 2) Salva o target na agenda
e.add_peer(TARGET_MAC)
print("2) Salvei o target na agenda!")

# 3) Quantos contatos tem agora?
print("3) Contatos na agenda:", len(e.get_peers()))

# 4) Manda uma mensagem para quem ESTÁ na agenda
ok = e.send(TARGET_MAC, b'1')
print("4) Mandei para o target. Confirmado?", ok)

# 5) Tire o # da linha abaixo para mandar para quem NÃO está na agenda
# e.send(OUTRO_MAC, b'1')

print("Fim!")
