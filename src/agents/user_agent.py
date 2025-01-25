class UserAgent:
    def __init__(self, user_id, name, communication_queue):
        self.user_id = user_id
        self.name = name
        self.communication_queue = communication_queue

    def submit_answer(self, quiz_id, question_id, answer):
        event = {
            "event_type": "submit_answer",
            "payload": {
                "user_id": self.user_id,
                "quiz_id": quiz_id,
                "question_id": question_id,
                "answer": answer
            }
        }
        self.communication_queue.append(event)
        print(f"User {self.name} submitted an answer for question {question_id} in quiz {quiz_id}.")
