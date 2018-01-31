from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.urlresolvers import reverse
from .models import User, IssueText, EmotionChoice

def index(request):
    username = request.COOKIES.get('username', '')
    user = get_object_or_404(User, pk=username)
    return render(request, 'index.html', {'username':username, 'page': user.page})
    # return HttpResponse("Hello, this web is for annotating GitHub issue emotions!")

def polls(request):
    issue_id = request.GET.get('page', '')
    if int(issue_id) <= 0:
        issue = None
    else:
        issue = get_object_or_404(IssueText, pk=issue_id)
    return render(request, 'polls.html', {'issue': issue})

def vote(request):
    # issue_id = request.getParameter('issue_id')
    # print(issue_id)
    issue_id = request.GET.get('issue_id','')
    username = request.COOKIES.get('username', '')
    issue = get_object_or_404(IssueText, pk=issue_id)
    user = get_object_or_404(User, pk=username)
    EmotionChoice.objects.filter(issue=issue, user=user).delete()
    choice = EmotionChoice(issue=issue, user=user, choice_text=request.POST.get('choice'))
    choice.save()
    # ctx = {}
    # ctx['issue_id'] = issue.id
    # ctx['username'] = user.username
    page = int(issue_id)
    if page == user.end:
        page = 0
    elif page == IssueText.objects.all().order_by('-id')[0].id:
        page = 1
    else:
        page += 1
    user.page = page
    user.save()
    if page == 0:
        issue = None
    else:
        issue = get_object_or_404(IssueText, pk=page)
    return render(request, "polls.html", {'issue': issue})

def vote_test(request):
    issue_id = -1
    username = request.COOKIES.get('username', '')
    issue = get_object_or_404(IssueText, pk=issue_id)
    user = get_object_or_404(User, pk=username)
    if request.method == 'POST':
        choice_text = request.POST.get('choice')
        EmotionChoice.objects.create(issue=issue, user=user, choice_text=choice_text)
    return render(request, 'polls.html')

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
                response = HttpResponseRedirect('/labeling/index')
                response.set_cookie('username', username, 27200, secure=False)
                return response
            else:
                return HttpResponseRedirect('/labeling/login/')
    else:
        uf = UserForm()
    return render(request, 'login.html', {'uf': uf})
