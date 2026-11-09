# =============================================================
# Aula 04 — Preparando o rádio
# Minicurso 06 — ESP-NOW com MicroPython
# Placa: ESP32-C3 SuperMini (qualquer ESP32 serve)
#
# Baseado no trabalho de Noah Teodoro Ceiglinski Domingues
# Revisão: Prof. Rogério Malta Branco
# =============================================================

import network

# 1) Cria o "controle" do rádio, no modo ESTAÇÃO (STA)
sta = network.WLAN(network.WLAN.IF_STA)
print("1) Rádio ligado agora?", sta.active())

# 2) Desliga: apaga qualquer estado antigo
sta.active(False)
print("2) Depois do active(False):", sta.active())

# 3) Liga de novo: rádio "limpo", pronto para usar
sta.active(True)
print("3) Depois do active(True): ", sta.active())

# 4) Garante que NÃO está tentando entrar numa rede Wi-Fi
sta.disconnect()
print("4) Conectado a alguma rede?", sta.isconnected())

# 5) Curiosidade: em qual "canal" o rádio está?
print("5) Canal do rádio:", sta.config('channel'))
