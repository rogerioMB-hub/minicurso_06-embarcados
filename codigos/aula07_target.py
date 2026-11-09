# =============================================================
# Aula 07 — TARGET: dorme SEM ler, depois conta o que chegou
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network, espnow, time

# --- Prepara o rádio (Aula 04) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

DORMIR = 10        # segundos sem ler nada (mude no experimento!)

while True:
    print("[target] dormindo", DORMIR, "s... NÃO estou lendo nada!")
    time.sleep(DORMIR)

    lidas = 0
    ultima = None
    while e.any():
        mac, msg = e.recv(0)
        lidas = lidas + 1
        ultima = msg

    print("[target] acordei! li", lidas, "mensagens. A última foi:", ultima)
    print()
