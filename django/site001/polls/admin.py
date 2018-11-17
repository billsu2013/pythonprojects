#from django.contrib import admin
#
## Register your models here.
from .models import Question, Choice
#admin.site.register(Question)
#admin.site.register(Choice)


from django.contrib import admin

# Register your models here.

#from .models import Question

#admin.site.register(Question)
#admin.site.register(Choice)
class QuestionAdmin(admin.ModelAdmin):
    # ...
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=4

#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Question',               {'fields': ['question_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#admin.site.register(Question,QuestionAdmin)







