## Endpoint
- GET '/categories'
- GET '/questions'
- DELETE '/questions/<int:question_id>'
- POST '/questions'
- POST '/questions/search'
- GET '/categories/<int:category_id>/questions'

#### GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
```
{
  '1' : "Science",
  '2' : "Art",
  '3' : "Geography",
  '4' : "History",
  '5' : "Entertainment",
  '6' : "Sports"
}
```

#### GET '/questions'
- Fetches a list of questions
- Request Arguments: need the current page which in the query
- Returns: a list of questions, number of total questions, current category, categories. 

```
{
  categories: {
    1: "Science", 
    2: "Art", 
    3: "Geography", 
    4: "History", 
    5: "Entertainment", 
    6: "Sports"
  }
  currentCategory: {id: 0, type: "click"},
  questions: [{answer: "Muhammad Ali", category: 4, difficulty: 1, id: 9,…},…]
  success: true,
  total_questions: 21
}
```

#### DELETE '/questions/<int:question_id>'
- DELETE question using a question ID. 
- Request Arguments: need question id which in the path
- Returns: the id of the deleted question

```
{
  'success': True,
  'deleted': 1
}
```

#### POST '/questions'
- create a question
- Request Arguments: require the question and answer text, 
  category, and difficulty score
- Returns: the id of the created question

```
{
  'success': True,
  'deleted': 2
}
```

#### POST '/questions/search'
- search questions
- Request Arguments: the words using searching 
- Returns: a list of questions based on a search term

```
{
  currentCategory: {id: 0, type: "click"},
  questions: [{answer: "Muhammad Ali", category: 4, difficulty: 1, id: 9, question: "What boxer's original name is Cassius Clay?" }],
  success: true,
  total_questions: 1
}
```

#### GET '/categories/<int:category_id>/questions'
- get questions based on category
- Request Arguments: category id
- Returns: a list of questions based on category

```
{
  currentCategory: {id: 1, type: "Science"},
  questions: [{
    answer: "The Liver",
    category: 1,
    difficulty: 4,
    id: 20,
    question: "What is the heaviest organ in the human body?"
  }],
  success: true,
  total_questions: 1
}
```

#### POST '/quizzes'
- get questions to play the quiz.
- Request Arguments: none
- Returns: a random questions within the given category, 
  if provided, and that is not one of the previous questions.
```
{
  question: {
    answer: "Lake Victoria",
    category: 3,
    difficulty: 2,
    id: 13,
    question: "What is the largest lake in Africa?"
  },
  success: true
}
```