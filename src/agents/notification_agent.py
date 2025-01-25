class NotificationAgent:
    def send_results(self, results):
        for user_id, result in results.items():
            print(f"User {user_id}: {result['correct']} out of {result['total']} correct.")
