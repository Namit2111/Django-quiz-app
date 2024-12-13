import random
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = "Seed the database with sample quiz questions"

    def handle(self, *args, **kwargs):
        # Clear existing questions
        Question.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing questions deleted.'))

        # Predefined questions
        questions = [
            {
                "text": "What is the capital of France?",
                "option_a": "Paris",
                "option_b": "London",
                "option_c": "Berlin",
                "option_d": "Madrid",
                "correct_option": "A",
            },
            {
                "text": "What is 2 + 2?",
                "option_a": "3",
                "option_b": "4",
                "option_c": "5",
                "option_d": "6",
                "correct_option": "B",
            },
            {
                "text": "Which programming language is known as the 'language of the web'?",
                "option_a": "Python",
                "option_b": "Java",
                "option_c": "JavaScript",
                "option_d": "C++",
                "correct_option": "C",
            },
            {
                "text": "What is the largest planet in our solar system?",
                "option_a": "Earth",
                "option_b": "Mars",
                "option_c": "Jupiter",
                "option_d": "Saturn",
                "correct_option": "C",
            },
            {
                "text": "Who wrote 'To Kill a Mockingbird'?",
                "option_a": "Harper Lee",
                "option_b": "Mark Twain",
                "option_c": "George Orwell",
                "option_d": "J.K. Rowling",
                "correct_option": "A",
            },
        ]

        # Create questions
        for q in questions:
            Question.objects.create(
                text=q["text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"],
            )

        self.stdout.write(self.style.SUCCESS(f"{len(questions)} questions added successfully."))
