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
mc = 'mc'
fr = 'fr'
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
			if len(quizzes[-1]) > 1:
				creating_quiz = False
				print("\t\t\t('" + quizzes[-1][0] + "' saved)\n")

			else:
				print('\t\t\t(A quiz must have 1 or more questions!)\n')

		elif inputCommand == del_quiz:
			quiz_name = quizzes[-1][0]
			quizzes.pop()
			creating_quiz = False

			print("\t\t\t('" + quiz_name + "' deleted)\n")
		
		elif inputCommand == mc or inputCommand == fr:
			while True:
				question = input('\t\t\tQuestion ' + str(len(quizzes[-1])) + " (can use 'del que'): ")
				print()

				question_done = False

				if question != '':

					question_done = True

					if question == del_quest:
						print('\t\t\t\t(Question cancelled)\n')
						break

					else:
						#Input: mc

						if inputCommand == mc:
							options = []
							correct_answers = 0
							total_options = 1

							while True:
								option_input = input('\t\t\t\tOption ' + str(total_options) + ': ')
								print()

								if option_input != '':
									if option_input == del_quest:
										print('\t\t\t\t\t(Question cancelled)\n')
										break

									elif option_input == 'que done':
										if len(options) >= 2 and correct_answers > 0:
											quizzes[-1].append(Question(inputCommand, question, options))
											break
										else:
											print('\t\t\t\t\t(Must have more than 1 option!)')
											print('\t\t\t\t\t(Must choose one or more correct answers!)\n')

									elif option_input == del_quest:
										print('\t\t\t\t(Question cancelled)\n')
										break

									else:
										same_option = ''

										for option in options:
											if option.find('->') == 0 and option_input.find('->') == 0:
												same_option = '(Correct option is already been selected!)'
												break

											elif (option.find('->') != 0 and option_input.find('->') != 0 and option == option_input) or (option.find('->') == 0 and option_input.find('->') != 0 and option[2:] == option_input) or (option.find('->') != 0 and option_input.find('->') == 0 and option == option_input[2:]):
												same_option = '(The option already exists!)'
												break

										if same_option == '':
											if option_input.find('->') == 0:
												correct_answers += 1

											options.append(option_input)
											total_options += 1

										else:
											print('\t\t\t\t\t' + same_option + '\n')

								else:
									print('\t\t\t\t\t(Must write something!)\n')
						
						#Input: fr

						elif inputCommand == fr:
							while True:
								correct_answer = input("\t\t\t\tEnter correct answer (can use 'del que'): ")
								print()

								if correct_answer != '':
									if correct_answer == del_quest:
										print('\t\t\t\t\t(Question cancelled)\n')
										break

									else:
										quizzes[-1].append(Question(inputCommand, question, correct_answer))
										break

								else:
									print('\t\t\t\t\t(Must write the correct answer!)\n')

				else:
					print('\t\t\t\t(Must write something!)\n')

				if question_done == True:
					break

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
							print('\t\t\t\t(Question # out of range!)\n')

					except:
						print("\t\t\t\t(Invalid Input!)\n")

			else:
				print('\t\t\t(Quiz is empty!)\n')

		elif inputCommand == view_quiz:
			if len(quizzes[-1]) > 1:

				print('\t\t\t----------------------------------\n')

				for i in range(1, len(quizzes[-1])):

					print('\t\t\tQuestion ' + str(i) + ': ' + quizzes[-1][i].question + '\n')

					if quizzes[-1][i].question_type == 'mc':
						for j in range(len(quizzes[-1][i].options)):

							if quizzes[-1][i].options[j].find('->') == 0:
								print('\t\t\t\t-> Option ' + str(j + 1) + ': ' + quizzes[-1][i].options[j][2:] + '\n')

							else:
								print('\t\t\t\t   Option ' + str(j + 1) + ': ' + quizzes[-1][i].options[j] + '\n')

					else:
						print('\t\t\t\tCorrect Answer: ' + quizzes[-1][i].options + '\n')

				print('\t\t\t----------------------------------\n')

			else:
				print('\n\t\t\t(Quiz is empty!)\n')

		else:
			print("\t\t\t(Invalid input for creating a quiz!)\n")
		

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

			quiz_exist = False

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quiz_exist = True

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

			if quiz_exist == False:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print("\t(No quizzes exist!)\n")

	#View a quiz

	elif inputCommand == view_quiz:
		if len(quizzes) > 0:

			quiz_name_input = input("\tEnter Quiz Name: ")
			print()

			quiz_to_view = None

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quiz_to_view = quiz
					break

			if quiz_to_view != None:

				with_answers_input = input('\t\tShow answers? (yes or no): ')

				while True:
					if with_answers_input != 'yes' and with_answers_input != 'no':
						print('\t\t\t(Invalid Input!)\n')
					else:
						break

				print()

				
				for i in range(1, len(quiz_to_view)):
					print('\t\t\tQuestion ' + str(i) + ': ' + quiz_to_view[i].question + '\n')

					if quiz_to_view[i].question_type == 'mc':

						for option_num in range(len(quiz_to_view[i].options)):

							if quiz_to_view[i].options[option_num].find('->') == 0:
								if with_answers_input == 'yes':
									print('\t\t\t\t-> Option ' + str((option_num + 1)) + ': ' + quiz_to_view[i].options[option_num][2:] + '\n')

								else:
									print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz_to_view[i].options[option_num][2:] + '\n')

							else:
								if with_answers_input == 'yes':
									print('\t\t\t\t   Option ' + str((option_num + 1)) + ': ' + quiz_to_view[i].options[option_num] + '\n')

								else:
									print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz_to_view[i].options[option_num] + '\n')

					else:
						if with_answers_input == 'yes':
							print('\t\t\t\tCorrect Answer: ' + quiz_to_view[i].options + '\n')

			else:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print('\t(No quizzes exist!)\n')

	#Delete a quiz

	elif inputCommand == del_quiz:

		if len(quizzes) > 0:

			quiz_name_input = input('\tEnter Quiz Name: ')
			print()

			quiz_exist = False

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quizzes.remove(quiz)
					print("\t\t('" + quiz_name_input + "' deleted)\n")
					quiz_exist = True
					break

			if quiz_exist == False:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print('\t(No quizzes exist!)\n')

	#Take a quiz

	elif inputCommand == take_quiz:

		if len(quizzes) > 0:

			quiz_name_input = input('\tEnter Quiz Name: ')
			print('\n')

			quiz_exist = False

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quiz_exist = True
					quiz_completed = False
					quest_num = 1

					while True:
						print('\t\tQuestion ' + str(quest_num) + ': ' + quiz[quest_num].question + '\n')

						if quiz[quest_num].question_type == 'mc':

							option_count = 1

							for option in quiz[quest_num].options:
								if option.find('->') == 0:
									print('\t\t\tOption ' + str(option_count) + ': ' + option[2:] + '\n')

								else:
									print('\t\t\tOption ' + str(option_count) + ': ' + option + '\n')

								option_count += 1

							print()


						while True:
							answer_input = input('\t\t\tEnter Answer: ')
							print()

							got_answer_right = False

							if answer_input != '':
								if quiz[quest_num].question_type == 'mc':

									try:
										chosen_option_num = int(answer_input)

										if chosen_option_num >= 1 and chosen_option_num <= len(quiz[quest_num].options):
											
											for i in range(len(quiz[quest_num].options)):
												if i + 1 == chosen_option_num and quiz[quest_num].options[i].find('->') == 0:
													print('\t\t\t\tCorrect :)\n')
													got_answer_right = True
													break

											if got_answer_right == False:
												print('\t\t\t\tIncorrect :(\n')

										else:
											print("\t\t\t\t(Option number doesn't exist!)\n")

									except:
										print('\t\t\t\t(Must write the option number!)\n')

								else:

									if answer_input == quiz[quest_num].options:
										print('\t\t\t\tCorrect :)\n')
										got_answer_right = True

									else:
										print('\t\t\t\tIncorrect :(\n')

							else:
								print('\t\t\t\t(Must write an answer!)\n')

							if got_answer_right == True:

								if quest_num + 1 <= len(quiz) - 1:
									quest_num += 1

								else:
									print('\t\t(Quiz completed)\n')
									quiz_completed = True
								
								break

						if quiz_completed == True:
							break

					break

			if quiz_exist == False:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print('\t(No quizzes exist!)\n')









