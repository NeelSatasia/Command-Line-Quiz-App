from question import Question

print('\n\n--- This is a text-based Quiz App where you can create and take the quiz ---\n')

print('Commands: ')

print('\t-Create Quiz:                   create quiz')
print('\t-Delete Quiz:                   del quiz')
print('\t-Finish Quiz:                   finish quiz')
print('\t-Add Question (type):           mc (multiple choice) or fr (free response)')
print('\t-Quit adding options for mc:    quest done')
print('\t-Correct answer for mc:         (Use -> before the answer (ex: ->answer)')
print('\t-Delete Question:               del que (for current or last question) or del que ( enter a question number)')
print('\t-Edit Question:                 edit que')
print('\t-Take Quiz:                     take quiz')
print('\t-View Quiz:                     view quiz')
print('\t-Terminate Code:                close')

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
view_quiz = 'view quiz'

creating_quiz = False

quizzes = []

inputCommand = None

#While the program is running

while True:
	if creating_quiz == True:
		inputCommand = input('\t\tEnter Command (for ' + "'" + quizzes[-1][0] + "'"  + '): ')
	else:
		inputCommand = input('Enter Command: ')
	
	print()

	#Terminate code

	if inputCommand == 'close':
		break;

	#Creating a quiz

	if creating_quiz == True:

		if inputCommand == create_quiz:
			print('\t\t\t(You must first finish creating the new quiz or delete it)\n')

		elif inputCommand == finish_quiz:
			creating_quiz = False
			print("\t\t\t('" + quizzes[-1][0] + "' saved)\n")

		elif inputCommand == del_quiz:
			quizzes.pop()
			creating_quiz = False

			print("\t\t\t('" + quiz_name + "' deleted)\n")
		
		elif inputCommand == add_mcquest or inputCommand == add_frquest:
			question = input('\t\t\tQuestion ' + str(len(quizzes[-1])) + " (can use 'del que'): ")
			print()

			if question == del_quest:
				print('\t\t\t\t(Question cancelled)\n')

			else:
				#Input: mc

				if inputCommand == add_mcquest:
					options = []
					correct_answers = 0
					total_options = 1

					while True:
						option = input('\t\t\t\tOption ' + str(total_options) + ': ')
						print()

						if option == 'que done':
							if len(options) >= 2 and correct_answers > 0:
								quizzes[-1].append(Question(inputCommand, question, options))
								break
							else:
								print('\t\t\t\t\t(Must have more than 1 option!)')
								print('\t\t\t\t\t(Must choose one or more correct answers!)\n')

						elif option == del_quest:
							print('\t\t\t\t(Question cancelled)\n')
							break

						else:
							if option.find('->') == 0:
								correct_answers += 1

							options.append(option)
							total_options += 1
				
				#Input: fr

				elif inputCommand == add_frquest:
					correct_answer = input("\t\t\t\tEnter correct answer (can use 'del que'): ")
					print()

					if correct_answer == del_quest:
						print('\t\t\t\t(Question cancelled)\n')

					else:
						quizzes[-1].append(Question(inputCommand, question, correct_answer))

		elif inputCommand == del_quest:

			if len(quizzes[-1]) > 1:
				which_question_input = input("\t\t\tQuestion # (or the command 'last'): ")
				print()

				if which_question_input == 'last':
					quizzes[-1].pop()
					print('\t\t\t(Question ' + str(len(quizzes[-1])) + ' deleted)\n')

				else:
					try:
						quest_num = int(which_question_input)

						if quest_num >= 1 and quest_num <= len(quizzes[-1]) - 1:
							quizzes[-1].pop(quest_num)
							print('\t\t\t(Question ' + which_question_input + ' deleted)\n')
						else:
							print('\t\t\t(Question # out of range!)')

					except:
						print("\t\t\t(Invalid input or question # out of range!)\n")

			else:
				print('\t\t\t(Quiz is empty!)\n')

		else:
			print("\t\t\t(Invalid Input!)\n")
		

	#Create a quiz

	elif inputCommand == create_quiz:
		quiz_name_input = input('\tEnter Quiz Name: ')

		quizzes.append([quiz_name_input])

		print("\n\t\t('" + quiz_name_input + "' created)\n")
		creating_quiz = True

	#Delete a question from a quiz

	elif inputCommand == del_quest:

		if len(quizzes) > 0:
			quiz_name_input = input('\tEnter Quiz Name: ')
			print()

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					which_question_input = input("\t\tQuestion # (or the command 'last'): ")
					print()

					if len(quiz) - 1 > 1:
						if which_question_input == 'last':
							quiz.pop()
							print('\t\t\t(Question ' + str(len(quiz)) + ' deleted)\n')

						else:
							try:
								quest_num = int(which_question_input)

								if quest_num >= 1 and quest_num <= len(quiz) - 1:
									quiz.pop(quest_num)
									print('\t\t\t(Question ' + which_question_input + ' deleted)\n')

								else:
									print('\t\t\t(Question # out of range!)\n')

							except:
								print("\t\t\t(Invalid input or question # out of range!)\n")

					else:
						que_deletable = False
						num_input = False

						try:
							quest_num = int(which_question_input)
							num_input = True
						except:
							num_input = False

						if which_question_input == 'last' or num_input == True:

							if (num_input == True and (int(which_question_input) >= 1 and int(which_question_input) <= len(quiz) - 1)) or (which_question_input == 'last'):
								print("\t\t\t(Deleting this question will also delete the quiz since the quiz will be empty)\n")
								que_deletable = True

							if que_deletable == True:
								while True:
									confirm_input = input('\t\t\tConfirm (yes or no): ')
									print()

									if confirm_input == 'yes':
										quizzes.remove(quiz)
										print("\t\t\t\t('" + quiz_name_input + "' deleted)\n")
										break

									elif confirm_input == 'no':
										print("\t\t\t\t('" + quiz_name_input + "' saved)\n")
										break

									else:
										print("\t\t\t\t(Invalid Input!)\n")

							else:
								print("\t\t\t(Invalid input or question # out of range!)\n")
					break

		else:
			print("\t(No quizzes exist!)\n")

	#View a quiz

	elif inputCommand == view_quiz:
		quiz_name_input = input("\tEnter Quiz Name: ")
		print()

		with_answers_input = input('\t\tWith answers? (yes or no): ')

		while True:
			if with_answers_input != 'yes' and with_answers_input == 'no':
				print('\t\t\t(Invalid Input!)\n')
			else:
				break

		print()

		for quiz in quizzes:
			if quiz[0] == quiz_name_input:
				for i in range(1, len(quiz)):
					print('\t\t\tQuestion ' + str(i) + ': ' + quiz[i].question + '\n')

					if quiz[i].question_type == 'mc':

						for option_num in range(len(quiz[i].options)):

							if quiz[i].options[option_num].find('->') == 0:
								if with_answers_input == 'yes':
									print('\t\t\t\t-> Option ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num][2:] + '\n')

								else:
									print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num][2:] + '\n')

							else:
								print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num] + '\n')

					else:
						if with_answers_input == 'yes':
							print('\t\t\t\tCorrect Answer: ' + quiz[i].options + '\n')










