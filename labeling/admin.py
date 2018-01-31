from django.contrib import admin
from .models import IssueText, User, EmotionChoice

class IssueTextAdmin(admin.ModelAdmin):
    fields = ['id', 'issue_text', 'old_id', 'url', 'issue_or_comment']
    list_display = ('id', 'issue_text', 'old_id', 'url', 'issue_or_comment')
    search_fields = ['issue_text']

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'start', 'end', 'page']
    list_display = ('username', 'password', 'start', 'end', 'page')

class ChoiceAdmin(admin.ModelAdmin):
    model = EmotionChoice
    list_display = ('get_id', 'get_type', 'choice_text', 'get_user', 'get_text')

    def get_id(self, obj):
        return obj.issue.id
    get_id.short_description = 'Id'
    def get_text(self, obj):
        return obj.issue.issue_text
    get_text.short_description = 'Text'
    def get_type(self, obj):
        return obj.issue.issue_or_comment
    get_type.short_description = 'Type'
    def get_user(self, obj):
        return obj.user.username
    get_user.short_description = 'Annotator'

admin.site.register(IssueText, IssueTextAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(EmotionChoice, ChoiceAdmin)