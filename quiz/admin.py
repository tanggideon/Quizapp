from django.contrib import admin

from quiz.models import Answer, Instruction, Question, Quiz

# Register your models here.

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [InstructionInline, QuestionInline]
    list_display = ["category", "course", "due_by"]


admin.site.register(Instruction)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)