from question import Question

print('\n\n--- This is a text-based Quiz App where you can create and take the quiz ---\n')

print('Commands: ')

print('\t-Create Quiz:                   create quiz')
print('\t-Delete Quiz:                   del quiz')
print('\t-Finish Quiz:                   finish quiz')
print('\t-Add Question (type):           mc (multiple choice) or fr (free response)')
print('\t-Quit adding options for mc:    quest done')
print('\t-Correct answer for mc:         (Use -> before the answer (ex: ->answer')
print('\t-Delete Question:               del que (for current or last question) or del que ( enter a question number)')
print('\t-Edit Question:                 edit que')
print('\t-Take Quiz:                     take quiz')
print('\t-Close the terminal:            close')

print('\n')

create_quiz = 'create quiz'
del_quiz = 'del quiz'
finish_quiz = 'finish quiz'
add_mcquest = 'mc'
add_frquest = 'fr'
add_opt_mc = 'add opt'
remove_opt_mc = 'rem opt'
del_quest = 'del que'
take_quiz = 'take quiz'

creating_quiz = False

quizzes = []

new_quiz = []

inputCommand = None

#While the program is running

while True:
	if len(new_quiz) > 0:
		inputCommand = input('\t-Enter Command (for ' + "'" + new_quiz[0] + "'"  + '): ')
	else:
		inputCommand = input('-Enter Command: ')
	
	print()

	if inputCommand == 'close':
		break;

	#Creating a quiz

	if creating_quiz == True:

		if inputCommand == create_quiz:
			print('\t\t(You must first finish creating the new quiz or delete it)\n')

		elif inputCommand == finish_quiz:
			creating_quiz = False
			quizzes.append(new_quiz)
			quiz_name = new_quiz[0]
			new_quiz.clear()
			print("\t\t('" + quiz_name + "' is saved)\n")

		elif inputCommand == del_quiz:
			quiz_name = new_quiz[0]
			new_quiz.clear()
			creating_quiz = False

			print("\t\t('" + quiz_name + "' is deleted)\n")
		
		elif inputCommand == add_mcquest or inputCommand == add_frquest:
			question = input('\t\tQuestion ' + str(len(new_quiz)) + " (can use 'del que'): ")
			print()

			if question == del_quest:
				print('\t\t\t(Question Cancelled)\n')

			else:
				new_quiz.append(Question(inputCommand, question))

				#Input: mc

				if inputCommand == add_mcquest:
					total_options = 1

					while True:
						option = input('\t\t\tOption ' + str(total_options) + ': ')
						print()

						if option == 'que done':
							if len(new_quiz[-1].options) >= 2 and len(new_quiz[-1].correct_answers) > 0: #fix this bug
								break
							else:
								print('\t\t\t(Must have more than 1 option!)')
								print('\t\t\t(Must choose one or more correct answers!)\n')

						elif option == del_quest:
							new_quiz.pop()
							print('\t\t\t(Question deleted)\n')
							break

						else:
							if option.find('->') == 0:
								new_quiz[-1].correct_answers.append(option[2:])

							new_quiz[-1].options.append(option)
							total_options += 1
				
				#Input: fr

				elif inputCommand == add_frquest:
					correct_answer = input("\t\t\tEnter correct answer (can use 'del que'): ")
					print()

					if correct_answer == del_quest:
						new_quiz.pop()
						print('\t\t\t(Question deleted)\n')

					else:
						new_quiz[-1].correct_answers.append(correct_answer)

		elif inputCommand == del_quest:
			which_question_input = input("\t\tQuestion # (can also use the command 'last'): ")
			print()

			if which_question_input == 'last':
				if len(new_quiz) > 1:
					last_question = len(new_quiz) - 1
					new_quiz.pop()
					print('\t\t(Question ' + str(last_question) + ' is deleted)\n')

				else:
					print('\t\t(Quiz is empty!)\n')

			else:
				try:
					quest_num = int(which_question_input)

					if quest_num >= 1 and quest_num <= len(new_quiz) - 1:
						new_quiz.pop(quest_num)
						print('\t\t(Question ' + which_question_input + 'is deleted)\n')

				except:
					print("\t\tInvalid input or question # doesn't exist!\n")

	#Create a quiz

	elif inputCommand == create_quiz:
		quiz_name_input = input('\t-Enter Quiz Name: ')

		new_quiz.append(quiz_name_input)

		print("\n\t\t('" + quiz_name_input + "' is created)\n")
		creating_quiz = True











