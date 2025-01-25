class QuizAgent:
    def __init__(self, quiz_id, questions, communication_queue):
        self.quiz_id = quiz_id
        self.questions = questions
        self.communication_queue = communication_queue

    def emit_question(self, question_id):
        if question_id in self.questions:
            question = self.questions[question_id]["question"]
            event = {
                "event_type": "new_question",
                "payload": {
                    "quiz_id": self.quiz_id,
                    "question_id": question_id,
                    "question": question
                }
            }
            self.communication_queue.append(event)
            print(f"Quiz {self.quiz_id} emitted question {question_id}: {question}")
        else:
            print("Invalid question ID.")
