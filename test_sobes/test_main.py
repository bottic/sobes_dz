import pytest
from sobes.main import isbalansed
fixture = {
    ('(((([{}]))))', 'balansed'),
    ('[([])((([[[]]])))]{()}', 'balansed'),
    ('{{[()]}}', 'balansed'),
    ('}{}', 'not balansed')
}

@pytest.mark.parametrize('string_to_test, result', fixture)
def test_isbalansed(string_to_test, result):
    calc_res = isbalansed(string_to_test)
    assert calc_res == result