from ninja import NinjaAPI

from api.teacher_router import teacher_router

api = NinjaAPI()
api.add_router("/teacher", teacher_router)
