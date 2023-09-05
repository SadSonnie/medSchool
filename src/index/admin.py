from django.contrib import admin
from .models import Choices, Answer, Questions, Form, Responses, Profile

admin.site.index_template = 'memcache_status/admin_index.html'

@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
    list_display = ['choice', 'is_answer']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'answer_to']

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_type', 'required', 'answer_key', 'score', 'feedback']

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'description', 'creator', 'background_color', 'text_color', 'collect_email', 'authenticated_responder', 'edit_after_submit', 'confirmation_message', 'is_quiz', 'allow_view_score', 'createdAt', 'updatedAt']

@admin.register(Responses)
class ResponsesAdmin(admin.ModelAdmin):
    list_display = ['response_code', 'response_to', 'responder_ip', 'responder', 'responder_email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fath_name', 'age', 'phone_number', 'numb_of_dip', 'speciality', 'job']

# Path: src/index/admin.py


