# Autor original: Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
#
# TARGET - ESP32-C3 SuperMini (MicroPython)
# Recebe o comando via ESP-NOW e roda a sequencia do LED RGB (catodo comum).
# LED RGB: R=GPIO0, G=GPIO1, B=GPIO3

import network, espnow, time, math
from machine import Pin, PWM

# --- Wi-Fi em estado conhecido (soft reset nao reseta o radio) ---
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(False)
sta.active(True)
sta.disconnect()
print("MAC do target:", sta.config('mac'))   # anota esse MAC e cola no controller.py

e = espnow.ESPNow()
e.active(True)

# --- LED RGB ---
pwm_r = PWM(Pin(0), freq=1000)
pwm_g = PWM(Pin(1), freq=1000)
pwm_b = PWM(Pin(3), freq=1000)

def set_rgb(r, g, b):
    """r,g,b de 0.0 a 1.0 (catodo comum: duty alto = mais brilho)"""
    pwm_r.duty_u16(int(r * 65535))
    pwm_g.duty_u16(int(g * 65535))
    pwm_b.duty_u16(int(b * 65535))

def apagar():
    set_rgb(0, 0, 0)

def hsv_to_rgb(h):
    """h de 0.0 a 1.0, saturacao e brilho maximos"""
    h6 = h * 6
    i = int(h6) % 6
    f = h6 - int(h6)
    q = 1 - f
    if i == 0: return 1, f, 0
    if i == 1: return q, 1, 0
    if i == 2: return 0, 1, f
    if i == 3: return 0, q, 1
    if i == 4: return f, 0, 1
    return 1, 0, q

def sequencia():
    print("[target] sinal recebido, aguardando 5 s")
    apagar()
    for s in range(5, 0, -1):
        print("[target] LED acende em", s)
        time.sleep(1)

    print("[target] LED ligado: 30 s de troca suave de cor")
    inicio = time.ticks_ms()
    DURACAO = 30_000
    CICLO = 10_000          # uma volta completa no circulo de cores a cada 10 s
    while time.ticks_diff(time.ticks_ms(), inicio) < DURACAO:
        t = time.ticks_diff(time.ticks_ms(), inicio)
        h = (t % CICLO) / CICLO
        set_rgb(*hsv_to_rgb(h))
        time.sleep_ms(20)

    print("[target] aviso: piscando vermelho 3x")
    for _ in range(3):
        set_rgb(1, 0, 0)
        time.sleep_ms(300)
        apagar()
        time.sleep_ms(300)

    apagar()
    print("[target] desligado")

apagar()
print("[target] aguardando comando...")

while True:
    mac, msg = e.recv()          # espera ate chegar algo (timeout padrao: 5 min -> (None, None))
    if msg:
        print("[target] recebi:", msg)
        if msg == b'ligar':
            sequencia()
            # descarta mensagens repetidas que chegaram durante a sequencia
            while e.any():
                e.recv(0)
            print("[target] aguardando comando...")
