# Simulação de Sistema Físico: Queda Livre

Repositório para o projeto da disciplina de Física para Ciência da Computação (2025.2) da Universidade Estadual de Santa Cruz (UESC).

---

## Informações Gerais

* **Proposta de projeto escolhida:** Projeto 4
* **Professor:** Prof. Orlando Katime Santrich
* **Alunos responsáveis pelo projeto:**
  * Arthur de Carvalho
  * Marcel Figueredo
  * Paulo de Pinho

* **Bibliotecas usadas:**
  * Numpy
  * Matplotlib
  * Math (nativa do Python)


---

## Proposta do Projeto

O objetivo deste projeto é desenvolver uma simulação computacional para analisar os princípios de conservação e dissipação de energia em um corpo em queda livre.

### Objetivos:

1.  **Simular um corpo em queda:**
    * Implementar os modelos matemáticos que descrevem o movimento de um objeto em queda sob a ação da gravidade e sob a ação da resistência do ar (se houver).
2.  **Calcular e mostrar graficamente as energias envolvidas:**
    * Calcular as energias cinética, potencial gravitacional e dissipada (se houver).
    * Gerar gráficos que ilustrem a variação de cada tipo de energia ao longo do tempo.
3.  **Validar a conservação ou não da energia total:**
    * Analisar os resultados para confirmar que a energia mecânica total se conserva nos sistemas ideais.
    * Mostrar que a energia mecânica total não se conserva na presença de forças dissipativas, validando o princípio da dissipação de energia.

---

## Como Executar o Projeto

Você pode executar o projeto de duas maneiras. O método com ambiente virtual (`venv`) é o mais recomendado, pois isola as dependências do projeto do restante do seu sistema.

### Método 1: Com Ambiente Virtual (Recomendado)

Este comando irá clonar o repositório, criar um ambiente virtual chamado `venv`, instalar as dependências (`numpy`, `matplotlib` e `notebook`) dentro dele e, em seguida, iniciar o Jupyter Notebook.

**Copie e cole no seu terminal:**

```bash
git clone https://github.com/CarvDev/Projeto-Fisica-UESC.git && cd Projeto-Fisica-UESC && python -m venv venv && venv/bin/pip install numpy matplotlib notebook && venv/bin/jupyter notebook Projeto.ipynb
```

### Método 2: Usando Pacotes do Sistema

Este método assume que você **já possui** o `git`, `python`, `numpy`, `matplotlib` e `jupyter notebook` instalados no seu sistema (globalmente).

**Copie e cole no seu terminal:**

```bash
git clone https://github.com/CarvDev/Projeto-Fisica-UESC.git && cd Projeto-Fisica-UESC && python -m venv venv && venv/bin/pip install numpy matplotlib notebook && venv/bin/jupyter notebook Projeto.ipynb
```