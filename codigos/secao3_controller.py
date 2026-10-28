# Autor original: Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
#
# CONTROLLER - ESP32-C3 SuperMini (MicroPython)
# Ao ligar, envia o comando 'ligar' ao target via ESP-NOW.

import network, espnow, time

# >>> TROCA pelo MAC que o target imprime no serial <<<
TARGET_MAC = b'\xaa\xbb\xcc\xdd\xee\xff'

# --- Wi-Fi em estado conhecido ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)
sta.active(True)
sta.disconnect()
print("MAC do controller:", sta.config('mac'))

e = espnow.ESPNow()
e.active(True)
e.add_peer(TARGET_MAC)

# --- envio com confirmacao e retry ---
TENTATIVAS = 10
for n in range(1, TENTATIVAS + 1):
    ok = e.send(TARGET_MAC, b'ligar')   # sync=True: True so se o target confirmou
    print("[controller] envio", n, "-> confirmado:", ok)
    if ok:
        break
    time.sleep_ms(500)
else:
    print("[controller] ERRO: target nao respondeu")

print("[controller] pronto")
