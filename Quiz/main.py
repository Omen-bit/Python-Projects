from database import question_data

class Question:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer

class QuizBrain:
    def __init__(self,questions_list):
        self.questions_list=questions_list
        self.question_number=0
        self.score=0

    def next_question(self):
        current_question=self.questions_list[self.question_number]
        print(current_question.text)
        choice=input("Enter your answer (True/False): ")
        self.question_number+=1
        if choice==current_question.answer:
            print("Yor are Correct")
            self.score+=1
            print(f"Your current score : {self.score}/{self.question_number}")

        else:
            print("That's Wrong")
            print(f"Your current score : {self.score}/{self.question_number}")


question_bank=[]
for values in question_data:
    q_text=values["text"]
    q_answer=values["answer"]
    new_question=Question(q_text,q_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
for items in question_bank:
    quiz.next_question()
