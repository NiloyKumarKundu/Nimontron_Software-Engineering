from ctypes import sizeof
from re import I
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
import os
from django.db.models import Q
from django.db.models.functions import Concat
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Delivery_Man
from django.core.files.storage import  FileSystemStorage
import os



# Create your views here.


temp = {'name': 'Nimontron', 'title': 'Nimontron', 'sub_title': '', 'error': '', 'post': ''}

# Normal View

def index(request):
    return render(request, 'visitors/index.html', temp)


def about(request):
    temp['title'] = 'About Us'
    temp['sub_title'] = 'About'
    return render(request, 'visitors/about.html', temp)


def service(request):
    temp['title'] = 'Services'
    temp['sub_title'] = 'Service'
    return render(request, 'visitors/service.html', temp)


def restaurant_lists(request):
    temp['title'] = 'Restaurants'
    temp['sub_title'] = 'Restaurants'
    return render(request, 'visitors/restaurant_lists.html', temp)


def contact(request):
    temp['title'] = 'Contact Us'
    temp['sub_title'] = 'Contact'
    return render(request, 'visitors/contact.html', temp)



def donate(request):
    temp['title'] = 'Donate Others'
    temp['sub_title'] = 'Donate Others'
    post = Foundation_Post.objects.all()
    temp['post'] = post
    return render(request, 'visitors/donate.html', temp)


def login_as(request):
    temp['title'] = 'Log In As'
    temp['sub_title'] = 'Log In As'
    return render(request, 'visitors/login_as.html', temp)


# For All User

def Logout(request):
    temp['name'] = 'Nimontron'
    logout(request)
    return redirect('customers:login_as')




# Customer View


def signup(request):
    temp['title'] = 'Sign Up'
    temp['sub_title'] = 'Sign Up'
    temp['error'] = ''
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        image = request.FILES['image']
        password = request.POST['password']
        email = request.POST['email']
        contact_no = request.POST['contact']
        gender = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, password=password)
            Customer.objects.create(user=user, contact_no=contact_no, image=image, gender=gender, type='customer')
            temp['error'] = 'no'
        except:
            temp['error'] = 'yes'

    return render(request, 'visitors/signup.html', temp)



def customer_login(request):
    temp['title'] = 'Customer LogIn'
    temp['sub_title'] = 'Customer Login'
    temp['error'] = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            try:
                user1 = Customer.objects.get(user=user)
                if user1.type == "customer":
                    login(request, user)
                    messages.warning(request, 'Something went wrong! Please try again...')
                    return redirect('customers:customer_home')
                else:
                    messages.warning(request, 'Something went wrong! Please try again...')
            except:
                messages.warning(request, 'Something went wrong! Please try again...')
        else:
            messages.error(request, 'Email or password is wrong!')
    return render(request, 'visitors/login.html', temp)


def navCart(request):
    user=request.user
    cart = Cart.objects.filter(user=user, status='Cart').count()
    return cart

def customer_home(request):
    temp['title'] = 'Nilomtron'
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['cart'] = navCart(request)
    return render(request, 'customers/customer_home.html', temp)

def customer_all_post(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['title'] = 'All Posts'
    temp['sub_title'] = 'All Posts'
    temp['cart'] = navCart(request)
    nums='a'
    if 'search' in request.GET:
        q=request.GET['search']
        t=q.isdigit()
        if t==1:
            p=int(q) 
            p2=p-10
            p3=p+10
            p4=p-20
            p5=p+20
            p6=p-5
            p7=p+5
            p8=p-15
            p9=p+15
            p10=p-25
            p11=p+25
            p12=p+1
            p13=p+2
            p14=p+3
            p15=p+4
            p16=p+6
            p17=p+7
            p18=p+8
            p19=p+9
            p20=p-1
            p21=p-2
            p22=p-3
            p23=p-4
            p24=p-6
            p25=p-7
            p26=p-8
            p27=p-9
            p28=p+11
            p29=p+12
            p30=p+13
            p31=p+14
            p32=p-11
            p33=p-12
            p34=p-13
            p35=p-14

            posts=Post.objects.filter(Q(new_price=q)| Q(new_price=p2)|Q(new_price=p3)|Q(new_price=p5)|Q(new_price=p4)
            |Q(new_price=p6)|Q(new_price=p7)|Q(new_price=p8)|Q(new_price=p9)|Q(new_price=p10)|Q(new_price=p11)
            |Q(new_price=p12)|Q(new_price=p13)|Q(new_price=p14)|Q(new_price=p15)|Q(new_price=p16)|Q(new_price=p17)
            |Q(new_price=p18)|Q(new_price=p19)|Q(new_price=p20)|Q(new_price=p21)|Q(new_price=p22)|Q(new_price=p23)
            |Q(new_price=p24)|Q(new_price=p25)|Q(new_price=p26)|Q(new_price=p27)|Q(new_price=p28)|Q(new_price=p29)
            |Q(new_price=p30)|Q(new_price=p31)|Q(new_price=p32)|Q(new_price=p33)|Q(new_price=p34)|Q(new_price=p35)
            )
        else:
            posts=Post.objects.filter(
            Q(title__icontains=q) | Q(location__icontains=q)| Q(description__icontains=q)
            | Q(name__icontains=q) | Q(category__icontains=q))

    else:
        # Paginator
        post = Post.objects.all()
        per_page = 8
        all_post = Paginator(post, per_page)
        page = request.GET.get('page')
        venu = all_post.get_page(page)
        nums = 'a' * venu.paginator.num_pages
        
        try:
            posts = all_post.get_page(page)
        except PageNotAnInteger:
            posts = all_post.page(1)
        except EmptyPage:
            posts = all_post.page(all_post.num_page)
    temp['total_posts'] = posts
    temp['nums'] = nums
    return render(request, 'customers/customer_all_post.html', temp)


def customer_all_restaurants(request):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    temp['title'] = 'All Restaurants'
    temp['sub_title'] = 'All Restaurants'
    temp['cart'] = navCart(request)
    if 'search' in request.GET:
        q2=request.GET['search']
        restaurant=Restaurant.objects.filter(Q(ratting__icontains=q2) | Q(description__icontains=q2)
        | Q(address__icontains=q2) | Q(type__icontains=q2) | Q(name__icontains=q2) )
    else:
        restaurant = Restaurant.objects.all().order_by('-type')

    temp['restaurant'] = restaurant
    return render(request, 'customers/customer_all_restaurants.html', temp)



def customer_cart(request):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    temp['title'] = 'Shopping Cart'
    temp['sub_title'] = 'cart'
    temp['cart'] = navCart(request)
    return render(request, 'customers/customer_cart.html', temp)


def customer_food_post_details(request, id):
    temp['cart'] = navCart(request)
    temp['title'] = 'Food Post'
    temp['sub_title'] = 'Food Post'
    post = Post.objects.get(id=id)
    temp['post'] = post
    temp['error'] = ''
    x = request.user
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        user = request.user

        cart = Cart.objects.filter(user=user, post = post).exists()
        if cart:
            product = Cart.objects.get(user=user, post = post)
            product.quantity = product.quantity + 1
            product.save()
            return redirect('../customer_food_post_details/' + str(id))

        restaurant = Post.objects.get(id=id).restaurant
        ordered_date = post.creation_date
        status = "Cart"
        title = post.title
        address = Customer.objects.get(user=user).address

        try:
            Cart.objects.create(address=address, title=title, post=post, restaurant=restaurant, user=user, ordered_date=ordered_date, status=status)
            messages.success(request, "Post Added in your cart successfully")
        except:
            messages.error(request, "Something went wrong")

        return redirect('../customer_food_post_details/' + str(id))
    return render(request, 'customers/customer_food_post_details.html', temp)



def cart_item_decrease(request, id):
    temp['cart'] = navCart(request)
    temp['title'] = 'Food Post'
    temp['sub_title'] = 'Food Post'
    post = Post.objects.get(id=id)
    temp['post'] = post
    temp['error'] = ''

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        user = request.user

        cart = Cart.objects.filter(user=user, post = post).exists()
        if cart:
            product = Cart.objects.get(user=user, post = post)
            if product.quantity > 1:
                product.quantity = product.quantity - 1
                product.save()
                return redirect('../customer_food_post_details/' + str(id))
    return render(request, 'customers/customer_food_post_details.html', temp)



def item_increase(request, id):
    product = Cart.objects.get(id = id)
    product.quantity = product.quantity + 1
    product.save()
    return redirect('../customer_view_cart')

def item_decrease(request, id):
    product = Cart.objects.get(id=id)
    if product.quantity > 1:
        product.quantity = product.quantity - 1
        product.save()
    return redirect('../customer_view_cart')


#customer_view_cart
def customer_view_cart(request):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    user=request.user
    cart_items = Cart.objects.filter(user=user, status='Cart')

    temp['title'] = 'Food Cart'
    temp['sub_title'] = 'Cart'
    temp['cart_items']= cart_items
    temp['cart'] = navCart(request)

    price = 0
    for i in cart_items:
        price = price + i.post.new_price

    temp['price'] = price
    temp['total_price'] = 40 + price
    temp['total_items'] = len(cart_items)

    if request.method == 'POST':
        transaction_id = request.POST['trxid']

        for i in cart_items:
            cartItem = Cart.objects.get(id=i.id)
            cartItem.transaction_id = transaction_id
            cartItem.status = 'Active'
            cartItem.save()
        messages.success(request, "Order submitted successfully")
        return redirect('../customer_view_cart')
    return render(request, 'customers/customer_view_cart.html', temp)




def customer_delete_cart_item(request, id):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')

    temp['cart'] = navCart(request)
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('../customer_view_cart')







#customer_order
def customer_order(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    
    temp['title'] = 'Order Details'
    temp['sub_title'] = 'Orders'
    temp['cart'] = navCart(request)

    active_orders = Cart.objects.filter(user=request.user, status='Active')
    prev_orders = Cart.objects.filter(user=request.user, status='Delivered')

    total_money = 0
    for i in active_orders:
        total_money = total_money + i.post.new_price

    prev_total = 0
    for i in prev_orders:
        prev_total = prev_total + i.post.new_price


    temp['orders'] = active_orders
    temp['size'] = len(active_orders)
    temp['past_order'] = len(prev_orders)
    temp['prev_order'] = prev_orders
    temp['prev_total'] = prev_total
    temp['total_amount'] = total_money

    return render(request, 'customers/customer_order.html', temp)



# Restaurants View

def restaurants_signup(request):
    temp['title'] = 'Sign Up As a Restaurants'
    temp['sub_title'] = 'Sign Up'
    temp['error'] = ''
    if request.method == 'POST':
        name = request.POST['rname']
        email = request.POST['email']
        address = request.POST['address']
        image = request.FILES['image']
        password = request.POST['password']
        contact_no = request.POST['contact']
        description = request.POST['description']
        try:
            user = User.objects.create_user(first_name=name, username=email, password=password)
            Restaurant.objects.create(user=user, name=name, contact_no=contact_no, image=image, address=address, type='restaurant', description = description, status='approved')              # will be edited!
            messages.warning(request, 'Something went wrong! Please try again...')
        except:
            messages.error(request, 'Email or password is wrong!')
    return render(request, 'visitors/restaurants_signup.html', temp)



def restaurants_login(request):
    temp['title'] = 'Restaurant LogIn'
    temp['sub_title'] = 'Restaurant Login'
    temp['error'] = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            try:
                user1 = Restaurant.objects.get(user=user)
                if user1.type == "restaurant" and user1.status != 'pending':
                    login(request, user)
                    temp['error'] = 'no'
                    return redirect('customers:restaurants_home')
                else:
                    messages.error(request, 'Please wait for the Admin approval.')
            except:
                messages.error(request, 'Email is not identified. Please sign up first.')
        else:
            messages.error(request, 'Email or password is wrong!')
    return render(request, 'visitors/restaurants_login.html', temp)





def restaurants_home(request):
    temp['title'] = 'Nilomtron'

    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    return render(request, 'restaurants/restaurants_home.html', temp)


def restaurants_change_password(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['error'] = ''
    if request.method == 'POST':
        currentPass = request.POST['currentpassword']
        newPass = request.POST['newpassword']
        try:
            user = User.objects.get(id=request.user.id)
            if user.check_password(currentPass):
                user.set_password(newPass)
                user.save()
                temp['error'] = 'no'
            else:
                temp['error'] = 'not'
        except:
            error = 'yes'
    return render(request, 'restaurants/restaurants_change_password.html', temp)


def restaurants_add_post(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['error'] = ''
    x = request.user
    y = Restaurant.objects.get(user=x)
    temp['location'] = y.address
    temp['category'] = Category.objects.all()

    if request.method == 'POST':
        post_title = request.POST['post_title']
        description = request.POST['description']
        prev_price = request.POST['prev_price']
        new_price = request.POST['new_price']
        image = request.FILES['image']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        location = request.POST['post_location']
        category = request.POST['category']
        name = request.user.first_name
        
        user = request.user
        restaurant = Restaurant.objects.get(user = user)

        try:
            Post.objects.create(restaurant=restaurant, name=name, start_date=start_date, end_date=end_date, title=post_title, description=description, location=location, prev_price=prev_price, new_price=new_price, image=image, category=category, creation_date=date.today())
            messages.success(request, 'Item has been added successfully.')
        except:
            messages.error(request, 'Something went wrong. Please try again!')
    return render(request, 'restaurants/restaurants_add_post.html', temp)


def restaurant_all_post(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['title'] = 'Restaurant All Posts'
    temp['sub_title'] = 'Restaurant All Posts'
    nums='a'
    if 'search' in request.GET:
        q=request.GET['search']
        t=q.isdigit()
        if t==1:
            p=int(q) 
            p2=p-10
            p3=p+10
            p4=p-20
            p5=p+20
            p6=p-5
            p7=p+5
            p8=p-15
            p9=p+15
            p10=p-25
            p11=p+25
            p12=p+1
            p13=p+2
            p14=p+3
            p15=p+4
            p16=p+6
            p17=p+7
            p18=p+8
            p19=p+9
            p20=p-1
            p21=p-2
            p22=p-3
            p23=p-4
            p24=p-6
            p25=p-7
            p26=p-8
            p27=p-9
            p28=p+11
            p29=p+12
            p30=p+13
            p31=p+14
            p32=p-11
            p33=p-12
            p34=p-13
            p35=p-14

            posts=Post.objects.filter(Q(new_price=q)| Q(new_price=p2)|Q(new_price=p3)|Q(new_price=p5)|Q(new_price=p4)
            |Q(new_price=p6)|Q(new_price=p7)|Q(new_price=p8)|Q(new_price=p9)|Q(new_price=p10)|Q(new_price=p11)
            |Q(new_price=p12)|Q(new_price=p13)|Q(new_price=p14)|Q(new_price=p15)|Q(new_price=p16)|Q(new_price=p17)
            |Q(new_price=p18)|Q(new_price=p19)|Q(new_price=p20)|Q(new_price=p21)|Q(new_price=p22)|Q(new_price=p23)
            |Q(new_price=p24)|Q(new_price=p25)|Q(new_price=p26)|Q(new_price=p27)|Q(new_price=p28)|Q(new_price=p29)
            |Q(new_price=p30)|Q(new_price=p31)|Q(new_price=p32)|Q(new_price=p33)|Q(new_price=p34)|Q(new_price=p35)
            )
        else:
            posts=Post.objects.filter(
            Q(title__icontains=q) | Q(location__icontains=q)| Q(description__icontains=q)
            | Q(name__icontains=q) | Q(category__icontains=q))

    else:
        # Paginator
        post = Post.objects.all()
        per_page = 4
        all_post = Paginator(post, per_page)
        page = request.GET.get('page')
        venu = all_post.get_page(page)
        nums = 'a' * venu.paginator.num_pages
        
        try:
            posts = all_post.get_page(page)
        except PageNotAnInteger:
            posts = all_post.page(1)
        except EmptyPage:
            posts = all_post.page(all_post.num_page)
    temp['total_posts'] = posts
    temp['nums'] = nums
    return render(request, 'customers/restaurant_all_post.html', temp)


def restaurants_food_posts(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    user = request.user
    restaurant = Restaurant.objects.get(user=user)
    post = Post.objects.filter(restaurant=restaurant)
    temp['post'] = post
    return render(request, 'restaurants/restaurants_food_posts.html', temp)



def restaurants_edit_post(request, id):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    temp['error'] = ''
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        post_title = request.POST['post_title']
        description = request.POST['description']
        prev_price = request.POST['prev_price']
        new_price = request.POST['new_price']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        location = request.POST['post_location']
        
        post.title = post_title
        post.dexcription = description
        post.prev_price = prev_price
        post.new_price = new_price
        post.location = location

        try:
            post.save()
            temp['error'] = 'no'
        except:
            temp['error'] = 'yes'

        if start_date:
            try:
                post.start_date = start_date
                post.save()
            except:
                pass

        if end_date:
            try:
                post.end_date = end_date
                post.save()
            except:
                pass

    temp['post'] = post
    return render(request, 'restaurants/restaurants_edit_post.html', temp)





def restaurants_delete_post(request, id):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    posts = Post.objects.get(id=id)
    posts.delete()
    return redirect('../restaurants_food_posts')



def restaurants_pending_order(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    res = Restaurant.objects.get(user=request.user.id)

    active_order = Cart.objects.filter(restaurant=res, status='Active')
    temp['pending_order'] = len(active_order)
    temp['active_order'] = active_order
    return render(request, 'restaurants/restaurants_pending_order.html', temp)


def restaurants_update_status(request, id):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    post = Cart.objects.get(id=id)

    if request.method == 'POST':
        status = request.POST['status']
        post.status = status
        post.save()
        post = Cart.objects.get(id=id)
        messages.success(request, 'Status has been updated successfully!')
    temp['post'] = post

    return render(request, 'restaurants/restaurants_update_status.html', temp)
        





def restaurants_delivered_order(request):
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    res = Restaurant.objects.get(user=request.user.id)

    delivered_order = Cart.objects.filter(restaurant=res, status='Delivered')
    temp['delivered_order'] = delivered_order
    temp['size'] = len(delivered_order)
    return render(request, 'restaurants/restaurants_delivered_order.html', temp)



# Autosuggest
def autosuggest(request):
    if 'term' in request.Get:
        qs=Post.objects.filter(Q(title__icontains=request.Get.get('term')))
        titles = list()
        for x in qs:
            titles.append(x.title)
        return JsonResponse(titles, safe=False)

    return render(request, 'customers/customer_all_post.html')

#customer_profile
def customer_profile(request):
    temp['title'] = 'Profile'
    temp['sub_title'] = 'Profile'
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    user=request.user
    data=Customer.objects.get(user=user)
    temp['info'] = data
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        user.first_name = fname
        user.last_name = lname
        data.address = address
        data.contact_no = contact_no
        data.gender = gender
        user.save()
        data.save()
    return render(request, 'customers/customer_profile.html', temp)
    
    
#restaurant_profile
def restaurant_profile(request):
    temp['title'] = 'Nimontron'
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    user=request.user
    try:
        data=Customer.objects.get(user=user)
    except:
        data=Customer.objects.all().first
    temp['info'] = data
    return render(request, 'restaurants/restaurant_profile.html', temp) 



# Restaurant Donation Part

#Restaurants Donation Post
def restaurants_donation_post(request):
    return render(request, 'restaurants/restaurants_donation_post.html', temp)






#foundation_profile
def foundation_profile(request):
    temp['title'] = 'Nimontron'
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    user=request.user
    try: 
        data=Customer.objects.get(user=user)
    except:
        data=Customer.objects.all().first
    print(data)
    temp['info'] = data
    return render(request, 'customers/restaurant_profile.html', temp)



#Foundation


def foundation_login(request):
    temp['title'] = 'Foundation LogIn'
    temp['sub_title'] = 'Foundation Login'
    temp['error'] = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            try:
                user1 = Foundation.objects.get(user=user)
                if user1.type == "foundation" and user1.status != 'pending' :
                    login(request, user)
                    temp['error'] = 'no'
                    return redirect('customers:foundation_home')
                else:
                    temp['error'] = 'not'
            except:
                temp['error'] = 'yes'
        else:
            temp['error'] = 'yes'
    return render(request, 'visitors/foundation_login.html', temp)



def foundation_home(request):
    temp['title'] = 'Nimontron'
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    return render(request, 'foundations/foundation_home.html', temp)


def foundation_signup(request):
    temp['title'] = 'Sign Up As a Foundation'
    temp['sub_title'] = 'Sign Up'
    temp['error'] = ''
    if request.method == 'POST':
        first_name = request.POST['rname']
        email = request.POST['email']
        address = request.POST['address']
        image = request.FILES['image']
        password = request.POST['password']
        contact_no = request.POST['contact']
        description = request.POST['description']
        ngo_code=request.POST['ngo_code']
        Date_of_Establishment=request.POST['Date_of_Establishment']
    
        user = User.objects.create_user(first_name=first_name, username=email, password=password)
        Foundation.objects.create(user=user, contact_no=contact_no,description = description,address=address, image=image, code_no= ngo_code, Doe=Date_of_Establishment, type='foundation', status='pending')
        temp['error'] = 'no'

    return render(request, 'visitors/foundation_signup.html', temp)






def foundation_add_post(request):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    temp['error'] = ''
    if request.method == 'POST':
    
        title=request.POST['post_title']
        description = request.POST['description']
        items=request.POST['items']
        quantity=request.POST['quantity']
        contact=request.POST['contact']
        area=request.POST['area']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date'] 

        user = request.user
        foundation= Foundation.objects.get(user = user)
        
    
        Foundation_Post.objects.create(foundation=foundation,title=title,description=description,items=items,quantity=quantity,contact=contact,area=area,start_date=start_date,
             end_date=end_date,status='pending', creation_date=date.today(), contact_no='',fname='')
          
        temp['error'] = 'no'
        
    
    return render(request, 'foundations/foundation_add_post.html', temp)

def foundation_food_posts(request):
    if not request.user.is_authenticated:
     return redirect('customer:login_as')
    user = request.user
    foundation = Foundation.objects.get(user=user)
    post = Foundation_Post.objects.filter(foundation=foundation)
    temp['post'] = post
    return render(request, 'foundations/foundation_food_posts.html', temp)






def foundation_edit_post(request,id):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    temp['error'] = ''
    post = Foundation_Post.objects.get(id=id)


    if request.method == 'POST':
    
        title=request.POST['post_title']
        description = request.POST['description']
        items=request.POST['items']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date'] 


        post.title=title
        post.description=description
        post.items=items
        

        try:
            post.save()
            temp['error'] = 'no'
        except:
            temp['error'] = 'yes'
  

        if start_date:
            try:
                post.start_date = start_date
                post.save()
            except:
                pass

        if end_date:
            try:
                post.end_date = end_date
                post.save()
            except:
                pass

    temp['post'] = post
        
    
    return render(request, 'foundations/foundation_edit_post.html', temp)



def foundation_delete_post(request, id):
     if not request.user.is_authenticated:
        return redirect('customer:login_as')
     post=Foundation_Post.objects.filter(id=id)
     post.delete()
     return render(request, 'foundations/foundation_food_posts.html', temp)


def accept_post(request,id):
    if not request.user.is_authenticated:
        return redirect('customer:login_as')
    user=request.user
    cs=Customer.objects.get(user=user)
    post=Foundation_Post.objects.get(id=id)
    post.status="Accepted"
    post.contact_no=cs.contact_no
    post.fname=cs.user.first_name
    post.save()

    post = Foundation_Post.objects.all()
    temp['post'] = post
    return render(request, 'customers/donate.html', temp)



# For testing api
def api_customer_post(request):
    data = list(Post.objects.all().values())
    return JsonResponse(data, safe=False)


# Devliver Man

def delivery_man_signup(request):
    temp['title'] = 'Sign Up As Delivery Man'
    temp['sub_title'] = 'Sign Up'
    temp['error'] = ''
    if request.method == 'POST':
        name = request.POST['dname']
        email = request.POST['email']
        address = request.POST['address']
        image = request.FILES['image']
        password = request.POST['password']
        contact_no = request.POST['contact']
        gender = request.POST['gender']

        try:
            user = User.objects.create_user(first_name=name, username=email, password=password)
            Delivery_Man.objects.create(user=user, name=name, gender=gender, contact_no=contact_no, image=image, address=address, type='delivery_man', status='pending')              # will be edited!
            temp['error'] = 'no'
        except:
            temp['error'] = 'yes'

    return render(request, 'visitors/delivery_man_signup.html', temp)

def delivery_man_login(request):
    temp['title'] = 'Delivery Man LogIn'
    temp['sub_title'] = 'Delivery Man Login'
    temp['error'] = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            try:
                user1 = Delivery_Man.objects.get(user=user)
                if user1.type == "delivery_man" and user1.status != 'pending':
                    login(request, user)
                    temp['error'] = 'no'
                    return redirect('customers:delivery_man_home')
                else:
                    messages.error(request, 'Please wait for the Admin approval.')
                    temp['error'] = 'yes'
            except:
                messages.error(request, 'Email is not identified. Please sign up first.')
        else:
            messages.error(request, 'Email or password is wrong!')
    return render(request, 'visitors/delivery_man_login.html', temp)


def delivery_man_home(request):
    temp['title'] = 'Nilomtron'

    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    return render(request, 'delivery_man/delivery_man_home.html', temp)


def delivery_man_profile(request):
    temp['title'] = 'Profile'
    temp['sub_title'] = 'Profile'
    if not request.user.is_authenticated:
        return redirect('customers:login_as')
    user=request.user
    data=Delivery_Man.objects.get(user=user)
    temp['info'] = data
    if request.method == 'POST':
        fname = request.POST['first_name']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        user.first_name = fname
        data.address = address
        data.contact_no = contact_no
        data.gender = gender
        if len(request.FILES)!= 0:
            if len(data.image)>0:
                os.remove(data.image.path)
            data.image = request.FILES['image']
        user.save()
        data.save()
    return render(request, 'delivery_man/delivery_man_profile.html', temp)


def all_delivery_requests(request):
    if not request.user.is_authenticated:
     return redirect('customer:login_as')
    user = request.user
    all_requests = Cart.objects.all()
    temp['all_requests'] = all_requests
    return render(request, 'delivery_man/all_delivery_requests.html', temp)

def accept_delivery_requests(request):
    if not request.user.is_authenticated:
     return redirect('customer:login_as')
    user = request.user
    all_requests = Cart.objects.all()
    dm=Delivery_Man.objects.get(user=user)
    post=Foundation_Post.objects.get(id=id)
    post.status="Accepted"
    post.contact_no=cs.contact_no
    post.fname=cs.user.first_name
    post.save()
    temp['all_requests'] = all_requests
    return render(request, 'delivery_man/all_delivery_requests.html', temp)

def order_request_delivered(request):
    if not request.user.is_authenticated:
     return redirect('customer:login_as')
    user = request.user
    all_requests = Cart.objects.all()
    temp['all_requests'] = all_requests
    return render(request, 'delivery_man/all_delivery_requests.html', temp)
