import json

def add_kata_len_in_json_file(len):
    data = {"len": len}
    with open("bd.json", "w") as file:
        json.dump(data, file)
    print(f"Length of completed katas saved: {len}")

def get_kata_len_from_json_file():
    try:
        with open("bd.json", "r") as file:
            data = json.load(file)
            return data.get("len", 0)
    except FileNotFoundError:
        print("No data file found. Returning length as 0.")
        return 0
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning length as 0.")
        return 0