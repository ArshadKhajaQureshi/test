from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, redirect

def form(requests):
    n1=""
    data={}
    try:
        if requests.method=="POST":
            n1=int(requests.POST.get('num1'))
            data={
                "n2":n1*3,
                "n1":n1
            }
            # url="/about-us/?output={}".format(data)
            # return HttpResponseRedirect('/about-us/')    
            # return HttpResponseRedirect('/')   
            return render(requests,"myhomepage.html",data)
            # return redirect(url)
    except:
        pass        
    return render(requests,"myhomepage.html",data)
