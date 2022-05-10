import json

from django.views import View
from django.http import JsonResponse

from .models import Category, Product, Nutrition, Menu

class ProductsView(View):

    def get(self, request):
        # 상품 정보를 반환해준다.
        results = []
        
        products = Product.objects.all()

        for product in products:
            results.append({
                "id"    :   product.id,
                "korean_name"   :   product.korean_name,
                "english_name"  :   product.english_name,
                "description"   :   product.description,
                "category_id"   :   product.category_id,
                "nutrition_id"  :   product.nutrition_id,
            })
        
        return JsonResponse({"products" : results}, status = 200)


    def post(self, request):
        input_data = json.loads(request.body)

        menu = Menu.objects.create(name=input_data["menu"])
        category = Category.objects.create(name=input_data["category"], menu_id=menu.id)
        nutritioin = Nutrition.objects.create(
            protein_g = input_data["protein"],
            sodium_mg = input_data["sodium"],
            size_ml = input_data["size"],
        )
        product = Product(
            korean_name = input_data["korean_name"],
            english_name = input_data["english_name"],
            description = input_data["description"],
            category_id = category.id,
            nutrition_id = nutritioin.id,
        )
        product.save()

        return JsonResponse({"message" : "SUCCESS"}, status = 201)