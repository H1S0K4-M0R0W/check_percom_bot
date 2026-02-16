import json

class Worker:
    def __init__(self):
        pass

    def read_config_json(self, link):
        with open(link, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        if data.get("user_id"):
            return data.get("user_id")

        else:
            return None