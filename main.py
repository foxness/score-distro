import json
import urllib.request
import html


def main():
    username = input('Enter a MyAnimeList username: ')
    animes = get_animes(username)
    scores = get_scores(animes)
    print_scores(scores)


def get_animes(username):
    fp = urllib.request.urlopen(f'https://myanimelist.net/animelist/{username}')
    page = fp.read().decode('utf8')
    fp.close()

    DATA_START = 'data-items="'
    DATA_END = '"'

    start_index = page.find(DATA_START)
    if start_index == -1:
        return None
    
    start_index += len(DATA_START)
    end_index = page.find(DATA_END, start_index + 1)
    data = page[start_index:end_index]
    unescaped = html.unescape(data)
    animes = json.loads(unescaped)

    return animes


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

    for score in sorted(percentages.keys(), reverse = True):
        percent = percentages[score]
        length = int(percent * MAX_LENGTH / max_percent)
        print(f'{percent:6.2%}  {score:2}: {"-" * length}')

    print()


main()
