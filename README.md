# Text-Based-Quiz-App
Python Project

Description: In this project, the user can create many quizzes by using the given commands, such as "create quiz", "mc" (add multiple choice question), "fr" (add free response question), "edit quiz", and "view quiz", etc. You can also use "take quiz" command to take the specified quiz.

There are total of 2 classes:
                        1. main_quiz.py: This is the main class where the code of the functions of all the quizzes commands exist while the program is                                running as long as the main while loop is looping. Whatever command the user inputs everytime, the code will check which command                            is entered and it will allow the user to use its functionality. For example, if the user types the command "create quiz" and                                enters the quiz name on the next line, it will add that quiz to the list of quizzes and then user can add questions and answers.
                        
                        2. question.py: The class stores all the information of each question in each quiz like what type of question it is mc or fr, what                            is the question, and the options or answers
