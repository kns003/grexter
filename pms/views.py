from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Building, Room

class BuildingListCreate(View):

    def get(self, request, *args, **kwargs):
        building_json = [building.to_dict() for building in
                         Building.objects.filter(is_active=True)]
        return JsonResponse({'status': True, 'buildings': building_json})

    def post(self, request, *args, **kwargs):
        """
        Sample post data to create building:

        {"name": "Aquila",
        "landmark_1": "HSR Layout",
        "landmark_2": "6th sector",
        "landmark_3": "near bds complex"}
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.POST.dict()
        try:
            building = Building.objects.create(
                **data
            )
        except Exception as e:
            return JsonResponse({'status': False, 'msg': str(e)})
        return JsonResponse({'status': True,
                             'msg': 'Building successfully created',
                             'building_id': building.id})

class BuildingGetUpdateDelete(View):

    def get(self, request, building_id, *args, **kwargs):
        try:
            building = Building.objects.get(id=building_id)
        except Exception as e:
            return JsonResponse({'status': False, 'msg': str(e)})
        return JsonResponse({'status': True, 'building': building.to_dict()})

    def put(self, request, building_id, *args, **kwargs):
        building = Building.objects.filter(id=building_id)
        if not building.exists():
            return JsonResponse({'status': False, 'msg': 'Building does not exist'})
        data = request.POST.dict()
        building.update(**data)
        return JsonResponse({'status': True, 'msg':'Buidling details updated successfully'})

    def delete(self, request, building_id, *args, **kwargs):
        building = Building.objects.filter(id=building_id)
        if not building.exists():
            return JsonResponse(
                {'status': False, 'msg': 'Building does not exist'})
        building.delete()
        return JsonResponse(
            {'status': True, 'msg': 'Building deleted'})

class RoomListCreate(View):
    def get(self, request, *args, **kwargs):
        room_json = [room.to_dict() for room in
                         Room.objects.filter(is_active=True)]
        return JsonResponse({'status': True, 'buildings': room_json})

    def post(self, request, *args, **kwargs):
        """
        Sample post data to create building:

        {"name": "Aquila",
        "landmark_1": "HSR Layout",
        "landmark_2": "6th sector",
        "landmark_3": "near bds complex"}
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.POST.dict()
        try:
            room = Room.objects.create(
                **data
            )
        except Exception as e:
            return JsonResponse({'status': False, 'msg': str(e)})
        return JsonResponse({'status': True,
                             'msg': 'Room successfully created',
                             'building_id': room.id})

class RoomGetUpdateDelete(View):

    def get(self, request, room_id, *args, **kwargs):
        try:
            room = Room.objects.get(id=room_id)
        except Exception as e:
            return JsonResponse({'status': False, 'msg': str(e)})
        return JsonResponse({'status': True, 'room': room.to_dict()})

    def put(self, request, room_id, *args, **kwargs):
        room = Room.objects.filter(id=room_id)
        if not room.exists():
            return JsonResponse({'status': False, 'msg': 'Room does not exist'})
        data = request.POST.dict()
        room.update(**data)
        return JsonResponse({'status': True, 'msg':'Room details updated successfully'})

    def delete(self, request, room_id, *args, **kwargs):
        room = Room.objects.filter(id=room_id)
        if not room.exists():
            return JsonResponse(
                {'status': False, 'msg': 'Room does not exist'})
        room.delete()
        return JsonResponse(
            {'status': True, 'msg': 'Room deleted'})
