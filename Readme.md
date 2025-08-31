# Instruções para Executar a Aplicação de Verificação de Par ou Ímpar

![Banner do Projeto](./assets/topo.png)

## Identificação do Projeto

- **Instituição:** Universidade Cruzeiro do Sul (UNICSUL)
- **Curso:** Superior em Desenvolvimento Back-end
- **Disciplina:** Projeto Integrador Transdisciplinar em Desenvolvimento Back-End II
- **Aluno:** Cleyton Alves da Silva
- **RGM:** 38309696
- **Período letivo:** 2025.2
- **Situação-problema:** 3 - Verificador de Paridade (Ímpar ou Par)

Esta aplicação é uma demonstração do projeto de intervenção para a situação-problema 3, onde desenvolvemos um verificador de paridade em Python utilizando Flask. A aplicação disponibiliza uma página HTML com CSS inline, permitindo ao usuário informar um número inteiro e receber em tempo real o resultado indicando se ele é **Par** ou **Ímpar**.

## Versão Online de Demonstração

Uma versão funcional desta aplicação poderá ser hospedada em serviços como **Render**, **Railway** ou **Heroku**.

**Exemplo de URL:**
[https://par-ou-impar.onrender.com](https://par-ou-impar.onrender.com)

![Demonstração](./assets/demo.gif)

> **Nota:** Em hospedagens gratuitas, a aplicação pode levar até 30 segundos para carregar no primeiro acesso, pois o serviço "adormece" após períodos de inatividade.

## Estrutura do Projeto

O projeto consiste em:

1. `app.py` - O arquivo principal com a aplicação Flask
2. `requirements.txt` - Arquivo com as dependências do projeto
3. `templates/` - Diretório com os templates HTML:
   - `index.html` - Página inicial com formulário para digitar o número e verificar paridade
4. `assets/` - Diretório com recursos gráficos (ex.: imagens, banners)

## Requisitos

- Python 3.8 ou superior
- Flask (`pip install flask`)

## Como Executar

### Opção 1: Clonar o repositório GitHub

Se preferir executar localmente:

```bash
git clone https://github.com/cleyton1986/par-ou-impar.git
cd par-ou-impar
pip install -r requirements.txt
python app.py
```

Acesse a aplicação em seu navegador:
`http://127.0.0.1:5000/`

### Opção 2: Configurar manualmente

Alternativamente, você pode configurar o projeto manualmente:

1. Crie a estrutura de diretórios:

   ```
   par-ou-impar/
   ├── app.py
   ├── requirements.txt
   ├── assets/
   │   └── topo.png
   └── templates/
       └── index.html
   ```

2. Copie o código do arquivo `app.py`, `requirements.txt` e do template para os respectivos arquivos.

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:

   ```bash
   python app.py
   ```

5. Acesse a aplicação em seu navegador:

   ```
   http://127.0.0.1:5000/
   ```

## Funcionalidades Implementadas

1. **Verificação de Paridade**:

   - Usuário informa um número inteiro
   - O sistema retorna em tempo real se é **Par** ou **Ímpar**

2. **Interface Simples**:

   - Página HTML com CSS inline
   - Formulário intuitivo e resultado exibido dinamicamente

3. **Tratamento de Erros**:

   - Entradas inválidas retornam mensagem de erro amigável

## Relação com o Projeto de Intervenção

Esta aplicação demonstra os conceitos apresentados no projeto de intervenção para a situação-problema 3:

- Uso de Python no back-end
- Criação de funções puras e reutilizáveis
- Estruturas condicionais para regras de negócio
- Integração entre back-end (Flask) e front-end (HTML/CSS)

## Contextualização Acadêmica

Este projeto foi desenvolvido como parte da disciplina **Projeto Integrador Transdisciplinar em Desenvolvimento Back-End II** da Universidade Cruzeiro do Sul, que tem como objetivo integrar conhecimentos sobre lógica de programação, back-end e desenvolvimento de aplicações web simples.

### Objetivos de Aprendizagem

Este projeto demonstra as seguintes competências e habilidades:

1. **Compreensão e aplicação de lógica condicional em Python**
2. **Criação de funções e reutilização de código**
3. **Integração de back-end com front-end simples**
4. **Uso de frameworks de mercado (Flask)**
5. **Desenvolvimento de aplicações de prova de conceito para problemas reais**
