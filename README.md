# SINÔNIMO API

A sinônimo API é uma simples e contém apenas um endpoint que recebe com argumento um conjunto de palavras e retorna seus respectivas sinõnimos. A API faz uma busca no site do [dicio](https://www.dicio.com.br/) via web scraping simples.

# 1 - Instalação

1. Baixando a API

```bash
git clone https://github.com/LuisHenrique01/API_SIG.git
```
2. Criando o ambiente virtual    
   * Observação: Python >= 3.8

```bash
python -m venv venv
```

```bash
 source venv/bin/activate 
```

# 2 - Configurando
1. Instalando dependências
```bash 
pip install -r requirements.txt 
```

# 3 - Como usar
1. Inicialize o servidor
```bash
python manage.py runserver
```

* Vai inicializar umm servidor no [localhost](http://127.0.0.1:8000/)

2. Entre no endpoint [sinonimo](http://127.0.0.1:8000/sinonimo/)

3. Use o argumento "q" para requisitar os sinônimos desejado.

# 4 Exemplo
* Caso queira buscar por sinônimos de "palavra"
  * [http://127.0.0.1:8000/sinonimo/?q=palavra](http://127.0.0.1:8000/sinonimo/q=palavra)

* Caso queira buscar por sinônimos de "palavra" e "casa"
  * [http://127.0.0.1:8000/sinonimo/?q=palavra%20casa](http://127.0.0.1:8000/sinonimo/q=palavra%20casa)
  * O "%20" representa o caracter " " em ASCII 20

* Você também pode ultilizar o caracter "+" para separar as palavras
 * [http://127.0.0.1:8000/sinonimo/?q=palavra+casa+morador](http://127.0.0.1:8000/sinonimo/?q=palavra+casa+morador)

## IMPORTANTE!
### **Cuidado com o número de palavras passadas a cada request na API pois isso pode deixar o tempo de resposta lento ou até mesmo inviabilizar o retorno**