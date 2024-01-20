from django.shortcuts import render,HttpResponse,redirect
from visitor_app.models import Info

# Create your views here.

def create(request):
    if request.method=='POST':
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['umobile']
        idt=request.POST['intime']
        odt=request.POST['outtime']
        msg=request.POST['msg']
        # print(n)
        m=Info.objects.create(name=n,email=mail,mobile=mob,intime=idt,outtime=odt,msg=msg)
        m.save()
        #return HttpResponse("Data is inserted")
        return redirect('/dashboard')
    else:
        print("Request is:",request.method)
    return render(request,'create.html')

def dashboard(request):
    m=Info.objects.all()
    #print(m)
    context={}
    context['data']=m
    #return HttpResponse("data Fetch Successfully")
    return render(request,'dashboard.html',context)

def edit(request,rid):
    if request.method=='POST':
        #update new data
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['umobile']
        idt=request.POST['intime']
        odt=request.POST['outtime']
        msg=request.POST['msg']
        m=Info.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=mob,intime=idt,outtime=odt,msg=msg)
        return redirect('/dashboard')
    else:
        #display form with old data
        m=Info.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
        
        
    #print("id of record to be edited :",rid)
    #return HttpResponse("Id:"+rid)

def delete(request,rid):
    #print("id of record to be deleted :",rid)
    m=Info.objects.filter(id=rid)
    m.delete()
    #return HttpResponse("Id:"+rid)
    return redirect('/dashboard')
