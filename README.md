![Banner do minicurso](assets/banner.png)

# Minicurso 06 — ESP-NOW com MicroPython

**Comunicação sem fio entre duas placas ESP32, sem roteador e sem internet.**

Neste minicurso você vai fazer uma placa conversar com outra pelo ar. Começamos pelo clássico — **aperta o botão numa placa, acende o LED na outra** — e depois desmontamos esse exemplo peça por peça, bem devagar, até chegar a um projeto completo com confirmação, nova tentativa e medição de sinal.

> 🛠️ **Aulas de bancada.** O simulador Wokwi não simula ESP-NOW entre duas placas. Por isso, a maior parte deste minicurso é feita com hardware real (**ESP32-C3 SuperMini**). Quando uma parte puder ser simulada, a aula indica.

---

## 📋 Antes de começar

| Item | Detalhe |
|---|---|
| Placas | 2× ESP32-C3 SuperMini |
| Firmware | MicroPython 1.29.0 (ou mais recente) |
| IDE | Thonny |
| Componentes | 1 botão, 1 LED, resistor de 220 Ω, jumpers, protoboard (mais um LED RGB a partir da Seção 3) |
| Pré-requisito | Ter feito o MC01 (GPIO, botão e LED) |

---

## 📚 Aulas

### Seção 1 — Primeiro contato

| Aula | Tema | Status |
|---|---|---|
| [Aula 01](aulas/aula01-botao-led-sem-fio.md) | Botão numa placa, LED na outra | 🚧 em construção |
| [Aula 02](aulas/aula02-do-fio-para-o-ar.md) | O que aconteceu? Do fio para o ar | 🚧 em construção |
| [Aula 03](aulas/aula03-endereco-mac.md) | O endereço MAC de cada placa | 🚧 em construção |

### Seção 2 — Desmontando a Aula 01, peça por peça

| Aula | Tema | Status |
|---|---|---|
| Aula 04 | Preparando o rádio (`sta.active`) | 📝 planejada |
| Aula 05 | `add_peer`: a agenda de contatos | 📝 planejada |
| Aula 06 | `send` e `recv`: a fila de mensagens | 📝 planejada |
| Aula 07 | O ACK: o "recebido" do rádio | 📝 planejada |

### Seção 3 — Projeto: controller e target

| Aula | Tema | Status |
|---|---|---|
| Aula 08 | Tentar de novo: o retry | 📝 planejada |
| Aula 09 | O target com LED RGB | 📝 planejada |
| Aula 10 | RSSI e teste de distância | 📝 planejada |

### Seção 4 — Confiabilidade

Resposta de volta, numeração de mensagens, criptografia e integração com CLP. 📝 *planejada*

---

## 📁 Estrutura do repositório

```
minicurso_06-embarcados/
├── README.md              ← você está aqui
├── index.md               ← página do GitHub Pages
├── _config.yml
├── COMO-PUBLICAR.md
├── GUIA-CONSTRUCAO.md     ← convenções para quem constrói o curso
├── aulas/                 ← uma aula por arquivo
├── codigos/               ← códigos completos (.py) para abrir no Thonny
└── assets/
    ├── banner.png / banner.svg
    ├── img/               ← imagens e esquemas de montagem
    ├── gif/               ← animações das aulas
    └── wokwi-links.md
```

---

## 🙌 Créditos

- **Códigos-base, montagem e estudo do ESP-NOW:** Noah Teodoro Ceiglinski Domingues
- **Revisão técnica e pedagógica:** Prof. Rogério Malta Branco

Curso Técnico em Automação Industrial — IFRS Campus Rio Grande

---

## 📖 Referências

- [MicroPython — módulo `espnow`](https://docs.micropython.org/en/latest/library/espnow.html)
- [ESP-IDF — ESP-NOW (ESP32-C3)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/api-reference/network/esp_now.html)
- [Espressif — ESP-NOW](https://www.espressif.com/en/solutions/low-power-solutions/esp-now)
