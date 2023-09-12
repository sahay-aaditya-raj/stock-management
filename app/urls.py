from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('stocks/', views.stocks, name='stocks'),
    path('stocks/<str:pk>', views.stockDel, name='stocks-del'),
    path('invoice-list/', views.invoice_list, name='invoice-list'),
    path('invoice-list/<str:pk>', views.viewSavedInvoice, name='view-saved-invoice'),
    path('pdfview/<str:pk>/', views.pdfview, name='pdfview'),
    
    path('msg/<str:msg>', views.tempMsg, name='tempMsg'),
    path('products/', views.productList, name='products'),
    path('manufacturers/', views.manufacturer, name='manufacturer'),
    path('party/', views.party, name='party'),
    path('party/<str:pk>', views.partyView, name='party-view'),
    path('add-party', views.addParty, name='add-party'),
    
    path('new-inv-menu/', views.new_invoice_menu, name='new-inv-menu'),
    path('new-temp-inv/<str:pk>/', views.new_temp_inv, name='new-temp-inv'),
    path('del-temp-ent/<str:pk>/', views.del_ent, name='del-temp-ent'),
    path('save-invoice/<str:pk>/', views.saveinvoice, name='save-invoice'),
    path('del-temp-rate-ent/<str:pk>/', views.del_rateEnt, name='del-temp-rate-ent'),
    path('save-rate-inv/<str:pk>/', views.saveRateInv, name='save-rate-inv')
]
