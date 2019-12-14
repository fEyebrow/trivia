QUESTIONS_PAGE_NUM = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PAGE_NUM
    end = start + QUESTIONS_PAGE_NUM

    questions = [question.format() for question in selection]
    current_question = questions[start:end]
    return current_question
