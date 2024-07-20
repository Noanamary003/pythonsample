from django.shortcuts import render,redirect
from .models import model1,model2,model3,cartmodel
# Create your views here.
def index1(request):
    return render(request,'index.html')
def index2(request):
    return render(request,'indexstaff.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phoneno = request.POST.get("phoneno")  # Corrected field name to lowercase
        model_instance = model1(username=username, email=email, password=password, phoneno=phoneno)
        model_instance.save()
        return render(request, 'login.html')
    else:
        return render(request, 'temp.html')
    
def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        cr=model1.objects.filter(email=email,password=password)
        if cr:
            username=model1.objects.get(email=email,password=password)
            id=username.id
            email=username.email
            password=username.password
            request.session['id']=id
            request.session['email']=email
            request.session['password']=password
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def register1(request):
    if request.method=="POST":
        username=request.POST.get("username")
       
        email=request.POST.get("email")
        password=request.POST.get("password")
        model1(username=username,email=email,password=password).save()
        return render(request,'stafflogin.html')
    else:
        return render(request,'temp2.html')
    
def stafflogin(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        cr=model2.objects.filter(email=email,password=password)
        if cr:
            username=model2.objects.get(email=email,password=password)
            id=username.id
            email=username.email
            password=username.password
            request.session['id']=id
            request.session['email']=email
            request.session['password']=password
            return render(request,'indexstaff.html')
        else:
            return render(request,'stafflogin.html')
    else:
        return render(request,'stafflogin.html')
        
def userlist(request):
    user=model1.objects.all()
    return render(request,'userlist.html',{'user2': user})  

def userstafflist(request):
    user=model2.objects.all()
    return render(request,'userstafflist.html',{'user2': user})          

def delete1(request,id):
    del1=model1.objects.get(id=id)
    del1.delete()
    return render(request,"indexstaff.html")

def index3(request):
    return render(request,'adminindex.html')

def delete2(request,id):
    del1=model2.objects.get(id=id)
    del1.delete()
    return render(request,"adminindex.html")

def index3(request):
    return render(request,'adminindex.html')

def registerproduct(request):
    if request.method=="POST":
        name=request.POST.get("name")
       
        model=request.POST.get("model")
        price=request.POST.get("price")
        quantity=request.POST.get("quantity")
        model3(name=name,model=model,price=price,quantity=quantity).save()
        return render(request,'indexstaff.html')
    else:
        return render(request,'product.html')


def productlist(request):
    user=model3.objects.all()
    return render(request,'productlist.html',{'user3': user})  

def delete3(request,id):
    d=model3.objects.get(id=id)
    d.delete()
    return render(request,'indexstaff.html')

def adminlogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        u='admin@gmail.com'
        p='admin'
        if email==u:
            if password==p:
                return render(request,'adminindex.html')
    return render(request,'adminlogin.html')

def profile(request):
    try:
        email =request.session['email']
    except:
        return redirect('login')
    cr=model1.objects.get(email=email)
    if cr:
        user_info = {
        'username': cr.username,
        'email': cr.email,
        'password': cr.password,
        
        }
        return render(request,'profile.html',user_info)
    else:
        return render(request,'profile.html')
    
def updateprofile(request):
    email=request.session['email']
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        

        data=model1.objects.get(email=email)
        data.username=username
        data.email=email
        data.password=password
        

        data.save()

        cr=model1.objects.get(email=email)
        if cr:
            user_info = {
            'username': cr.username,
            
            'email': cr.email,
            'password': cr.password,
            
            }
            return render(request,'profile.html',user_info)
        else:
             return render(request,'profile.html')
        
def search(request):
    if request.method=='POST':
        cat=request.POST.get('name')
        data=model3.objects.filter(name=cat)
        return render(request,'search.html',{'datas':data})
    else:
        return render(request,'search.html')
    
def addcart(request, id):
    email = request.session['email']
    dt = model3.objects.get(id=id) 
    a = dt.name
    b = dt.model
    c = dt.price
    d = dt.quantity
    return render(request, "cart.html", {'a': a, 'b': b, 'c': c, 'd': d, 'email': email})


def addcart2(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        quantity = int(request.POST.get('quantity'))

        try:
            data = model3.objects.get(name=name)
            current_quantity = data.quantity
            new_quantity = current_quantity - quantity

            if new_quantity < 0:
                return render(request, 'error.html')

            email = request.session['email']
            user_data = model1.objects.get(email=email)
            phoneno = user_data.phoneno

            # Update quantity in database
            data.quantity = new_quantity
            data.save()

            # Save to cart model
            cartmodel(name=name, model=model, price=price, quantity=quantity, email=email, phoneno=phoneno).save()

            return render(request, 'index.html')
        
        except model3.DoesNotExist:
            return render(request, 'error.html')
    
    else:
        return render(request, 'cart.html')

    
def productlist2(request):
    user=model3.objects.all()
    return render(request,'productlist2.html',{'user': user})  

def cartlist(request):
    user=cartmodel.objects.all()
    return render(request,'cartlist.html',{'user3': user})  

def delete4(request,id):
    del1=cartmodel.objects.get(id=id)
    del1.delete()
    return render(request,"index.html")