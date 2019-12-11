import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category
from flaskr.until import paginate_questions

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  cors = CORS(app, resources={r"/*": {"origins": "*"}})
  
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
      return response
  
  @app.route('/categories', methods=['GET'])
  def categories():
    categories = Category.query.all()
    formatCategories = [category.format() for category in categories]
    result = {}
    for category in formatCategories:
      print(category)
      result[category['id']] = category['type']

    return jsonify({
      'success': True,
      'categories': result
    })

  @app.route('/questions', methods=['GET'])
  def questions():
    selection = Question.query.all()
    current_question = paginate_questions(request, selection)

    categories = Category.query.all()
    formatCategories = [category.format() for category in categories]
    categoryDic = {}
    for category in formatCategories:
      categoryDic[category['id']] = category['type']

    if len(current_question) == 0:
      abort(404)
    currentCategory = {
      'type': 'click',
      'id': 0
    }
    return jsonify({
      'success': True,
      'questions': current_question,
      'total_questions': len(selection),
      'categories': categoryDic,
      'currentCategory': currentCategory
    })

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id==question_id).one_or_none()
      if questions is None:
        abort(404)
      question.delete()
      return jsonify({
        'success': True,
        'deleted': question_id
      })
    except:
      abort(422)

  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_answer = body.get('answer')
    new_category = body.get('category')
    new_difficulty = body.get('difficulty')
    new_question = body.get('question')
    
    question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
    question.insert()

    return jsonify({
      'success': True,
      'created': question.id
    })

  @app.route('/questions/search', methods=['POST'])
  def search_question():
    body = request.get_json()
    search_term = body.get('searchTerm')
    questions = Question.query.filter(Question.question.ilike('%' + search_term + '%')).all()

    if questions is None:
      abort(404)
    
    format_questions = [question.format() for question in questions]
    currentCategory = {
      'type': 'click',
      'id': 0
    }
    return jsonify({
      'success': True,
      "questions": format_questions,
      "total_questions": len(format_questions),
      "currentCategory": currentCategory
    })

  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def questions_by_category(category_id):
    category = Category.query.filter(Category.id==category_id).one_or_none()
    formatCategory = category.format()
    if category is None:
      abort(404)
    category_type = str(formatCategory["id"])
    
    questions = Question.query.filter(Question.category==category_type).all()
    formatQuestions = [question.format() for question in questions]
    return jsonify({
      'success': True,
      'total_questions': len(questions),
      'questions': formatQuestions,
      'currentCategory':formatCategory
    })

  @app.route('/quizzes', methods=['POST'])
  def quizzes():
    body = request.get_json()
    previous_questions = body.get('previous_questions')
    quiz_category = body.get('quiz_category')
    category_id = str(quiz_category["id"])
    if quiz_category["id"] == 0:
      questions = Question.query.all()
      format_questions = [question.format() for question in questions if question.id not in previous_questions]
      return jsonify({
        'success': True,
        'question': format_questions[0]
      })
    else:
      questions = Question.query.filter(Question.category==category_id).all()
      format_questions = [question.format() for question in questions if question.id not in previous_questions]
      return jsonify({
        'success': True,
        'question': format_questions[0]
      })
        

 
  @app.errorhandler(404)
  def not_find(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "not found"
      }),404

  @app.errorhandler(422)
  def not_find(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "422 Unprocessable Entity"
      }),422
  
  return app

    