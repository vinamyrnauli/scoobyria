from django.urls import path
from main.views import show_main, create_product, add_product, decrement_product, remove_product, show_xml, show_json, show_xml_by_id, show_json_by_id, get_product_json, add_product_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('add-product/<int:product_id>/', add_product, name='add_product'),
    path('decrement-product/<int:product_id>/', decrement_product, name='decrement_product'),
    path('remove-product/<int:product_id>/',
    remove_product, name='remove_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]