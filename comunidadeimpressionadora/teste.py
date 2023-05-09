from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

# with app.app_context():
#    database.create_all()

# with app.app_context():
#     database.drop_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email="Lira@gmail.com", senha="123456")
#     usuario2 = Usuario(username="joao", email="Joao@gmail.com", senha="abcdefgtt")
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()

with app.app_context():
    usuario_teste = Usuario.query.filter_by(id=2).first()
    print(usuario_teste)
    print(usuario_teste.username)
    print(usuario_teste.email)
    print(usuario_teste.senha)
    print(usuario_teste.cursos)



# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
    # primeiro_usuario = meus_usuarios[2]
    # print(primeiro_usuario.id)
    # print(primeiro_usuario.email)
    # print(primeiro_usuario.posts)

# with app.app_context():
#         meu_post = Post(id_usuario=1, titulo="Primeiro posto do lira", corpo="Lira Voando")
#         database.session.add(meu_post)
#         database.session.commit()

# with app.app_context():
#     post = Post.query.filter_by(id=4).first()
#     print(post.corpo)

#