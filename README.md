# EngSoftw_Atividade5

Atividade sobre GitHub Actions executando testes em multiplos sistemas
operacionais e versoes de Python.

## Programa

O projeto implementa uma calculadora simples em Python com operacoes de:

- soma
- subtracao
- multiplicacao
- divisao
- potencia

Exemplo de uso:

```bash
python calculator.py add 2 3
python calculator.py divide 10 2
python calculator.py power 2 5
```

## Testes

Os testes unitarios ficam em `tests/test_calculator.py` e cobrem as operacoes
principais, erro de divisao por zero e erro para operacao desconhecida.

Para executar localmente:

```bash
python -m unittest discover -s tests -v
```

## GitHub Actions

O workflow esta em `.github/workflows/ci.yml` e roda automaticamente em:

- todo `push`
- todo `pull_request`

A matriz do GitHub Actions executa o build e os testes em:

- `ubuntu-latest`
- `macos-latest`
- `windows-latest`

E nas versoes de Python:

- `3.11`
- `3.12`

Isso gera 6 execucoes no total: 3 sistemas operacionais x 2 versoes de Python.
