# =============================================================
# Aula 07 — CONTROLLER: manda e mostra o ACK
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network, espnow, time

# >>> TROQUE pelo MAC do seu target <<<
TARGET_MAC = b'\xaa\xbb\xcc\xdd\xee\xff'

# --- Prepara o rádio (Aula 04) e a agenda (Aula 05) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
e.add_peer(TARGET_MAC)

contador = 0
confirmadas = 0

while True:
    contador = contador + 1

    ok = e.send(TARGET_MAC, str(contador))   # ok = o ACK chegou?
    if ok:
        confirmadas = confirmadas + 1

    print("[controller] enviei", contador, "-> ACK:", ok,
          "| confirmadas até agora:", confirmadas)

    time.sleep_ms(500)                       # manda 2 por segundo
