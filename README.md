# 🏭 Industrial Data Logger - Sistema de Mensageria e Alertas

Este projeto foi desenvolvido por **Gustavo** como um estudo técnico sobre **Sistemas de Monitoramento Industrial** utilizando Programação Orientada a Objetos. O software simula a captura de dados de sensores e alertas de segurança em uma fábrica.

## 🚀 Funcionalidades do Sistema

* **Fila de Mensagens (Buffer):** O sistema não processa os dados imediatamente; ele os armazena em uma fila, permitindo o processamento em lote (batch), o que otimiza recursos computacionais.
* **Gestão de Alarmes:** Classificação dinâmica de gravidade (ALTA, MEDIA, BAIXA) com respostas específicas para cada nível de alerta.
* **Registro de Produção:** Captura e validação de dados quantitativos de produtividade para integração com bancos de dados.
* **Arquitetura Baseada em Propriedades:** Uso do decorator `@property` para garantir uma interface de processamento limpa e profissional.

## 🛠️ Conceitos de POO Aplicados

* **Polimorfismo de Interface:** Uma única fila armazena diferentes tipos de pacotes (`Alarme` e `Produção`), tratando todos através de uma interface comum de processamento.
* **Herança Estruturada:** Todas as mensagens derivam de uma `PacoteBase`, compartilhando metadados como origem e data/hora.
* **Tratamento de Exceções:** Implementação de travas contra dados inválidos em campos numéricos, garantindo que o fluxo de produção não seja interrompido por erros de digitação.

## 📂 Organização Modular

* **`modulos.py`**: Contém a lógica das classes e as regras de processamento de cada tipo de pacote.
* **`main.py`**: Interface de comando que gerencia a entrada de dados e o gatilho de esvaziamento da fila.

---
*Projeto focado em automação industrial, filas de processamento e arquitetura de sistemas Python.*
