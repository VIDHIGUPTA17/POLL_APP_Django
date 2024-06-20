from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll


# Create your views here.

def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render(request,"home.html",context)


def create(request):
    if request.method =='POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['question'])
            form.save()
            return redirect('home')
    else:
        form=CreatePollForm()
    context={
        'form':form
    }
    return render(request,"create.html",context)



def vote(request,poll_id):
    polls=Poll.objects.get(pk=poll_id)
    if request.method =='POST':
        selectedoption=request.POST['poll']
        if selectedoption == 'option1':
            polls.option_1_count+=1
            polls.total+=1
        elif selectedoption == 'option2':
            polls.option_2_count+=1
            polls.total+=1
        elif selectedoption == 'option3':
            polls.option_3_count+=1
            polls.total+=1
        elif selectedoption == 'option4':
            polls.option_4_count+=1
            polls.total+=1
        else:
            return HttpResponse(400, "invalid")
        
        polls.save()
        return redirect('result',poll_id)
    
    context={"polls":polls}
    return render(request,"vote.html",context)






def result(request,poll_id):
    polls=Poll.objects.get(pk=poll_id)
    context={"poll":polls}
    return render(request,"result.html",context)

