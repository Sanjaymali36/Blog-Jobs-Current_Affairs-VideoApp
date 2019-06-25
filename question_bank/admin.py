
from tinymce.widgets import TinyMCE
from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choices
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class SSCQuestionAdmin(admin.ModelAdmin):
    list_display= ["pk","section_category","topic_category"]
    list_filter = ["section_category","topic_category"]
    readonly_fields = ('dateInserted',)
    inlines = [ChoiceInline]

class visitedQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    ("Content", {"fields": ["qid","test_time"]})
     ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(SSCquestions,SSCQuestionAdmin)
admin.site.register(visitedQuestion,visitedQuestionAdmin)

