from django.urls import path
from notice import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('notice/', views.notice, name='notice'),
                  path('save-notice/', views.save_notice, name='save_notice'),
                  path('get-single-notice-detail/', views.get_single_notice_detail, name='get_single_notice_detail'),
                  path('delete-single-notice-detail/', views.delete_single_notice_detail,
                       name='delete_single_notice_detail'),
                  path('filter-notice/', views.filter_notice, name='filter_notice'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
