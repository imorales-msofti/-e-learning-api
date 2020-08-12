from .models import Lesson
from apps.questions.models import Question


def getCalificacionRespuestas(respuestas, lesson_id):
    score = 0
    try:
        for item_respuesta in respuestas:
            pregunta = Question.objects.get(name="item_respuesta['pregunta']")

            #Si la pregunta es correcta se incrementa el Score
            if(pregunta.correct_answer == item_respuesta.answer):
                score += pregunta
    except Exception as excep:
        score = 0

    return score
