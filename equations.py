import json


def new(topic, y):
    with open("equations.json", "r+") as f:
        data = json.load(f)
        data[topic] = []
        data[topic].append(y)
        f.seek(0)
        json.dump(data, f, indent=4)


def write_json(topic, new_data):
    with open("equations.json", 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[topic].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)


while True:
    topic = str(input("Topic: ")).lower()
    equation = str(input("Equation: "))
    if topic.lower() == "q" or equation.lower() == "q":
        break
    y = {
      "equation": equation,
      "image": "hmm"
    }
    z = {
      topic: [
          {
              "equation": equation,
              "image": "hmm"
          }
      ]
    }

    with open("equations.json", "r") as f:
        data = json.load(f)
    if topic not in data:
        new(topic, y)
    else:
        write_json(topic, y)
