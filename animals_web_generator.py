import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def print_data(animals_data):
    for animal in animals_data:
        print(f'Name: {animal["name"]}')
        print(f'Diet: {animal["characteristics"]["diet"]}')
        print(f'Location: {animal["locations"][0]}')
        if "type" in animal["characteristics"]:
            print(f'Type: {animal["characteristics"]["type"]}')
        print()

animals_data = load_data('animals_data.json')
print_data(animals_data)
