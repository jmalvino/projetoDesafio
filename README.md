# projetoDesafio









# estudo
# passa a passo do q foi feito e erros encontrados e como foi resolvidos 

# erro no git (criava o diretorio mas n enviava os arquivos)
foi resolvido deslogando da conta no vscode e logando novamente

# python
criação do projeto em python
> python -m venv projeto

criação do ambiente django
>django startproject projeto 

Ativando o projeto 
>.\projeto\Scripts\Activate.ps1

Com o ambiente virtual ativo, intalação
>pip install django 

# Erro ao tentar starta o projeto ('django-admin' não é reconhecido como um comando...)
Entra no powershell em modo adm e executa esse código
>Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

startando o projeto
>django-admin startproject djangoprojeto .

Inicializando o servidor
>python manage.py runserver

# pacientes

Criando pacientes
>django-admin startapp pacientes

# criando um médico

Criando medico
>django-admin startapp medicos

# criando pagina home

Criando medico
>django-admin startapp home

# etapa códigos
criei pagina urls.py em todos os app
criei uma pasta 'templates' em todos os app 
# (o django ja espera que tenha uma pasta com o nome templates então n precisa aportar)
criei as rotas dentro do settings do projeto principal e dos secudários dentro do views e urls

# criando os models
model medicos
model pacientes

# criando home com bootstrap


# erro de pagina n encontrada quando se está tentando voltar utilizando o 
>success_url = reverse_lazy('index')
# resolvido indo no arquivo de url e adicionando o NAME, se n adicionar ele n encontra
>path('', views.index, name="index")



