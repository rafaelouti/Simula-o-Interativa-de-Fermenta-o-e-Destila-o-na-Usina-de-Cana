# Simulação Interativa de Fermentação e Destilação na Usina de Cana

Este projeto é uma simulação interativa desenvolvida em Python utilizando a biblioteca Tkinter. A ferramenta foi criada para visualizar, de forma didática e simplificada, os processos de fermentação e destilação presentes em uma usina de cana-de-açúcar.

## Visão Geral

A simulação possui duas etapas principais:

- **Fermentação:**  
  - Exibe um tanque virtual com uma barra de progresso que indica o avanço do processo.
  - Mostra parâmetros importantes como o volume de etanol produzido, o valor do **Brix** (indicador da concentração de açúcar) e a **temperatura** do tanque.

- **Destilação:**  
  - Após a fermentação, o processo de destilação é iniciado em uma nova tela.
  - Um aparelho virtual apresenta o recipiente coletor, onde o etanol é acumulado.
  - Exibe o **grau do álcool** (de 30% até 96%) e permite o controle de uma **bomba** que, quando ligada, acelera a destilação.

## Funcionalidades

- Atualização dos parâmetros em tempo real (a cada 1 segundo).
- Interface interativa com botões para iniciar os processos e controlar a bomba.
- Indicadores visuais para progresso, Brix, temperatura, volume de etanol e grau do álcool.

## Pré-requisitos

- **Python 3.x**
- **Tkinter:** Geralmente já vem instalado com o Python.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/simulacao-usina-cana.git
