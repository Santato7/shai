# shai (Shell AI) README

**shai** é uma ferramenta de linha de comando (CLI) que consome APIs de IA para responder perguntas e gerar comandos Bash ou código em várias linguagens de programação. A ferramenta utiliza a biblioteca `rich` para fornecer saídas estilizadas e claras no terminal.

## Requisitos

- Python
- pip
- git

## Instalação

### Linux

```sh
curl -fsSL https://raw.githubusercontent.com/santato7/shai/main/install.sh | bash
```

## Uso

```sh
shai [options] <prompt>
```

## Opções

- `-h` ou `--help`: Mostra esta mensagem de ajuda.
- `-b` ou `--bash`: Gerar comandos Bash.
- `-c` ou `--code`: Gerar código em várias linguagens de programação.

Se nenhum argumento de opção for passado, **shai** atua como um "assistente geral".

## Exemplo

```sh
shai "Como fazer um bolo?"
```

```sh
shai -c "Como criar uma função em Python que soma dois números?"
```

## Configuração

**shai** requer uma chave de API do Google Gemini para funcionar. Durante a instalação, você será solicitado a inserir sua chave de API. A chave será armazenada em um arquivo de configuração localizado em `~/.config/shai/shai.conf`.

Para obter sua chave de API do Gemini, acesse [Google Gemini API](https://developers.generativeai.google/documentation) e siga as instruções para criar uma chave de API.
