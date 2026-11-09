# =============================================================
# Aula 01 — TARGET (a placa do LED)
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
#
# Ligação: GPIO5 -> resistor 220 Ω -> LED (perna longa) ;
#          LED (perna curta) -> GND
# =============================================================

import network, espnow
from machine import Pin

# --- 1. Liga o rádio (sem conectar em nenhuma rede) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)        # desliga primeiro: garante um começo "limpo"
sta.active(True)         # liga o rádio
sta.disconnect()

# Mostra o "endereço" desta placa. ANOTE e cole no controller!
print("MAC desta placa (target):", sta.config('mac'))

# --- 2. Prepara o ESP-NOW ---
e = espnow.ESPNow()
e.active(True)

# --- 3. O LED ---
led = Pin(5, Pin.OUT)
led.value(0)             # começa apagado

print("[target] esperando mensagens...")

while True:
    mac, msg = e.recv()  # espera chegar uma mensagem
    if msg:              # se chegou algo (e não foi só tempo esgotado)
        print("[target] recebi:", msg)
        if msg == b'1':
            led.value(1)     # acende
        elif msg == b'0':
            led.value(0)     # apaga
