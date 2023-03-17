from django.shortcuts import render
from .forms import ResumeForm
from .models import resume
from django.views import View
from django.db.models import Q

class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = resume.objects.all()
  return render(request, 'App/home.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'App/submit.html')

class CandidateView(View):
 def get(self, request, pk):
  candidate = resume.objects.get(pk=pk)
  return render(request, 'App/candidate.html', {'candidate':candidate})

def list(request):
  count = resume.objects.all().count()
  if 'q' in request.GET:
      q = request.GET['q']
      # data = Data.objects.filter(last_name__icontains=q)
      multiple_q = Q(Q(name__icontains=q))
      candidates = resume.objects.filter(multiple_q)
  else:
      candidates = resume.objects.all()
  return render(request, 'App/List.html', {'candidates':candidates,'count':count})

