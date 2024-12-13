# Django Quiz Application

This is a Django-based quiz application where users can answer questions and view a summary of their quiz results. The application supports random question selection, answer submission, and summary display. Additionally, the application allows for easy database seeding with predefined questions.

## Requirements

- Python 3.9+
- Django 5.x or above
- SQLite (default database for development, no additional setup required)

## Installation

### 1. Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Set up a virtual environment

It’s recommended to use a virtual environment to manage your project dependencies:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### On macOS/Linux:
```bash
source venv/bin/activate
```

#### On Windows:
```bash
venv\Scripts\activate
```

### 4. Install the required dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file does not exist, you can manually install Django by running:

```bash
pip install django
```

### 5. Apply database migrations

To create the necessary database tables for your models, run the following command:

```bash
python manage.py migrate
```

### 6. Seed the database with questions

The application includes a command to seed the database with predefined questions. To populate your database with questions, run:

```bash
python manage.py seed_questions
```

This will add a set of questions to the `Question` model, ready for the quiz.

### 7. Create a superuser (optional)

If you need access to the Django admin panel, create an admin user:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email address, and password.

### 8. Start the development server

You can now run the Django development server:

```bash
python manage.py runserver
```

This will start the server at `http://127.0.0.1:8000/`.

---

## Project Structure

The project includes the following key components:

### `urls.py`

Defines URL patterns for the following views:

- `start_quiz`: Initializes a new quiz session.
- `get_question`: Displays a random question from the database.
- `submit_answer`: Handles the user’s answer submission and stores the result.
- `quiz_summary`: Displays a summary of the user’s quiz performance.

### `views.py`

Contains the views responsible for processing user requests and interacting with the models:

- `start_quiz`: Starts a new quiz session by generating a unique session ID and redirects to the first question.
- `get_question`: Displays a random question that the user hasn't answered yet.
- `submit_answer`: Processes the user’s answer, records the result, and redirects to the next question.
- `quiz_summary`: Displays a summary of the quiz showing the total number of questions, correct answers, and incorrect answers.

### `models.py`

Contains the following models:

- `Question`: Represents a quiz question with multiple options (`A`, `B`, `C`, `D`) and the correct answer.
- `QuizSession`: Tracks the user's quiz session, storing each question answered and whether the answer was correct.

### Templates

Ensure you have the following templates inside the `templates` directory:

- `question.html`: Displays the current question with radio buttons for the user to select an answer.
- `summary.html`: Displays the quiz summary with the total number of questions, correct answers, and incorrect answers.

### `seed_questions.py`

A management command file (`seed_questions.py`) is included for seeding the database with sample questions. You can run the following command to populate the database:

```bash
python manage.py seed_questions
```

This will add predefined questions to the database, allowing you to start the quiz immediately.

---
