import json
from django.views import View

from .models import Category, Product, Nutrition, Menu
class ProductsView(View):
    pass
    # def post(self, request):
        
    #     목적    : Client에서 보내는 상품정보(category, korean_name, english_name, description, protein, size, sodium)을
    #             database의 products 테이블에 저장한다.
        
        
    #     input   :
    #         {
    #             "menu": "drinks"
    #             "catagory" : "cold brew",
    #             "description" : "test",
    #             "korean_name" : "나이트로 바닐라 크림",
    #             "english_name" : "Nitro Vanila Cream",
    #             "protein": 10.3,
    #             "size" : 60.5,
    #             "sodium": 10.5,
    #         }
        
    #     input_data = json.loads(request.body) # use json, convert to dictionary
        
    #     menu= Menu.objects.create(name=input_data["menu"])
    #     category = Category.objects.create(name=input_data["category"], menu=menu)
    #     nutrition = Nutrition.objects.create(
    #         protein_g = input_data["protein"],
    #         sodium_mg = input_data["sodium"],
    #         size_ml = input_data["size"]
    #     )
    #     product = Product(
    #         korean_name = ,
    #         english_name = ,
    #         description = ,


    #     )

    #         Category 모델 사용, category 테이블에 row를 추가
    #         Nutrition 모델 사용, nutrition table (protein, size, sodium)
    #         Product 모델 사용
            
    #     output  :
    #         {
    #             "message" : "SUCCESS"
    #         }, status_code = 201

        
        
        

    # def get(self, request):
    #     pass