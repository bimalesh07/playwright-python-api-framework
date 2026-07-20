# 📂 Test_Case/test_api/test_Product.py
import pytest
import random
from utilities.Custom_logger import LogGen

class TestProductModule:
    logger = LogGen.loggen()
    assigned_category_id = None
    created_product_id = None
    product_slug = None
    
    product_title = f"Premium Leather Boots {random.randint(100, 999)}"

    @pytest.fixture(scope="function", autouse=True)
    def setup_temporary_category(self, categories_client):
        if TestProductModule.assigned_category_id is None:
            self.logger.info("Creating a dedicated category for Product testing...")
            cat_payload = {
                "name": f"Footwear {random.randint(1000, 9999)}",
                "image": "https://picsum.photos/640/480"
            }
            res = categories_client.create_category(cat_payload)
            assert res.status == 201
            TestProductModule.assigned_category_id = res.json()["id"]
            self.logger.info(f"Temporary Category created with ID: {TestProductModule.assigned_category_id}")
        
        yield 
        pass

    # CREATE PRODUCT ----------------
    def test_create_product_with_category(self, product_client):
        obj = product_client
        payload = {
            "title": TestProductModule.product_title,
            "price": 299,
            "description": "Handcrafted premium quality pure leather boots.",
            "categoryId": TestProductModule.assigned_category_id,
            "images": ["https://picsum.photos/640/480"]
        }
        res = obj.Create_Product(payload)
        assert res.status == 201
        
        res_data = res.json()
        assert res_data["title"] == TestProductModule.product_title
        
        TestProductModule.created_product_id = res_data["id"]
        TestProductModule.product_slug = res_data.get("slug", "boots-slug")
        self.logger.info(f"Product created successfully! ID: {TestProductModule.created_product_id}")

    # GET ALL PRODUCTS ----------------
    def test_get_all_products_validation(self, product_client):
        obj = product_client
        mandatory_params = {"offset": 0, "limit": 10}
        res = obj.Get_all_products(params=mandatory_params)
        assert res.status == 200
        products_list = res.json()
        assert isinstance(products_list, list)

    #GET PRODUCT BY ID ----------------
    def test_get_product_by_id(self, product_client):
        obj = product_client
        prod_id = TestProductModule.created_product_id
        res = obj.Get_BY_Product_id(prod_id)
        assert res.status == 200
        assert res.json()["title"] == TestProductModule.product_title

    #GET RELATED PRODUCTS BY ID ----------------
    def test_get_related_products_by_id(self, product_client):
        obj = product_client
        prod_id = TestProductModule.created_product_id
        res = obj.Get_Related_Products(prod_id)
        assert res.status == 200
        assert isinstance(res.json(), list)

    #TEST CASE: GET PRODUCT BY SLUG ----------------
    def test_get_product_by_slug(self, product_client):
        obj = product_client
        slug_to_test = TestProductModule.product_slug if TestProductModule.product_slug else "boots-slug"
        res = obj.Get_Product_By_Slug(slug_to_test)
        if res.status == 200:
            assert "id" in res.json()

    #GET RELATED PRODUCTS BY SLUG ----------------
    def test_get_related_products_by_slug(self, product_client):
        obj = product_client
        slug_to_test = TestProductModule.product_slug if TestProductModule.product_slug else "boots-slug"
        res = obj.Get_Related_Products_By_Slug(slug_to_test)
        if res.status == 200:
            assert isinstance(res.json(), list)

    # UPDATE PRODUCT 
    def test_update_product_validation(self, product_client):
        prod_id = TestProductModule.created_product_id
        
        get_current = product_client.Get_BY_Product_id(prod_id)
        assert get_current.status == 200
        current_data = get_current.json()
        
       
        update_payload = {
            "title": f"Updated {TestProductModule.product_title}",
            "price": 199,
            "description": current_data["description"],
            "categoryId": TestProductModule.assigned_category_id,
            "images": current_data["images"]
        }
        
        res_update = product_client.Update_By_prodcut_id(prod_id, update_payload)
        
        assert res_update.status == 200
        assert res_update.json()["price"] == 199
        self.logger.info(f"Product ID {prod_id} successfully updated with new price!")

    #DELETE PRODUCT & CLEANUP ----------------
    def test_delete_product_and_cleanup(self, product_client, categories_client):
        prod_id = TestProductModule.created_product_id
        
        
        res_delete = product_client.Delete_Product_id(prod_id)
        assert res_delete.status == 200
        self.logger.info(f"Product ID {prod_id} deleted successfully.")
        

        res_cat_delete = categories_client.delete_category(TestProductModule.assigned_category_id)
        assert res_cat_delete.status == 200
        self.logger.info("Main Category completely cleaned up from database.")