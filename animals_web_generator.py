import json
import os

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_data(animals_data):
    animals_data_str = ''
    for animal in animals_data:
        animals_data_str += f'<li class="cards__item">\n'
        animals_data_str += f'Name: {animal["name"]}<br/>\n'
        animals_data_str += f'Diet: {animal["characteristics"]["diet"]}<br/>\n'
        animals_data_str += f'Location: {animal["locations"][0]}<br/>\n'
        if "type" in animal["characteristics"]:
            animals_data_str += f'Type: {animal["characteristics"]["type"]}<br/>\n'
        animals_data_str += f'</li>'
        animals_data_str += '\n'
    return animals_data_str


def replace_html_content(template_path, output_path, animals_data_str):
    with open(template_path, "r") as reader:
        html_content = reader.readlines()

    new_html_content = []
    for line in html_content:
        if '__REPLACE_ANIMALS_INFO__' in line:
            line = line.replace('__REPLACE_ANIMALS_INFO__', animals_data_str)
        new_html_content.append(line)

    with open(output_path, "w") as writer:
        writer.writelines(new_html_content)


def main():
    animals_data = load_data('animals_data.json')
    animals_data_str = get_data(animals_data)
    print(animals_data_str)
    replace_html_content('animals_template.html', 'animals.html', animals_data_str)


if __name__ == '__main__':
    main()
