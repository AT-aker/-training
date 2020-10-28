import random
import time



question_answer = []
question_answer.append(['Cat not dog', 'T'])
question_answer.append(['Cat have five legs', 'F'])
question_answer.append(['Door is black', 'F'])
question_answer.append(['Light is on', 'T'])
question_answer.append(['Song is sailents', 'T'])

random.shuffle(question_answer)

user_score = 0
start_time = time.perf_counter()

for item in question_answer:
    print('True or Falce: ' +item[0])
    answer = input('Please enter T if true or F if falce')
    if answer == item[1] or answer == item[1].lower():
        print('Excellent')
        user_score += 1
    else:
        print('Not correct')
end_time = time.perf_counter()


print('Congratulations! Tour total score is:' + str(user_score) + ' total time:'
      + str(end_time - start_time) + ' seconds')