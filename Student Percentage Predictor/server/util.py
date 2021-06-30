import json
import pickle
import numpy as np

__columns = None
__model = None


def estimated_score(study_hours):
    x = np.array(study_hours)
    x = x.reshape(1, -1)
    return round(__model.predict(x)[0], 2)


def load_saved_artifacts():
    global __columns
    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model

    with open("./artifacts/score_predictor.pickle", "rb") as f:
        __model = pickle.load(f)


if __name__ == '__main__':
    load_saved_artifacts()
    print(estimated_score(9.25))
