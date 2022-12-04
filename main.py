import json


def main():
    animes = get_animes()
    scores = get_scores(animes)
    print_scores(scores)


def get_animes():
    raw = open('table', 'r').read()
    return json.loads(raw)


def get_scores(animes):
    scores = {}
    for anime in animes:
        score = anime['score']

        if score not in scores.keys():
            scores[score] = 1
        else:
            scores[score] += 1

    return scores


def print_scores(scores):
    MAX_LENGTH = 60

    count = sum(list(scores.values()))
    percentages = {k: scores[k] / count for k in scores.keys()}
    max_percent = max(percentages.values())

    print()

    for score, percent in percentages.items():
        length = int(percent * MAX_LENGTH / max_percent)
        print(f'{percent:6.2%}  {score:2}: {"-" * length}')

    print()


main()
