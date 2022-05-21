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
    path('all_delivery_requests', views.all_delivery_requests, name='all_delivery_requests'),
    path('accept_delivery_requests/<str:rand_order_id>/<str:status>', views.accept_delivery_requests, name='accept_delivery_requests'),
    path('order_delivered/<str:rand_order_id>/<str:status>', views.order_delivered, name='order_delivered'),
    path('delivery_details', views.delivery_details, name='delivery_details'),
    
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
    path('customer_add_donate_post', views.customer_add_donate_post, name='customer_add_donate_post'),
    path('customer_all_donate_post', views.customer_all_donate_post, name='customer_all_donate_post'),
    path('customer_edit_donate_post/<int:id>', views.customer_edit_donate_post, name='customer_edit_donate_post'),
    path('customer_delete_donate_post/<int:id>', views.customer_delete_donate_post, name='customer_delete_donate_post'),

    #customer_view_cart
    path('customer_view_cart', views.customer_view_cart, name='customer_view_cart'),
    path('customer_checkout_address', views.customer_checkout_address, name='customer_checkout_address'),
    path('customer_payment_method', views.customer_payment_method, name='customer_payment_method'),
    path('customer_order_review', views.customer_order_review, name='customer_order_review'),
    path('customer_order', views.customer_order, name='customer_order'),
    path('item_increase/<int:id>', views.item_increase, name='item_increase'),
    path('item_decrease/<int:id>', views.item_decrease, name='item_decrease'),
    path('customer_delete_cart_item/<int:id>', views.customer_delete_cart_item, name='customer_delete_cart_item'),
    path('customer_order_successfull', views.customer_order_successfull, name='customer_order_successfull'),
    path('customer_order_details/<str:rand_order_id>', views.customer_order_details, name='customer_order_details'),

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

    path('restaurants_order_details/<str:rand_order_id>', views.restaurants_order_details, name='restaurants_order_details'),

    path('restaurant_pending_order_status/<str:rand_order_id>/<str:status>', views.restaurant_pending_order_status, name='restaurant_pending_order_status'),

    # Restaurants Donation Part
    path('restaurants_add_donation_post', views.restaurants_add_donation_post, name='restaurants_add_donation_post'),


 # Foundations
    path('foundation_login', views.foundation_login, name='foundation_login'),
    path('foundation_home', views.foundation_home, name='foundation_home'),
    path('foundation_signup', views.foundation_signup, name='foundation_signup'),
    path('foundation_add_post', views.foundation_add_post, name='foundation_add_post'),
    path('foundation_food_posts', views.foundation_food_posts, name='foundation_food_posts'),
    path('foundation_edit_post/<int:id>', views.foundation_edit_post, name='foundation_edit_post'),
    path('foundation_delete_post/<int:id>', views.foundation_delete_post, name='foundation_delete_post'),
    path('accept_post/<int:id>', views.accept_post, name='accept_post'),
    path('foundation_others_donation_post', views.foundation_others_donation_post, name='foundation_others_donation_post'),
   path('foundation_accept_donate_post', views.foundation_accept_donate_post, name='foundation_accept_donate_post'),
   path('accepted_posts_foundation', views.accepted_posts_foundation, name='accepted_posts_foundation'),
    


#Foundation APIs
   path('foundation_all_other_donate_post', views.foundation_all_other_donate_post, name='foundation_all_other_donate_post'),

    

#foundation_profile
     path('foundation_profile', views.foundation_profile, name='foundation_profile'),



    # Autosuggest
    path('autosuggest', views.autosuggest, name='autosuggest'),

    #customer_profile
    path('customer_profile', views.customer_profile, name='customer_profile'),

     #restaurant_profile
    path('restaurant_profile', views.restaurant_profile, name='restaurant_profile'),
    
    

    
    
    
    # For testing api
    
    path('api/customer_post', views.api_customer_post),
    path('api/customer_donate_post', views.customer_donate_post, name='customer_donate_post'),
    path('api/customer_delete_specific_donate_post/<int:id>', views.customer_delete_specific_donate_post, name='customer_delete_specific_donate_post'),
    path('api/customer_edit_specific_donate_post/<int:id>', views.customer_edit_specific_donate_post, name='customer_edit_specific_donate_post'),

    path('customer_edit_s_donate_post', views.customer_edit_s_donate_post, name='customer_edit_s_donate_post'),

    path('api/customer_specific_donate_post/<int:id>', views.customer_specific_donate_post, name='customer_specific_donate_post'),
    path('ajax_get_view', views.ajax_get_view, name='ajax_get_view'),


    #admin_part
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    
    path('view_restaurants', views.view_restaurants, name='view_restaurants'),
    path('delete_restaurant/<int:id>',views.delete_restaurant, name="delete_restaurant"),
    path('view_specific_restaurant/<int:id>', views.view_specific_restaurant, name='view_specific_restaurant'),
    

    path('view_foundations', views.view_foundations, name='view_foundations'),
    path('delete_foundation/<int:id>',views.delete_foundation, name="delete_foundation"),
    path('view_specific_foundation/<int:id>', views.view_specific_foundation, name='view_specific_foundation'),


    path('view_all_delivery_man_lists', views.view_all_delivery_man_lists, name='view_all_delivery_man_lists'),
    path('view_specific_delivery_man/<int:id>', views.view_specific_delivery_man, name='view_specific_delivery_man'),
    path('delete_specific_delivery_man_account',views.delete_specific_delivery_man_account, name="delete_specific_delivery_man_account"),
    path('edit_delivery_man_profile/<int:id>', views.edit_delivery_man_profile, name='edit_delivery_man_profile'),
    path('view_specific_delivery_man_account',views.view_specific_delivery_man_account, name="view_specific_delivery_man_account"),
    

    path('edit_restaurant/<int:id>',views.edit_restaurant, name="edit_restaurant"),
    path('edit_foundation/<int:id>',views.edit_foundation, name="edit_foundation"),

    path('all_restaurant_jsn',views.all_restaurant_jsn, name="all_restaurant_jsn"),
    path('all_foundation_jsn',views.all_foundation_jsn, name="all_foundation_jsn"),

    path('foundation_delete/<int:id>',views.foundation_delete, name="foundation_delete"),
    path('specific_foundation_view/<int:id>',views.specific_foundation_view, name="specific_foundation_view"),
    path('specific_foundation_edit_post', views.specific_foundation_edit_post, name="specific_foundation_edit_post"),

   
   
     
    


 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


