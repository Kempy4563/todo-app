import json

with open("questions.json", 'r') as file:
    content = file.read()

# content is a string loads means load string. String is useless so we convert to a list
data = json.loads(content)

print(type(data))

score = 0


"""question is dictionary. 
Data is stored in a json 
list of dictionaries"""

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))

    """add another dictionary to questions for user choice"""
    question["user_choice_key"] = user_choice
    if question["user_choice_key"] == question["correct_answer"]:
        score = score + 1

for question in data:
    message = f"Your answer: {question['user_choice_key']}, Correct answer: {question['correct_answer']}"
    print(message)

print(f"your score is {score}")

#print(data)