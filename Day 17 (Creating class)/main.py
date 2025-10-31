from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank=[]
for values in question_data:
    question_text=values["text"]
    question_answer=values["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
for data in question_bank:
    quiz.next_question()