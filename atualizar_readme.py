import os

UNICODE_PRETO = "\u2591"
UNICODE_BRANCO = "\u2588"
TEXTO_PADRAO = "# Exercícios beecrowd\n\nPropostas de resoluções dos exercícios do site [beecrowd](https://www.beecrowd.com.br/) (antigo URI online judge).\n\nAtualmente existem resoluções para exercícios nas seguintes linguagens (divididos entre **completos** e **incompletos**):\n\n"


def calcular_barra(tamanho: int, total: int, completo: int) -> tuple():
    fator = tamanho / total
    branco = int(completo * fator)
    preto = tamanho - branco

    return (preto, branco)


def formatar_progresso(estatisticas: dict) -> str:
    tentados, completos = estatisticas.values()
    pretos, brancos = calcular_barra(30, tentados, completos)
    percentual = round(((completos / tentados) * 100), 2)

    return f"{completos:4} completos de {tentados:4} tentados {UNICODE_BRANCO * brancos}{UNICODE_PRETO * pretos} {percentual:.2f}%"


def obter_totais(dir: str) -> int:
    if os.path.isdir(dir):
        todos_arquivos = [file[2] for file in os.walk(dir)][0]
        todos_arquivos = list(dict.fromkeys([file[0:4] for file in todos_arquivos]))
        return (len(todos_arquivos), todos_arquivos)

    return (0, [])


def gera_estatisticas():
    estatisticas = {}
    exercicios = {}
    total_geral_completos = []
    total_geral_incompletos = []

    for language in os.listdir(os.curdir):
        if (os.path.isdir(language)) and (not language.startswith(".")):
            total_completos, lista_completos = obter_totais(
                os.path.join(language, "completos")
            )
            total_incompletos, lista_incompletos = obter_totais(
                os.path.join(language, "incompletos")
            )

            total_geral_completos.extend(lista_completos)
            total_geral_incompletos.extend(lista_incompletos)

            exercicios[language] = {
                "tentados": total_completos + total_incompletos,
                "completos": total_completos,
            }

    for linguagem, valores in exercicios.items():
        estatisticas[linguagem] = formatar_progresso(valores)

    total_completo = len(list(dict.fromkeys(total_geral_completos)))
    total_geral = total_completo + len(list(dict.fromkeys(total_geral_incompletos)))

    return (estatisticas, {"total": total_geral, "completo": total_completo})


def main():
    estatisticas, gerais = gera_estatisticas()

    with open(os.path.join(os.curdir, "readme.md"), "w") as f:
        f.write(TEXTO_PADRAO)

        f.write(f"Total geral: `{formatar_progresso(gerais).lstrip()}`\n\n")

        for linguagem, valor in estatisticas.items():
            f.write(f"- [{linguagem}](./{linguagem}/)\n\n")
            f.write("```txt")
            f.write(f"\n{valor}\n")
            f.write("```\n\n")


if __name__ == "__main__":
    main()
