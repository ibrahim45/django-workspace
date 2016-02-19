from django.contrib import admin
from polls.models import Question, Choice, Book, Author, Rating


class ChoiceInlineAdmin(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date Information', {'fields': []})
    # ]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    inlines = [ChoiceInlineAdmin]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 1
    list_editable = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Rating)
# admin.site.register(Choice)

