questions = [
    ("What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3),
    ("Who wrote the play Romeo and Juliet?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy", 2),
    ("What is the chemical symbol for gold?", "Au", "Ag", "Fe", "Pb", 1),
    ("Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2),
    ("How many continents are there on Earth?", "Five", "Six", "Seven", "Eight", 3),
    ("What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4),
    ("Who discovered gravity when he saw an apple fall from a tree?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 2),
    ("What is the national currency of India?", "Dollar", "Euro", "Rupee", "Yen", 3),
    ("How many sides does a hexagon have?", "Five", "Six", "Seven", "Eight", 2),
    ("Which country is famous for the Eiffel Tower?", "Italy", "France", "Germany", "Spain", 2)
]

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer.1 for a/ 2 for b/ 3 for c/ 4 for d: "))
    if(question[5] == a):
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {question[5]}")
        break
