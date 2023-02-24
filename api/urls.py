from django.urls import path
from .views import ArtistList, WorkList, ClientCreate

urlpatterns = [
    # path('api/clients/', ClientList.as_view()),
    path('api/artists/', ArtistList.as_view(), name='artists-list'),
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/register/', ClientCreate.as_view(), name='client-create'),
]
