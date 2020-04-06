from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Vítor', email='vitor.campos@engenharia.ufjf.br'),
            Usuario(nome='AUMGN', email='aumgn@sociedadenovoaeon.org')
        ],
        [
            Usuario(nome='Vítor', email='vitor.campos@engenharia.ufjf.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vitor.campos@engenharia.ufjf.br',
        'Teste de título',
        'Texto de teste'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Vítor', email='vitor.campos@engenharia.ufjf.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'aumgn@sociedadenovoaeon.org',
        'Teste de título',
        'Texto de teste'
    )
    enviador.enviar.assert_called_once_with(
        'aumgn@sociedadenovoaeon.org',
        'vitor.campos@engenharia.ufjf.br',
        'Teste de título',
        'Texto de teste'
    )
