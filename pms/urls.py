from django.urls import path
from .views import BuildingListCreate, BuildingGetUpdateDelete, RoomListCreate, \
RoomGetUpdateDelete

urlpatterns = [
    path('buildings/', BuildingListCreate.as_view(), name='building-list-create'),
    path('buildings/<int:building_id>/', BuildingGetUpdateDelete.as_view(), name='building-get-update-delete'),
    path('rooms/', RoomListCreate.as_view(), name='room-list-create'),
    path('rooms/<int:room_id>/', RoomGetUpdateDelete.as_view(), name='room-get-update-delete')
]