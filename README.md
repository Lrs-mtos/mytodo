# MyToDo
Este respositório contém um projeto de _checklist_ utilizando o framework Django (python). Nele, é possível que o usuário se cadastre, faça login, adicione tarefas, as marque como pendentes ou concluídas. Também é possível excluí-las.

---
## Pré requisitos
Aqui estão listados os comandos essenciais para que o projeto funcione.
Caso você não tenha Python3 instalado, instale-o com:

```bash
sudo apt update
sudo apt-get install python3.10
```

Instale o instalador de pacotes do Python
```bash
sudo apt install python3-pip
```
Instale o ambiente virtual do Python:

```bash
apt install python3.10-venv
```

## Execução

Crie um ambiente virtual
```bash
python3 -m venv nome_do_ambiente_virtual
```

Ative o ambiente virtual
```bash
source nome_do_ambiente_virtual/bin/activate
```
Instale o Django no ambiente virtual

```bash
pip3 install django
```

Quando não for mais interagir com o projeto, lembre-se de desativar o ambiente virtual
```bash
deactivate
```

