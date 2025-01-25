# Online Quiz System

The Online Quiz System is a modular, event-driven application designed to demonstrate the principles of Event-Driven Programming (EDP) in Python. It simulates an interactive quiz platform where multiple agents coordinate through events to deliver an engaging experience. 

## Features
- **Dynamic Question Emission**: Questions are emitted as events by the Quiz Agent.
- **Real-Time Answer Submission**: Users submit their answers, which are queued and processed.
- **Automated Evaluation**: Submitted answers are evaluated in real-time by the Result Agent.
- **Instant Notifications**: The Notification Agent sends results to users as soon as the quiz is complete.

## Agents and Their Roles
1. **UserAgent**:
   - Represents a quiz participant.
   - Submits answers for quiz questions.

2. **QuizAgent**:
   - Emits questions as events for users to answer.
   - Manages the quiz flow.

3. **ResultAgent**:
   - Processes and evaluates answers from the event queue.
   - Keeps track of individual user scores.

4. **NotificationAgent**:
   - Sends detailed result summaries to users.

## How It Works
The system operates using a global event queue to facilitate communication between agents. Here's the workflow:
1. The **QuizAgent** emits questions to the event queue.
2. Users (via **UserAgent**) submit their answers to the same queue.
3. The **ResultAgent** processes events, evaluates answers, and calculates scores.
4. The **NotificationAgent** retrieves results and delivers them to the users.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-quiz-system.git
   cd online-quiz-system
   ```
2. Ensure you have Python 3.x installed.
3. Install any necessary dependencies (none required for this project).

## Running the Project
Run the following command to start the simulation:
```bash
python src/main.py
```

## Example Output
Here’s an example of what you’ll see when you run the program:
```
Quiz quiz1 emitted question q1: What is 2 + 2?
Quiz quiz1 emitted question q2: What is the capital of France?
User Alice submitted an answer for question q1 in quiz quiz1.
User Alice submitted an answer for question q2 in quiz quiz1.
User Bob submitted an answer for question q1 in quiz quiz1.
User Bob submitted an answer for question q2 in quiz quiz1.
Answer for question q1 by user u1 is correct.
Answer for question q2 by user u1 is correct.
Answer for question q1 by user u2 is incorrect.
Answer for question q2 by user u2 is incorrect.
User u1: 2 out of 2 correct.
User u2: 0 out of 2 correct.
```

## Project Structure
```
online-quiz-system/
├── src/
│   ├── agents/
│   │   ├── user_agent.py         # Handles user actions and answer submissions
│   │   ├── quiz_agent.py         # Manages quiz questions and emits events
│   │   ├── result_agent.py       # Evaluates user answers and tracks results
│   │   └── notification_agent.py # Sends result notifications
│   └── main.py                   # Main entry point for the simulation
├── data/
│   └── quiz_questions.json       # Quiz questions and answers in JSON format
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies (if any)
```

## Extending the Project
This project is highly modular and can be extended in various ways:
- **Add Timers**: Implement time limits for answering questions.
- **Leaderboards**: Track and display high scores across multiple quizzes.
- **Database Integration**: Store questions, user profiles, and results in a database.
- **Web Interface**: Build a user-friendly web UI for the quiz.

## License
This project is licensed under the MIT License, making it free to use and modify.

## Contact
For questions or contributions, please reach out via [your_email@example.com].
