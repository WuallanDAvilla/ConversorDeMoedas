# Conversor de Moedas Moderno em Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.2-green?logo=tkinter&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.31.0-red)

Um conversor de moedas completo e robusto com interface gráfica moderna construída em Python. O projeto é autossuficiente, atualizando as taxas de câmbio e a lista de moedas disponíveis automaticamente, mas também funciona offline utilizando os últimos dados salvos.

<img src="imagem.png" alt="Screenshot da aplicação" width="600"/>

## ✨ Funcionalidades Principais

- **Interface Gráfica Moderna:** Desenvolvido com a biblioteca **CustomTkinter** para um visual limpo e agradável em modo escuro.
- **Atualização Automática:** Ao iniciar com acesso à internet, o aplicativo busca e salva as listas mais recentes de moedas e conversões da **AwesomeAPI**, garantindo que os dados estejam sempre atualizados.
- **Operação Offline:** Caso não haja conexão, o programa utiliza os últimos dados salvos localmente (`moedas.xml` e `conversoes.xml`), garantindo sua funcionalidade a qualquer momento.
- **Cotação em Tempo Real:** A conversão utiliza a cotação mais recente no momento do cálculo, buscando o valor diretamente da API.
- **Inversão Rápida:** Um botão **"⇄"** permite inverter facilmente a moeda de origem e destino.
- **Funcionalidades de Usabilidade:** Inclui um botão para **"Limpar"** os campos e reiniciar o cálculo de forma prática.
- **Ampla Cobertura de Moedas:** Suporte para todas as moedas e pares de conversão disponibilizados pela API, com uma lista de consulta na própria interface.

## 🛠️ Tecnologias Utilizadas

- **Python 3:** Linguagem principal do projeto.
- **CustomTkinter:** Para a criação da interface gráfica moderna.
- **Requests:** Para fazer as requisições HTTP à API de cotações.
- **XmlToDict:** Para converter os dados XML da API em um formato utilizável em Python.

## ⚙️ Instalação e Execução

Para executar este projeto localmente, siga os passos abaixo.

#### **1. Pré-requisitos**

- Ter o [Python 3](https://www.python.org/downloads/) instalado em seu sistema.

#### **2. Clone o Repositório**

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git]
cd seu-repositorio
```

#### **3. Instale as Dependências**

Abra um terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install customtkinter requests xmltodict
```

#### **4. Execute a Aplicação**

Com as dependências instaladas, basta executar o arquivo principal:

```bash
python main.py
```

> **Como os arquivos `.xml` funcionam?**
>
> Ao executar o programa pela primeira vez com internet, ele criará ou atualizará os arquivos `moedas.xml` e `conversoes.xml` na pasta do projeto. Se você executar sem internet, ele usará esses arquivos já existentes.

## 🧠 Aprendizados

Construindo esse projeto, o grupo desenvolveu maior maestria na linguagem de programação Python, no Visual Studio Code, com a importação e aplicação de bibliotecas. A equipe aprimorou o vinculo de trabalho em equipe entre os integrantes. Ao construir o código, houve problemas que persistiram na codificação, porém com um pouco de atenção eles foram superados. Um dos grandes aprendizados do grupo foi explorar novas funcionalidades na documentação da biblioteca e desenvolver outras funções.

## 👨‍💻 Autores e Créditos

Projeto realizado pela sala do 2º ano da escola **SESI de Osvaldo Cruz CE283**, no V itinerário, junto ao **SENAI**.

### Alunos

- Ariel Thiago Bisoli Ribeiro Nº18
- João Rafael Zanuto Nº11
- Matheus de Souza Alves Pereira Nº12
- Wuallan Meira Gomes Davila Nº23

### Professores

- Wagner de Campos Sabor Junior
- Irineu Francisco de Souza
