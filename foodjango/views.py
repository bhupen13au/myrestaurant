from django.shortcuts import render,redirect
from .models import User_details,Dish


def welcome(response):
    return render(response, 'index.html')


def login(response):
    return render(response,'login.html')


def validate_user(request):
    name = request.POST['username']
    # dob = request.POST['dob_date']
    email = request.POST['email_id']
    phone = request.POST['phone_no']
    try:
        db_obj = User_details.objects.get(u_name=name)
    except:
        print('Not found')
        return render(request, 'login.html')
    else:
        if db_obj:
            print(db_obj.u_name,db_obj.u_email,str(db_obj.u_phone))
            print(type(db_obj.u_name), type(db_obj.u_email), type(str(db_obj.u_phone)))
            print(name, email, phone)
            print(type(name), type(email), type(phone))
            if (name==db_obj.u_name) and email==db_obj.u_email and phone==str(db_obj.u_phone):
                print('inside if cond')
                return render(request,'menu.html')
            else:
                print('inside else')
                return render(request, 'login.html')


def signup(response):
    return render(response, 'signup.html')


def register(request):
    user = User_details()
    user.u_name = request.POST['username']
    user.u_dob = request.POST['dob_date']
    user.u_address = request.POST['address']
    user.u_email = request.POST['email_id']
    user.u_phone = request.POST['phone_no']
    user.save()
    # return render(request, 'login.html')
    return redirect('login')

# def menu(response):
#     dishes = list(Dish.objects.all())
#     return render(response, 'menu.html', {'dishes': dishes})


def menu(response):
    dishes = list(Dish.objects.all())
    for dish in dishes:
        print('name',dish.__dict__)
        print('cat', dish.Non_Veg)
    return render(response, 'menu.html', {'dishes': dishes})


def total_calc(request):
    dishqty_1 = request.POST['dishqty']
    # total = dishqty_1*price
    return