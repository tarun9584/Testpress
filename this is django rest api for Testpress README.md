# Testpress
This is django project for Testpress.

The Projcet is deployed on pythonanywhere.com 
and can be accessed by clicking here: http://tarun.pythonanywhere.com/auth/ (username: demo, password: demo1234)
This is admin page: where we can add Quizes, questions under the quizes and the options of the question. 

Apart from that I completd a REST api 

URL : http://tarun.pythonanywhere.com/Quizes/
Method : GET

Response:
 {
  "result": [
    {
      "quize": "Answer of 22-2?",
      "ques": []
    },
    {
      "quize": "Quiz2",
      "ques": [
        {
          "text": "what is correct?",
          "id": 1,
          "Options": [
            {
              "text": "Jvm is virtual machine.",
              "isCorrect": true
            },
            {
              "text": "Jvm is memory.",
              "isCorrect": false
            },
            {
              "text": "stack is permanent memory.",
              "isCorrect": false
            },
            {
              "text": "Queue is not data structure",
              "isCorrect": false
            }
          ]
        },
        {
          "text": "Answer of 2*2*4?",
          "id": 2,
          "Options": []
        }
      ]
    }
  ]
}

