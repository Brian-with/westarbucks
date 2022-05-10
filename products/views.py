import json

from django.views import View
from django.http import JsonResponse

from .models import Category, Product, Nutrition, Menu

class ProductsView(View):
    def post(self, request):
        input_data = json.loads(request.body)
        menu = Menu.objects.create(name=input_data["menu"])
        category = Category.objects.create(name=input_data["category"], menu_id=menu.id)
        nutritioin = Nutrition.objects.create(
            protein_g = input_data["protein"],
            sodium_mg = input_data["sodium"],
            size_ml = input_data["size"]
        )
        product = Product(
            korean_name = input_data["korean_name"],
            english_name = input_data["enlish_name"],
            description = input_data["description"],
            category_id = category.id,
            nutrition_id = nutritioin.id
        )

        return JsonResponse({"message" : "SUCCESS"}, status_code=201)