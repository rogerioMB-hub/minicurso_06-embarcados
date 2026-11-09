# =============================================================
# Aula 06 — TARGET: fica "ocupado" e depois lê a fila
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

while True:
    # 1) Finge que está ocupado fazendo outra coisa
    print("[target] ocupado por 5 segundos... (aperte o botão agora!)")
    time.sleep(5)

    # 2) Agora sim, vai olhar a fila
    print("[target] tem mensagem na fila?", e.any())

    while e.any():                  # enquanto tiver mensagem na fila...
        mac, msg = e.recv(0)        # RECV: tira UMA mensagem da fila
        print("    recebi:", msg)

    print("[target] fila vazia!")
    print()
