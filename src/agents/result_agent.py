class ResultAgent:
    def __init__(self, communication_queue):
        self.communication_queue = communication_queue
        self.results = {}

    def evaluate_answers(self):
        while self.communication_queue:
            event = self.communication_queue.pop(0)
            if event["event_type"] == "submit_answer":
                payload = event["payload"]
                user_id = payload["user_id"]
                quiz_id = payload["quiz_id"]
                question_id = payload["question_id"]
                answer = payload["answer"]

                correct_answer = payload.get("correct_answer", "")
                is_correct = answer == correct_answer

                if user_id not in self.results:
                    self.results[user_id] = {"correct": 0, "total": 0}

                self.results[user_id]["total"] += 1
                if is_correct:
                    self.results[user_id]["correct"] += 1

                print(f"Answer for question {question_id} by user {user_id} is {'correct' if is_correct else 'incorrect'}.")
        return self.results
