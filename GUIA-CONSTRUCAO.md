# Guia de construção — Minicurso 06 (ESP-NOW)

Documento para quem **constrói** o curso. Reúne convenções, restrições e checklists.
Ao abrir um chat novo para continuar o curso, anexe este arquivo e o zip mais recente do repositório.

---

## 1. Perfil dos alunos e ritmo

- Os alunos têm **muitas dificuldades**. Ir **bem devagar** e dar espaço para a compreensão.
- **Um conceito por aula.** Se a aula começar a ter dois conceitos, dividir em duas.
- Começar cada Conceito com uma **analogia do dia a dia** antes do termo técnico.
- Pontos densos (rádio, MAC, fila, ACK, RSSI) ganham **animação/GIF**.
- Código apresentado **em pedaços**, explicados um a um, e só depois inteiro.
- Experimentos em forma de perguntas curtas: *"o que acontece se…?"*.
- Objetivos de cada aula sempre explícitos.

## 2. Estrutura padrão de cada aula

Arquivo `aulas/aulaNN-nome.md` com front matter Jekyll:

```yaml
---
layout: default
title: "Aula NN — Título"
---
```

Ordem das seções:

1. **Objetivos**
2. **Conceito** (analogia → termo técnico → GIF)
3. **Montagem** — esquema/foto da bancada. *Neste curso substitui o `diagram.json`*, exceto nas aulas que rodam no Wokwi.
4. **Código** — em pedaços, depois completo
5. **Experimento** (perguntas)
6. **Desafio** (principal + bônus)
7. **Resumo**
8. Navegação ← →

Conceito usado antes de ser ensinado → criar aula **Extra** (`aulaNN-extra-tema.md`) com nota de referência. **Nunca renumerar** aulas existentes.

## 3. Hardware de referência — ESP32-C3 SuperMini

| Uso | Pino | Observação |
|---|---|---|
| Botão (controller, aula01) | GPIO4 | `Pin.PULL_UP` interno, botão ligado ao GND |
| LED simples (target, aula01) | GPIO5 | resistor 220 Ω |
| LED RGB cátodo comum (target, Seção 3) | R=GPIO0, G=GPIO1, B=GPIO3 | um resistor por cor |

⚠️ **Pinos a evitar na C3:**

- **GPIO2, GPIO8, GPIO9** — strapping (podem atrapalhar o boot).
- **GPIO8** é também o LED embutido da SuperMini, com **lógica invertida** — não usar como "LED fácil" com iniciantes.
- **GPIO18/19** — USB (comunicação com o Thonny).

Sempre avisar na aula quando um pino escolhido puder dar problema.

## 4. Restrições do ESP-NOW no MicroPython

- **Wokwi não simula ESP-NOW entre duas placas** → aulas de bancada. Partes de placa única (ex.: LED RGB/HSV) podem ter Wokwi.
- Interface Wi-Fi precisa estar ativa (`sta.active(True)`), sem conectar em rede. Sem isso: `ESP_ERR_ESPNOW_IF`.
- Soft reset **não** reseta o rádio → os códigos fazem `active(False)` e depois `active(True)`.
- Para **enviar**, o destino precisa de `add_peer(mac)`. Para receber sem criptografia, não.
- As duas placas no **mesmo canal**. Conectar uma delas a um roteador muda o canal.
- `send()` retorna `True` quando chega o **ACK do rádio** — isso **não** garante que o programa leu a mensagem.
- `recv()` sem argumento espera o timeout padrão (5 min) e então retorna `(None, None)` — tratar com `if msg:`.
- MAC impresso pode ter bytes mostrados como caracteres (ex.: `=`): é normal. Nas aulas usar o placeholder `b'\xaa\xbb\xcc\xdd\xee\xff'` e explicar.
- Thonny fala com uma placa por vez → duas janelas para monitorar as duas.

## 5. Animações (GIF)

- Geradas com **Pillow**, na identidade visual do curso: fundo azul-escuro (`#0d1b34`), traços de circuito (`#1e466e`), destaque verde (`#50dc78`), texto branco, fonte monoespaçada para rótulos.
- Salvar em `assets/gif/aulaNN-tema.gif`.
- Curtas (até ~6 s), em loop, uma ideia só.
- Imagens estáticas (diagramas) podem vir do ChatGPT/DALL-E → `assets/img/`.

## 6. Créditos

- Material-base (códigos, montagem, estudo do ESP-NOW): **Noah Teodoro Ceiglinski Domingues**.
- Revisão técnica e pedagógica: **Prof. Rogério Malta Branco**.
- Aulas baseadas no material do Noah levam no topo:
  > *Baseado no trabalho de Noah Teodoro Ceiglinski Domingues · Revisão: Prof. Rogério Malta Branco*
- Códigos dele levam no cabeçalho:
  ```python
  # Autor original: Noah Teodoro Ceiglinski Domingues
  # Revisão: Prof. Rogério Malta Branco
  ```

## 7. Publicação

- Fluxo pelo navegador (arrastar arquivos) ou por pull request criado pelo Claude.
- Sempre informar: arquivos (novos / substituir / remover), título do commit e descrição, separados.
- Commits: `feat(aulaNN): descrição` (conventional commits).
- Links do `index.md` com URL absoluta: `https://rogeriomb-hub.github.io/minicurso_06-embarcados/aulas/aulaNN-nome`.
- Google Sites: botões com link em nova aba (não usar iframe).

## 8. Checklist por aula

- [ ] Objetivos explícitos
- [ ] Um conceito só
- [ ] Analogia antes do termo técnico
- [ ] GIF nos pontos densos
- [ ] Código em pedaços + completo, comentado
- [ ] Alerta de pinos, se houver
- [ ] Créditos, se usa material do Noah
- [ ] Testado na bancada pelo professor
- [ ] Linha no README e no index atualizadas
