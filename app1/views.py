import os

from django.db.models import Q
from django.shortcuts import render, redirect
import app1
from .models import User, Image
from django.conf import settings
import hashlib


def initial(request):
    return redirect("/user/login")


# Log------------------------------------------------------
def user_login(request):
    method = request.method
    if method == "GET":
        return render(request, "user/login.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(name=username)
            user_id = user.id
            res = password + settings.SECRET_KEY
            password = hashlib.md5(res.encode("utf-8")).hexdigest()
            if password == user.password:
                if user.name == "manager":
                    return redirect("/manager/image/")
                else:
                    return redirect(f"/user/home/?user_id={user_id}")
            else:
                return render(request, "user/login.html", {"tip": "Incorrect password！"})
        except app1.models.User.DoesNotExist:
            return render(request, "user/login.html", {"tip": "User does not exist！"})


def user_signup(request):
    if request.method == "GET":
        return render(request, "user/signup.html")
    elif request.method == "POST":
        get_post = request.POST
        username = get_post.get("username")
        password = get_post.get("password")
        res = password + settings.SECRET_KEY
        password = hashlib.md5(res.encode("utf-8")).hexdigest()
        gender = get_post.get("gender")
        email = get_post.get("email")
        if User.objects.filter(name=username).exists():
            return render(request, "user/signup.html", {"msg": "Registration failed, username already exists!"})
        else:
            User.objects.create(name=username, password=password, gender=gender, email=email)
            return redirect("/user/login/", {"tip2": "Registration succeeded！"})


# Image Management-------------------------------------------------------------------------------
def manager_image(request):
    if request.method == "GET":
        image_list = Image.objects.all()
        return render(request, "manager/image.html", {"image_list": image_list})
    if request.method == "POST":
        search_query = request.POST.get('search')
        image_list = Image.objects.filter(
            Q(title__icontains=search_query) |
            Q(user__name__icontains=search_query) |
            Q(type__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(time__icontains=search_query) |
            Q(bio__icontains=search_query))
        return render(request, 'manager/image.html', {'image_list': image_list, "search_query": search_query})


def manager_image_add(request):
    if request.method == "GET":
        return render(request, "manager/image_add.html", {"users": User.objects.all()})
    elif request.method == "POST":
        title = request.POST.get("title")
        user = User.objects.get(id=request.POST.get("user"))
        image_type = request.POST.get("type")
        location = request.POST.get("location")
        time = request.POST.get("time")
        bio = request.POST.get("bio")
        picture = request.FILES.get("picture")
        Image.objects.create(title=title, user=user, type=image_type,
                             time=time, location=location, bio=bio, picture=picture)
        return redirect("/manager/image/")


def manager_image_delete(request):
    del_id = request.GET.get("del_id")
    image = Image.objects.filter(id=del_id).first()
    if image.picture:
        photo_path = image.picture.path
        if os.path.isfile(photo_path):
            os.remove(photo_path)
    image.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def manager_image_update(request):
    if request.method == "GET":
        update_id = request.GET.get("update_id")
        image = Image.objects.filter(id=update_id).first()
        users = User.objects.all()
        return render(request, "manager/image_update.html", {"image": image, "users": users})
    elif request.method == "POST":
        image_id = request.POST.get("image_id")
        title = request.POST.get("title")
        user = User.objects.get(id=request.POST.get("user"))
        image_type = request.POST.get("type")
        location = request.POST.get("location")
        time = request.POST.get("time")
        bio = request.POST.get("bio")
        Image.objects.filter(id=image_id).update(title=title, user=user, type=image_type,
                                                 time=time, location=location, bio=bio)
        picture = request.FILES.get("picture")
        if picture:
            image = Image.objects.get(id=image_id)
            image.photo.save(picture.name, picture)
        return redirect("/manager/image/")


# User Management----------------------------------------------------------------------
def manager_user(request):
    if request.method == "GET":
        user_list = User.objects.all()
        return render(request, "manager/user.html", {"user_list": user_list})
    if request.method == "POST":
        search_query = request.POST.get('search')
        user_list = User.objects.filter(
            Q(name__icontains=search_query) |
            Q(gender__icontains=search_query) |
            Q(email__icontains=search_query))
        return render(request, 'manager/user.html', {'user_list': user_list, "search_query": search_query})


def manager_user_add(request):
    if request.method == "GET":
        return render(request, "manager/user_add.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        email = request.POST.get("email")

        res = password + settings.SECRET_KEY
        password = hashlib.md5(res.encode("utf-8")).hexdigest()
        User.objects.create(name=username, password=password, gender=gender, email=email)

        return redirect("/manager/user/")


def manager_user_delete(request):
    del_id = request.GET.get("del_id")
    User.objects.filter(id=del_id).delete()
    return redirect("/manager/user/")


def manager_user_update(request):
    if request.method == "GET":
        update_id = request.GET.get("update_id")
        user = User.objects.get(id=update_id)
        return render(request, "manager/user_update.html", {"user": user})
    elif request.method == "POST":
        user_id = request.POST.get("user_id")
        username = request.POST.get("username")
        new_password = request.POST.get("password")
        gender = request.POST.get("gender")
        email = request.POST.get("email")

        user = User.objects.get(id=user_id)
        user.name = username
        if new_password:
            res = new_password + settings.SECRET_KEY
            password = hashlib.md5(res.encode("utf-8")).hexdigest()
            user.password = password
        user.gender = gender
        user.email = email
        user.save()

        return redirect("/manager/user/")


# User Page ------------------------------------------------------------------
def user_home(request):
    if request.method == "GET":
        images = Image.objects.all()
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'user/home.html', {'images': images, "user": user})
    if request.method == "POST":
        search_query = request.POST.get('search')
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        images = Image.objects.filter(
            Q(title__icontains=search_query) |
            Q(user__name__icontains=search_query) |
            Q(type__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(time__icontains=search_query) |
            Q(bio__icontains=search_query))
        return render(request, 'user/home.html', {'images': images, "user": user, "search_query": search_query})


def myspace(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(id=user_id)
    images = Image.objects.filter(user=user)
    context = {
        'user': user,
        'images': images,
    }
    return render(request, 'user/myspace.html', context)


def share(request):
    if request.method == "GET":
        user_id = request.GET.get('user_id')
        return render(request, "user/share.html", {"user": user_id})
    elif request.method == "POST":
        title = request.POST.get("title")
        user = User.objects.get(id=request.POST.get("user"))
        image_type = request.POST.get("type")
        location = request.POST.get("location")
        time = request.POST.get("time")
        bio = request.POST.get("bio")
        picture = request.FILES.get("picture")
        Image.objects.create(title=title, user=user, type=image_type,
                             time=time, location=location, bio=bio, picture=picture)
        return redirect(f"/user/home/?user_id={user.id}")


def user_image(request):
    if request.method == "GET":
        image_id = request.GET.get('image_id')
        user_id = request.GET.get('user_id')
        user = User.objects.get(id=user_id)
        image = Image.objects.get(id=image_id)
        context = {
            'image': image,
            'user': user
        }
        return render(request, 'user/image.html', context)