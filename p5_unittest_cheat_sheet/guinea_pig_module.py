import logging
import requests


def calculate_avg(l):
    return sum(l) / len(l)


# There is a run time bug here, can you find it?
def guinea_pig(source_url, response_url):
    age_list = []
    resp = requests.get(source_url)
    
    try:
        json_data = resp.json()
        # parse response
        for idx, line in enumerate(json_data):
            record_id, name, age = line
            if age < 0:
                continue
            age_list.append(age)
    except Exception as e:
        error_msg = "error {source}, destination " \
                    "{destination}, after {x} lines".format(
            source=source_url,
            destination=response_url,
            x=idx)
        logging.error(error_msg)
        return False

    payload = {"avg_age": calculate_avg(age_list)}
    requests.post(response_url, data=payload)

    return True




def fixed_guinea_pig(source_url, response_url):
    age_list = []
    idx = None
    try:
        resp = requests.get(source_url)
        json_data = resp.json()
        # parse response
        for idx, line in enumerate(json_data):
            record_id, name, age = line
            if age < 0:
                continue
            age_list.append(age)
    except Exception as e:
        error_msg = "error {source}, destination " \
                    "{destination}, after {x} lines".format(
            source=source_url,
            destination=response_url,
            x=idx)
        logging.error(error_msg)
        return False

    payload = {"avg_age": calculate_avg(age_list)}
    requests.post(response_url, data=payload)

    return True
