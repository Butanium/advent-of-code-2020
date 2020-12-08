file = open('puzzle_inputs/puzzle_input_day_6.txt')
file_lines = file.read().split('\n')
groups_answers = []
answer = []
for i in file_lines:
    if i == '':
        groups_answers.append(answer)
        answer = []
        continue
    answer.append(i)
groups_answers.append(answer)

result = 0
# for group in groups_answers:
#     questions = []
#     for answer in group:
#         for question in answer:
#             if question not in questions:
#                 questions.append(question)
#     print(questions)
#     result += len(questions)
for group in groups_answers:
    questions = []
    scores = []
    for answer in group:
        for question in answer:
            if question not in questions:
                questions.append(question)
                scores.append(1)
            else:
                scores[questions.index(question)] += 1
    print(questions)
    r = sum([i == len(group) for i in scores])
    result += r

print(result)
