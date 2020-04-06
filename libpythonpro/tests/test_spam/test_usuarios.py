from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Vitor', email='vitor.campos@engenharia.ufjf.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Vitor', email='vitor.campos@engenharia.ufjf.br'),
        Usuario(nome='AUMGN', email='vitor.campos@engenharia.ufjf.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
