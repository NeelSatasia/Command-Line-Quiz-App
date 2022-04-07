from question import Question
import os

print('\n\n--- This is a text-based Quiz App where you can create and take the quiz ---\n')

print('Commands: ')

print('\t-Create Quiz:                   /create quiz')
print('\t-Delete Quiz:                   (/del quiz) or (/del all quizzes)')
print('\t-Save Quiz:                     /save quiz')
print('\t-Add Question (type):           /mc (multiple choice) or /fr (free response)')
print('\t-Quit adding options for mc:    /que done')
print('\t-Correct answer for mc:         (Use -> before the answer (ex: ->answer)')
print('\t-Delete Question:               /del que (for current, last question, or enter a question number)')
print('\t-Take Quiz:                     /take quiz')
print('\t-View Quiz:                     /view quiz')
print('\t-Edit Quiz:                     /edit quiz')
print('\t-End taking the quiz:           /end quiz')
print("\t-View All Quizzes' Names:       /view quizzes names")
print('\t-Terminate Code:                /close')

print('\n')

#Commands

create_quiz = '/create quiz'
del_quiz = '/del quiz'
del_all_quizzes = '/del all quizzes'
save_quiz = '/save quiz'
mc = 'mc'
command_mc = '/mc'
fr = 'fr'
command_fr = '/fr'
quest_done = '/que done'
del_quest = '/del que'
take_quiz = '/take quiz'
view_quiz = '/view quiz'
edit_quiz = '/edit quiz'
end_quiz = '/end quiz'
view_quizzes = '/view quizzes names'
close = '/close'

filename = 'quizzes_data.txt'

quizzes = []

#If any, load all the quizzes from the file

if os.path.exists(filename):
	file = open(filename, 'r')

	for line in file:
		if line.find('(Quiz: ') == 0:
			quizzes.append([line[7:len(line) - 2]])

		elif line.find('(Question (mc): ') == 0:
			quizzes[-1].append(Question(mc, line[16:len(line) - 2], []))

		elif line.find('(Option: ') == 0:
			quizzes[-1][-1].options.append(line[9:len(line) - 2])

		elif line.find('(Question (fr): ') == 0:
			quizzes[-1].append(Question(fr, line[16:len(line) - 2], ''))

		elif line.find('(Correct Answer: ') == 0:
			quizzes[-1][-1].options = line[17:len(line) - 2]

	file.close()

#Adds new or updated quiz data

def quiz_data_in_file(quiz, file):

	for stuff in quiz:
		if isinstance(stuff, str):
			file.write('(Quiz: ' + stuff + ')\n')

		elif stuff.question_type == mc:
			file.write('(Question (mc): ' + stuff.question + ')\n')

			for option in stuff.options:
				file.write('(Option: ' + option + ')\n')

		elif stuff.question_type == fr:
			file.write('(Question (fr): ' + stuff.question + ')\n')
			file.write('(Correct Answer: ' + stuff.options + ')\n')

	file.write('\n')


create_or_edit_quiz = False
edit_quiz_mode = False
current_quiz_index = None

inputCommand = None

#While the program is running, the user can enter any given commands

while True:

	if create_or_edit_quiz == True:
		inputCommand = input('\t\tEnter Command (for ' + "'" + quizzes[current_quiz_index][0] + "'): ")
	else:
		inputCommand = input('Enter Command: ')
	
	print()

	#Terminate code

	if inputCommand == close:
		break;

	#Creating a quiz

	if create_or_edit_quiz == True:

		if inputCommand == create_quiz:
			print('\t\t\t(Must first finish with this quiz!)\n')

		elif inputCommand == save_quiz:

			if len(quizzes[current_quiz_index]) > 1:

				create_or_edit_quiz = False
				print("\t\t\t('" + quizzes[current_quiz_index][0] + "' saved)\n")

				if edit_quiz_mode == True:

					rewrite_file = open(filename, 'w')

					for quiz in quizzes:
						quiz_data_in_file(quiz, rewrite_file)

					rewrite_file.close()

					edit_quiz_mode = False

				else:
					edit_file = open(filename, 'a')
					quiz_data_in_file(quizzes[current_quiz_index], edit_file)

			else:
				print('\t\t\t(A quiz must have 1 or more questions!)\n')

		elif inputCommand == del_quiz:

			quiz_name = quizzes[current_quiz_index][0]
			quizzes.pop(current_quiz_index)
			create_or_edit_quiz = False

			print("\t\t\t('" + quiz_name + "' deleted)\n")

			if len(quizzes) > 0:

				file = open(filename, 'w')

				for quiz in quizzes:
					quiz_data_in_file(quiz, file)

				file.close()

			elif os.path.exists(filename):
				os.remove(filename)
		
		elif inputCommand == command_mc or inputCommand == command_fr:

			while True:
				question = input('\t\t\tQuestion ' + str(len(quizzes[current_quiz_index])) + " (can use '/del que'): ")
				print()

				question_done = False

				if question != '':

					question_done = True

					if question == del_quest:
						print('\t\t\t\t(Question cancelled)\n')
						break

					else:
						#Input: mc

						if inputCommand == command_mc:
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

									elif option_input == quest_done:
										if len(options) >= 2 and correct_answers > 0:
											quizzes[current_quiz_index].append(Question(mc, question, options))
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

						elif inputCommand == command_fr:
							while True:
								correct_answer = input("\t\t\t\tEnter correct answer (can use '/del que'): ")
								print()

								if correct_answer != '':
									if correct_answer == del_quest:
										print('\t\t\t\t\t(Question cancelled)\n')
										break

									else:
										quizzes[current_quiz_index].append(Question(fr, question, correct_answer))
										break

								else:
									print('\t\t\t\t\t(Must write the correct answer!)\n')

				else:
					print('\t\t\t\t(Must write something!)\n')

				if question_done == True:
					break

		elif inputCommand == del_quest:

			if len(quizzes[current_quiz_index]) > 1:

				which_question_input = input("\t\t\tQuestion # (or the command 'last'): ")
				print()

				if which_question_input == 'last':
					quizzes[current_quiz_index].pop()
					print('\t\t\t(Question ' + str(len(quizzes[current_quiz_index])) + ' deleted)\n')

				else:
					try:
						quest_num = int(which_question_input)

						if quest_num >= 1 and quest_num <= len(quizzes[current_quiz_index]) - 1:
							quizzes[current_quiz_index].pop(quest_num)
							print('\t\t\t\t(Question ' + which_question_input + ' deleted)\n')
						else:
							print('\t\t\t\t(Question # out of range!)\n')

					except:
						print("\t\t\t\t(Invalid Input!)\n")

			else:
				print('\t\t\t(Quiz is empty!)\n')

		elif inputCommand == view_quiz:
			
			if len(quizzes[current_quiz_index]) > 1:

				print('\t\t\t----------------------------------\n')

				for i in range(1, len(quizzes[current_quiz_index])):

					print('\t\t\tQuestion ' + str(i) + ': ' + quizzes[current_quiz_index][i].question + '\n')

					if quizzes[current_quiz_index][i].question_type == mc:
						for j in range(len(quizzes[current_quiz_index][i].options)):

							if quizzes[current_quiz_index][i].options[j].find('->') == 0:
								print('\t\t\t\t-> Option ' + str(j + 1) + ': ' + quizzes[current_quiz_index][i].options[j][2:] + '\n')

							else:
								print('\t\t\t\t   Option ' + str(j + 1) + ': ' + quizzes[current_quiz_index][i].options[j] + '\n')

					else:
						print('\t\t\t\tCorrect Answer: ' + quizzes[current_quiz_index][i].options + '\n')

				print('\t\t\t----------------------------------\n')

			else:
				print('\n\t\t\t(Quiz is empty!)\n')

		else:
			print("\t\t\t(Invalid input for creating a quiz!)\n")
		

	#Create a quiz

	elif inputCommand == create_quiz:
		while True:
			quiz_name_input = input('\tEnter Quiz Name: ')
			print()

			valid_quiz_name = True
			error_type = ''

			if quiz_name_input == '':
				valid_quiz_name = False
				error_type = '(The quiz must have a name!)'

			else:
				for quiz in quizzes:
					if quiz[0] == quiz_name_input:
						valid_quiz_name = False
						error_type = '(Quiz name already exists!)'
						break

			if valid_quiz_name == True:
				quizzes.append([quiz_name_input])

				print("\t\t('" + quiz_name_input + "' created)\n")
				create_or_edit_quiz = True
				current_quiz_index = -1

				break

			else:
				print('\t\t' + error_type + '\n')

	#View a quiz

	elif inputCommand == view_quiz:
		if len(quizzes) > 0:

			quiz_name_input = input("\tEnter Quiz Name: ")
			print()

			quiz_exist = False

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quiz_exist = True

					while True:
						with_answers_input = input('\t\tShow answers? (yes or no): ')
						print()

						if with_answers_input != 'yes' and with_answers_input != 'no':
							print('\t\t\t(Invalid Input!)\n')

						else:
							break

					print('\n\t\t----------------------------------\n')

					
					for i in range(1, len(quiz)):
						print('\t\t\tQuestion ' + str(i) + ': ' + quiz[i].question + '\n')

						if quiz[i].question_type == mc:

							for option_num in range(len(quiz[i].options)):

								if quiz[i].options[option_num].find('->') == 0:
									if with_answers_input == 'yes':
										print('\t\t\t\t-> Option ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num][2:] + '\n')

									else:
										print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num][2:] + '\n')

								else:
									if with_answers_input == 'yes':
										print('\t\t\t\t   Option ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num] + '\n')

									else:
										print('\t\t\t\tOption ' + str((option_num + 1)) + ': ' + quiz[i].options[option_num] + '\n')

						else:
							if with_answers_input == 'yes':
								print('\t\t\t\tCorrect Answer: ' + quiz[i].options + '\n')

					print('\t\t----------------------------------\n')

					break

			if quiz_exist == False:
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

					if len(quizzes) > 0:

						file = open(filename, 'w')

						for quiz in quizzes:
							quiz_data_in_file(quiz, file)

						file.close()

					elif os.path.exists(filename):
						os.remove(filename)

					break

			if quiz_exist == False:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print('\t(No quizzes exist!)\n')

	#Delete all quizzes

	elif inputCommand == del_all_quizzes:

		if len(quizzes) > 0:
			
			quizzes.clear()
			
			if os.path.exists(filename):
				os.remove(filename)

			print('\t(All quizzes deleted)\n')

		else:
			print('\t(No quizzes exist!)\n')

	#Take a quiz

	elif inputCommand == take_quiz:

		if len(quizzes) > 0:

			quiz_name_input = input('\tEnter Quiz Name: ')
			print()

			quiz_exist = False
			quit_quiz = False

			for quiz in quizzes:
				if quiz[0] == quiz_name_input:
					quiz_exist = True
					quiz_completed = False
					quest_num = 1
					total_correct_answers = 0

					while True:
						print('\t\tQuestion ' + str(quest_num) + ': ' + quiz[quest_num].question + '\n')

						if quiz[quest_num].question_type == mc:

							option_count = 1

							for option in quiz[quest_num].options:
								if option.find('->') == 0:
									print('\t\t\tOption ' + str(option_count) + ': ' + option[2:] + '\n')

								else:
									print('\t\t\tOption ' + str(option_count) + ': ' + option + '\n')

								option_count += 1

							print()


						while True:
							answer_input = input("\t\t\tEnter Answer (can use '/end quiz'): ")
							print()

							valid_answer = False

							if answer_input == end_quiz:
								print('\t\t\t\t(Quiz ended)\n')
								quit_quiz = True
								break

							elif answer_input != '':
								if quiz[quest_num].question_type == mc:

									try:
										chosen_option_num = int(answer_input)

										if chosen_option_num >= 1 and chosen_option_num <= len(quiz[quest_num].options):

											valid_answer = True
											got_answer_right = False
											
											for i in range(len(quiz[quest_num].options)):

												if i + 1 == chosen_option_num and quiz[quest_num].options[i].find('->') == 0:
													print('\t\t\t\tCorrect :)\n')
													got_answer_right = True
													total_correct_answers += 1
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
										total_correct_answers += 1

									else:
										print('\t\t\t\tIncorrect :(\n')

									valid_answer = True

							else:
								print('\t\t\t\t(Must write an answer!)\n')

							if valid_answer == True:

								if quest_num + 1 <= len(quiz) - 1:
									quest_num += 1

								else:
									print('\t\t(Results: ' + str(total_correct_answers) + ' out of ' + str(len(quiz) - 1) + ')\n')
									quiz_completed = True
								
								break

						if quiz_completed == True or quit_quiz == True:
							break

					break

			if quiz_exist == False:
				print("\t\t('" + quiz_name_input + "' doesn't exist!)\n")

		else:
			print('\t(No quizzes exist!)\n')

	#Edit a quiz

	elif inputCommand == edit_quiz:

		if len(quizzes) > 0:
			while True:
				quiz_name_input = input('\tEnter Quiz Name: ')
				print()

				if quiz_name_input == '':
					print("\t\t(Must enter quiz's name!)\n")

				else:
					quiz_found = False

					for i in range(len(quizzes)):
						if quizzes[i][0] == quiz_name_input:
							quiz_found = True
							current_quiz_index = i
							edit_quiz_mode = True

					if quiz_found == False:
						print("\t\t(Quiz doesn't exist!)\n")
						break

					else:
						create_or_edit_quiz = True
						break

		else:
			print('\t(No quizzes exist!)\n')

	#View all the quizzes

	elif inputCommand == view_quizzes:

		if len(quizzes) > 0:
			count = 0

			for quiz in quizzes:
				count += 1
				print('\t' + str(count) + '. ' + quiz[0] + '\n')

		else:
			print('\t(No quizzes exist!)\n')

	else:
		print('\t(Invalid Input!)\n')





