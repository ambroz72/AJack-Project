from django.http import JsonResponse
from django.shortcuts import render
from .models import person
from .forms import PersonRegistration 
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    form= PersonRegistration()
    dtls=person.objects.all()
    context={'form':form,'dtls':dtls}
    #context={'form':form}
    return render(request,'home.html',context)

# @csrf_exempt
# def add_data(request):
#     if request.method == "POST":
#         form = PersonRegistration(request.POST)
#         if form.is_valid():
#             name = request.POST['name']
#             email = request.POST['email']
#             password = request.POST['password']
#             prsn = person(name=name,email=email,password=password)
#             prsn.save()
#             x = person.objects.values()
#             print(x)
#             x_data = list(x)
#             print("---")
#             print(x_data)
#             return JsonResponse({'terms':'add','x_data':x_data})
#         else:
#             return JsonResponse({'terms':0})

#....ADD and UPDATE ..
@csrf_exempt
def add_data(request):
    if request.method == "POST":
        form = PersonRegistration(request.POST)
        if form.is_valid():
            prnid = request.POST['personid']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if(prnid == ''):
                prsn = person(name=name,email=email,password=password)
            else:
                prsn = person(id=prnid,name=name,email=email,password=password)
            prsn.save()
            x = person.objects.values()
            print(x)
            x_data = list(x)
            print("---")
            print(x_data)
            return JsonResponse({'terms':'add','x_data':x_data})
        else:
            return JsonResponse({'terms':0})


#....DELETE DATA....
@csrf_exempt
def delete_data(request):
    if request.method=="POST":
        id = request.POST.get('pid')
        print(id)
        dltprsn = person.objects.get(pk=id)
        dltprsn.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})


#...EDIT DATA.....
@csrf_exempt
def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('pid')
        print(id)
        editprsn = person.objects.get(pk=id)
        editprsn_data = {"id":editprsn.id,
                            "name":editprsn.name,
                            "email":editprsn.email,
                            "password":editprsn.password}
        return JsonResponse(editprsn_data)