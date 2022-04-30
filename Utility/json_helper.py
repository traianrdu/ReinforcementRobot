import json


def save_json(score, average):
    """Saves list to JSON file"""
    with open('Utility/score.json', 'w') as openfile:
        updated_json = {'score': score,
                        'avg_score': average}
        json.dump(updated_json, openfile)


def load_json():
    """Loads JSON into list"""
    with open('Utility/score.json', 'r') as openfile:
        json_object = json.load(openfile)
    score = json_object["score"]
    average = json_object["avg_score"]
    return score, average
