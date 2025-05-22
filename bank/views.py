from django.shortcuts import render
from bank.form import DemoRegister

from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def demo(req):
    if req.method == 'POST':
        # print(req.POST)
        form = DemoRegister(req.POST)#return complete form
        if form.is_valid():
            print(form.cleaned_data)
        # form = DemoRegister()
        return HttpResponseRedirect("/demo/success/")     
    else:
        form=DemoRegister()
    return render(req,"bank/index.html",{'form':form})


def reg_success(req):
    return render(req,"bank/success.html")