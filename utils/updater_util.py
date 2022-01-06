import os

BLACK_UNICODE = "\u2591"
WHITE_UNICODE = "\u2588"
DEFAULT_TEXT = "# Exercícios beecrowd\n\nPropostas de resoluções dos exercícios do site [beecrowd](https://www.beecrowd.com.br/) (antigo URI online judge).\n\nAtualmente existem resoluções para exercícios nas seguintes linguagens (divididos entre **completos** e **incompletos**):\n\n"

def calculate_white_black_quantity(size: int, total: int, complete: int):
    ratio = size / total
    white = int(complete * ratio)
    black = size - white

    return (black, white)


def format_progress_text(stats: dict):
    tried, complete = stats.values()
    black_squares, white_squares = calculate_white_black_quantity(30, tried, complete)
    percentual = round(((complete / tried) * 100), 2)

    return f"{complete:4} completos de {tried:4} tentados {WHITE_UNICODE * white_squares}{BLACK_UNICODE * black_squares} {percentual:.2f}%"


def get_totals(directory: str):
    if os.path.isdir(directory):
        all_files_list = [file[2] for file in os.walk(directory)][0]
        all_files_list = list(dict.fromkeys([file[0:4] for file in all_files_list]))
        return (len(all_files_list), all_files_list)

    return (0, [])


def get_stats(main_path):
    stats = {}
    problems = {}
    grand_total_complete = []
    grand_total_incomplete = []
    problems_path = os.path.join(main_path, 'problems')

    for language in os.listdir(problems_path):
        language_path = os.path.join(problems_path, language)
        if (os.path.isdir(language_path)) and (not language.startswith(".")):
            total_complete, list_complete = get_totals(
                os.path.join(language_path, "completos")
            )
            total_incomplete, list_incomplete = get_totals(
                os.path.join(language_path, "incompletos")
            )

            grand_total_complete.extend(list_complete)
            grand_total_incomplete.extend(list_incomplete)

            problems[language] = {
                "tentados": total_complete + total_incomplete,
                "completos": total_complete,
            }

    for language, value in problems.items():
        stats[language] = format_progress_text(value)

    total_complete = len(list(dict.fromkeys(grand_total_complete)))
    grand_total = total_complete + len(list(dict.fromkeys(grand_total_incomplete)))

    return (stats, {"total": grand_total, "completo": total_complete})


def update(main_path):
    string_stats, general = get_stats(main_path)

    with open(os.path.join(main_path, "readme.md"), "w") as f:

        f.write(DEFAULT_TEXT)
        f.write(f"Total geral: `{format_progress_text(general).lstrip()}`\n\n")

        for language, value in string_stats.items():
            f.write(f"- [{language}](./{language}/)\n\n")
            f.write("```txt")
            f.write(f"\n{value}\n")
            f.write("```\n\n")

    return "Readme file updated"