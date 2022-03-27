from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import autosuggest

app_name = 'customers'

urlpatterns = [
    # Normal User
    path('', views.index, name='index'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
    path('donate_others', views.donate, name='donate'),
    path('contact', views.contact, name='contact'),
    path('restaurants', views.restaurant_lists, name='restaurant_lists'),


    # Delivery_Man
    path('delivery_man_signup', views.delivery_man_signup, name='delivery_man_signup'),
    path('delivery_man_login', views.delivery_man_login, name='delivery_man_login'),
    path('delivery_man_home', views.delivery_man_home, name='delivery_man_home'),
    path('delivery_man_profile', views.delivery_man_profile, name='delivery_man_profile'),
    
    # Customer
    path('signup', views.signup, name='signup'),
    path('login_as', views.login_as, name='login_as'),
    path('customer_login', views.customer_login, name='customer_login'),
    path('customer_home', views.customer_home, name='customer_home'),
    path('customer_all_post', views.customer_all_post, name='customer_all_post'),
    path('customer_all_restaurants', views.customer_all_restaurants, name='customer_all_restaurants'),
    path('Logout', views.Logout, name='Logout'),
    path('customer_food_post_details/<int:id>', views.customer_food_post_details, name='customer_food_post_details'),
    path('cart_item_decrease/<int:id>', views.cart_item_decrease, name='cart_item_decrease'),

    # Restaurants
    path('restaurants_signup', views.restaurants_signup, name='restaurants_signup'),
    path('restaurants_login', views.restaurants_login, name='restaurants_login'),
    path('restaurants_home', views.restaurants_home, name='restaurants_home'),
    path('restaurants_change_password', views.restaurants_change_password, name='restaurants_change_password'),
    path('restaurants_add_post', views.restaurants_add_post, name='restaurants_add_post'),
    path('restaurants_food_posts', views.restaurants_food_posts, name='restaurants_food_posts'),
    path('restaurants_edit_post/<int:id>', views.restaurants_edit_post, name='restaurants_edit_post'),
    path('restaurants_delete_post/<int:id>', views.restaurants_delete_post, name='restaurants_delete_post'),
    path('restaurant_all_post', views.restaurant_all_post, name='restaurant_all_post'),
    path('restaurants_pending_order', views.restaurants_pending_order, name='restaurants_pending_order'),
    path('restaurants_delivered_order', views.restaurants_delivered_order, name='restaurants_delivered_order'),
    path('restaurants_update_status/<int:id>', views.restaurants_update_status, name='restaurants_update_status'),

    # Restaurants Donation Part
    path('restaurants_donation_post', views.restaurants_donation_post, name='restaurants_donation_post'),


 # Foundations
    path('foundation_login', views.foundation_login, name='foundation_login'),
    path('foundation_home', views.foundation_home, name='foundation_home'),
    path('foundation_signup', views.foundation_signup, name='foundation_signup'),
    path('foundation_add_post', views.foundation_add_post, name='foundation_add_post'),
    path('foundation_food_posts', views.foundation_food_posts, name='foundation_food_posts'),
    path('foundation_edit_post/<int:id>', views.foundation_edit_post, name='foundation_edit_post'),
    path('foundation_delete_post/<int:id>', views.foundation_delete_post, name='foundation_delete_post'),
    path('accept_post/<int:id>', views.accept_post, name='accept_post'),
    
#foundation_profile
     path('foundation_profile', views.foundation_profile, name='foundation_profile'),



    # Autosuggest
    path('autosuggest', views.autosuggest, name='autosuggest'),

    #customer_profile
    path('customer_profile', views.customer_profile, name='customer_profile'),

     #restaurant_profile
    path('restaurant_profile', views.restaurant_profile, name='restaurant_profile'),
    
    

    #customer_view_cart
    path('customer_view_cart', views.customer_view_cart, name='customer_view_cart'),
    path('customer_order', views.customer_order, name='customer_order'),
    path('item_increase/<int:id>', views.item_increase, name='item_increase'),
    path('item_decrease/<int:id>', views.item_decrease, name='item_decrease'),
    

    path('customer_delete_cart_item/<int:id>', views.customer_delete_cart_item, name='customer_delete_cart_item'),
    
    
    # For testing api
    
    path('api/customer_post', views.api_customer_post),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)