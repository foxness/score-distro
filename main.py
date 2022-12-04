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
    # MAX_LENGTH = 20
    print()
    print(scores)
    print()


main()
