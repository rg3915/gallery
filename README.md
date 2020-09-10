# gallery

Exemplo de projeto Django para upload e download de arquivos.

## Este projeto foi feito com:

* [Django 2.2.16](https://www.djangoproject.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/gallery.git
cd gallery
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Screenshot

![alt text](gallery_index.png)

![alt text](gallery_.png)