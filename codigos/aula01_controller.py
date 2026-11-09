# =============================================================
# Aula 01 — CONTROLLER (a placa do BOTÃO)
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
#
# Ligação: botão entre GPIO4 e GND (sem resistor: usamos o
#          pull-up interno da placa)
# =============================================================

import network, espnow, time
from machine import Pin

# >>> TROQUE pelo MAC que a placa do LED (target) mostrou <<<
TARGET_MAC = b'\xaa\xbb\xcc\xdd\xee\xff'

# --- 1. Liga o rádio (sem conectar em nenhuma rede) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)        # desliga primeiro: garante um começo "limpo"
sta.active(True)         # liga o rádio
sta.disconnect()

# --- 2. Prepara o ESP-NOW e cadastra o destino ---
e = espnow.ESPNow()
e.active(True)
e.add_peer(TARGET_MAC)   # coloca a outra placa na "agenda"

# --- 3. O botão ---
# PULL_UP: solto = 1, apertado = 0  (lógica invertida!)
botao = Pin(4, Pin.IN, Pin.PULL_UP)

estado_anterior = botao.value()
print("[controller] pronto! aperte o botão")

while True:
    estado = botao.value()

    # só envia quando o botão MUDA (apertou ou soltou)
    if estado != estado_anterior:
        if estado == 0:
            msg = b'1'           # apertado -> manda acender
        else:
            msg = b'0'           # solto    -> manda apagar

        ok = e.send(TARGET_MAC, msg)
        print("[controller] enviei", msg, "-> confirmado:", ok)

        estado_anterior = estado

    time.sleep_ms(20)    # pequena pausa: evita ler o "tremido" do botão
