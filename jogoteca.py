from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'nome': "Jean Land",
        'profissao': "Desenvolvedor Full Stack",
        'slogan': "Transformo necessidades em aplicações reais, criando interfaces envolventes e funcionais. Desenvolvo sistemas web através da minha paixão pela tecnologia, contribuindo com soluções inovadoras e eficazes para desafios complexos.",
        'sobre': "Sou estudante de Análise e Desenvolvimento de Sistemas pela Unicesumar e Engenharia de Software pela Uninter. Minha meta está no desenvolvimento de software. Gosto de aprender com profundidade, resolvendo problemas reais.",
        'evolucao': "Aprendi programação inicialmente com Python e rapidamente me identifiquei com a lógica por trás do código. Hoje, estou focado em dominar o desenvolvimento web com HTML, CSS, JavaScript, Git, e as tecnologias que me levarão a ser full stack, mesmo preferindo a parte mais técnica do back-end ao design visual.",
        'portfolio': "Portfólio",
        'apresentacao': "Meu portfólio pessoal com projetos e experiências.",
        'jogo': "Jogo do Número Secreto",
        'interativo': "Jogo interativo para adivinhar números.",
        'logica': "Lógica simples e divertida.",
        'feedback': "Feedback instantâneo para o usuário.",
        'codeconnect': "CodeConnect",
        'educacao': "Plataforma para educação em programação assíncrona.",
        'restaurante': "Restaurante API",
        'api': "API para gestão de pedidos de restaurante.",
        'gestao': "Gestão eficiente e moderna.",
        'email': "jean.land@email.com",
        'dinamismo': "Dinamismo e inovação"
    }
    return render_template('lista.html', **context)

if __name__ == '__main__':
    app.run(debug=True)