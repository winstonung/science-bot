import json


def new(topic, y):
    with open("main.json", "r+") as f:
        data = json.load(f)
        data[topic] = []
        data[topic].append(y)
        f.seek(0)
        json.dump(data, f, indent=4)


def write_json(topic, new_data):
    with open("main.json", 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[topic].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


topic = str(input("Topic: ")).lower()
while True:
    question = str(input("Question: "))
    answer = str(input("Answer: "))
    if topic.lower() == "q" or question.lower() == "q" or answer.lower() == "q":
        break
    result = topic.endswith("image")
    question.replace("\\n", "\n")
    answer.replace("\\n", "\n")
    if result is True:
        y = {
          "image": "hmm",
          "question": question,
          "answer": answer
          }
        z = {
            topic: [
                {
                    "image": "hmm",
                    "question": question,
                    "answer": answer
                }
            ]
        }
    else:
        y = {
            "question": question,
            "answer": answer
        }
        z = {
            topic: [
                {
                    "question": question,
                    "answer": answer
                }
            ]
        }

    with open("main.json", "r") as f:
        data = json.load(f)
        if topic not in data:
            new(topic, y)
        else:
            write_json(topic, y)
