from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola():
    return render_template(
        'lista.html',
        nome="Jean Land",
        profissao="Desenvolvedor",
        slogan="Transformando ideias em código.",
        sobre="Apaixonado por tecnologia e programação.",
        evolucao="Sempre buscando evolução e novos desafios.",
        portfolio="Portfólio",
        apresentacao="Meu portfólio pessoal com projetos e experiências.",
        jogo="Jogo do Número Secreto",
        interativo="Jogo interativo para adivinhar números.",
        logica="Lógica simples e divertida.",
        feedback="Feedback instantâneo para o usuário.",
        codeconnect="CodeConnect",
        educacao="Plataforma para educação em programação assíncrona.",
        restaurante="Restaurante API",
        api="API para gestão de pedidos de restaurante.",
        gestao="Gestão eficiente e moderna.",
        email="jean.land@email.com",
        dinamismo="Dinamismo e inovação"
    )

if __name__ == '__main__':
    app.run(debug=True)
