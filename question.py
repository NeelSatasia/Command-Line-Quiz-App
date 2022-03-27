class Question:
	options = []
	correct_answers = []

	def __init__(self, question_type, question):
		self.question_type = question_type
		self.question = question