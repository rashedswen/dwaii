from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from medicine.views import search, allMedicine, sign, logout_backend, \
    profile, add_to_storage, productinfo, Registerinfo, editproduct, \
    editproductBackend, addMedicine, requestMedicine, requestList, visitorProfile, requestinfo, addBranch, \
    searchRequest, searchdonate, donateList, Editinfo, edit_medicine, signup, medicineList, medicineDetail, storageList, \
    pharmacyList, MedicineListView, UserRecordView
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('search', search, name='search'),
                  path('searchRequest', searchRequest, name='searchRequest'),
                  path('searchDonate', searchdonate, name='searchDonate'),
                  path('sign/', sign, name='sign'),
                  path('signup/', signup, name='signup'),
                  path('', allMedicine, name='allMedicine'),
                  path('requestList/', requestList, name='requestList'),
                  path('donateList/', donateList, name='donateList'),
                  path('request/add', requestMedicine, name='requestMedicine'),
                  path('profile/add_to_storage/', add_to_storage, name='add_to_storage'),
                  path('profile/addMedicine/', addMedicine, name='addMedicine'),
                  path('profile/medicine/<int:medId>', edit_medicine, name='edit_medicine'),
                  path('profile/', profile, name='profile'),
                  path('profile/<int:phUrl>', visitorProfile, name='visitProfile'),
                  path('logout/', logout_backend, name='logout'),
                  path('info/<int:productId>', productinfo, name='productinfo'),
                  path('request/info/<int:requestId>', requestinfo, name='requestinfo'),
                  path('info/edit/<int:productId>', editproduct, name='editproduct'),
                  path('info/editBackend/<int:productId>', editproductBackend, name='editproductBackend'),
                  path('profile/inforegister', Registerinfo, name='infoRegister'),
                  path('profile/addBranch', addBranch, name='addBranch'),
                  path('profile/edit_information', Editinfo, name='edit_information'),

                  # API VIEWS
                  path('api/medicine/', medicineList, name='apiFlutterMedicine'),
                  path('api/storage', storageList, name='apiFlutterStorage'),
                  path('api/pharmacy/', pharmacyList, name='apiFlutterPharmacy'),
                  path('api/medicine/<str:pk>', medicineDetail, name='apiFlutterMed'),
                  
                  # Authentication
                  path('user/', UserRecordView.as_view(), name='users'),

                  # reset password
                  path('reset_password', auth_views.PasswordResetView.as_view(template_name="resetPassword.html"),
                       name='reset_password'),
                  path('reset_password_sent',
                       auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
                       name='password_reset_confirm'),
                  path('reset_password_complete',
                       auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                       name='password_reset_complete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
