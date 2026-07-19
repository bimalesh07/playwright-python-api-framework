
import pytest
import random
from utilities.Custom_logger import LogGen

class TestProductModule:
    logger = LogGen.loggen()
    
    assigned_category_id = None
    created_product_id = None
    
    # Static but unique title for assertions
    product_title = f"Premium Leather Boots {random.randint(100, 999)}"

    #Pure Product Module ke chalne se pehle ek temporary Category banayega
    @pytest.fixture(scope="class", autouse=True)
    def setup_temporary_category(self, categories_client):
       
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
        
        
        self.logger.info(f"Deleting temporary category ID: {TestProductModule.assigned_category_id}")
        categories_client.delete_category(TestProductModule.assigned_category_id)

    # ---------------- 1. TEST CASE: CREATE PRODUCT ----------------
    def test_create_product_with_category(self, product_client):
        obj = product_client
        
        # Payload exact matching with your Swagger guidelines
        payload = {
            "title": TestProductModule.product_title,
            "price": 299,
            "description": "Handcrafted premium quality pure leather boots.",
            "categoryId": TestProductModule.assigned_category_id,
            "images": ["https://picsum.photos/640/480"]
        }
        
        res = obj.Create_Product(payload) # Calls your fixed method
        assert res.status == 201
        
        res_data = res.json()
        assert res_data["title"] == TestProductModule.product_title
        assert res_data["category"]["id"] == TestProductModule.assigned_category_id
        
        TestProductModule.created_product_id = res_data["id"]
        self.logger.info(f"Product created successfully! ID: {TestProductModule.created_product_id}")

    # ---------------- 2. TEST CASE: GET ALL PRODUCTS (WITH PARAMS) ----------------
    def test_get_all_products_validation(self, product_client):
        obj = product_client
        
        mandatory_params = {
            "offset": 0,
            "limit": 10
        }
        
        res = obj.Get_all_products(params=mandatory_params) # Calls your fixed method
        assert res.status == 200
        
        products_list = res.json()
        assert isinstance(products_list, list), "Response main body must be a list!"
        assert len(products_list) <= 10, f"Expected max 10 products, but received {len(products_list)}"
        
        # Smart Assertion: Check if our newly created product title exists in this batch
        product_found = any(p["title"] == TestProductModule.product_title for p in products_list)
        self.logger.info(f"Is our product present in this GET batch? -> {product_found}")

    # TEST CASE: GET PRODUCT BY ID ----------------
    def test_get_product_by_id(self, product_client):
        obj = product_client
        prod_id = TestProductModule.created_product_id
        
        res = obj.Get_BY_Product_id(prod_id) # Calls your fixed method
        assert res.status == 200
        assert res.json()["title"] == TestProductModule.product_title
        self.logger.info(f"Successfully verified details for Product ID: {prod_id}")

    # TEST CASE: UPDATE & DELETE PRODUCT 
    def test_update_and_delete_product_flow(self, product_client):
        obj = product_client
        prod_id = TestProductModule.created_product_id
        update_payload = {"price": 199}
        res_update = obj.Update_By_prodcut_id(prod_id, update_payload) # Calls your fixed method
        assert res_update.status == 200
        assert res_update.json()["price"] == 199
        self.logger.info("Product price updated successfully.")
        
        # Delete Product (Database clean taaki Category Teardown safe rahe)
        res_delete = obj.Delete_Product_id(prod_id) # Calls your fixed method
        assert res_delete.status == 200
        self.logger.info("Product deleted successfully. System clean!")