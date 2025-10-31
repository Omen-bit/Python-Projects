class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def next_question(self):
        current_question=self.question_list[self.question_number]
        state=current_question.answer
        self.question_number+=1
        is_correct=input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        if is_correct==state:
            print("you got it right")
            print(f"The correct answer was: {current_question.answer}")
            self.score+=1
            print(f"Your current score is {self.score}")
        else:
            print("you got it wrong")
            print(f"The correct answer was: {current_question.answer}")
            self.score -= 1
            print(f"Your current score is {self.score}")



