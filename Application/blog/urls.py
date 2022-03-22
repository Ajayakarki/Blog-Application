from unicodedata import name
from django.urls import path
from .import views
from .views import PostView, PostDetail, PostCreate, PostUpdate, PostDelete, CommentView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.index, name='blog-home'),
    path('', PostView.as_view(), name='blog-home'),

    path('<int:pk>/comment/', CommentView.as_view(), name='blog_comment'),



    
    
    path('post/<pk>/', PostDetail.as_view(), name='post-detail'),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('post/<pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDelete.as_view(), name='post-delete'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)