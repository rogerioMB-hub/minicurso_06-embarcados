# =============================================================
# Aula 06 — CONTROLLER: manda 3 mensagens a cada aperto
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini — botão entre GPIO4 e GND
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network, espnow, time
from machine import Pin

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

botao = Pin(4, Pin.IN, Pin.PULL_UP)     # solto = 1, apertado = 0
contador = 0                            # numera as mensagens

print("[controller] aperte o botão para mandar 3 mensagens")

while True:
    if botao.value() == 0:              # apertou!
        for i in range(3):              # manda 3 mensagens seguidas
            contador = contador + 1
            texto = "msg " + str(contador)
            e.send(TARGET_MAC, texto)   # SEND: coloca a mensagem no ar
            print("[controller] enviei:", texto)
        while botao.value() == 0:       # espera soltar o botão
            time.sleep_ms(20)
    time.sleep_ms(20)
