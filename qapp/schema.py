import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Question, Answer

# Create a GraphQL type for the Answer model
class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer

# Create a GraphQL type for the Question model
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

# Create a Query
class Query(ObjectType):
    question = graphene.Field(QuestionType, id=graphene.Int())
    answer = graphene.Field(AnswerType, id=graphene.Int())
    questions = graphene.List(QuestionType)
    answers= graphene.List(AnswerType)

    def resolve_answer(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Answer.objects.get(pk=id)
        return None

    def resolve_question(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Question.objects.get(pk=id)
        return None

    def resolve_answers(self, info, **kwargs):
        return Answer.objects.all()

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()



schema = graphene.Schema(query=Query)