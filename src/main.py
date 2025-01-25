import json
from agents.user_agent import UserAgent
from agents.quiz_agent import QuizAgent
from agents.result_agent import ResultAgent
from agents.notification_agent import NotificationAgent

# Global communication queue
communication_queue = []

# Load quiz questions from JSON
with open("data/quiz_questions.json") as file:
    quiz_questions = json.load(file)

# Main function
def main():
    quiz_agent = QuizAgent("quiz1", quiz_questions["quiz1"], communication_queue)
    user_agent1 = UserAgent("u1", "Alice", communication_queue)
    user_agent2 = UserAgent("u2", "Bob", communication_queue)
    result_agent = ResultAgent(communication_queue)
    notification_agent = NotificationAgent()

    # Emit questions
    quiz_agent.emit_question("q1")
    quiz_agent.emit_question("q2")

    # Users submit answers
    user_agent1.submit_answer("quiz1", "q1", "4")
    user_agent1.submit_answer("quiz1", "q2", "Paris")
    user_agent2.submit_answer("quiz1", "q1", "3")
    user_agent2.submit_answer("quiz1", "q2", "London")

    # Evaluate answers
    results = result_agent.evaluate_answers()

    # Send notifications
    notification_agent.send_results(results)

if __name__ == "__main__":
    main()
