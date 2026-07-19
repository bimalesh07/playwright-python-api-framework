# 📂 api_endpoints/Product_Client.py
from utilities.Custom_logger import LogGen

class ProductClient:
    logger = LogGen.loggen()

    def __init__(self, api_context):
        self.api_context = api_context
        
    def Create_Product(self, create_payload):
        self.logger.info("******* Creating the Product *********")
        return self.api_context.post("/api/v1/products", data=create_payload)

    def Get_all_products(self, params=None):
        self.logger.info("********** Get all the product ***********")
        return self.api_context.get("/api/v1/products", params=params)

    def Get_BY_Product_id(self, product_id):
        self.logger.info("******* Get by the Product with Id ********")
        return self.api_context.get(f"/api/v1/products/{product_id}")

    def Update_By_prodcut_id(self, product_id, update_product):
        self.logger.info("****** Update Product *******************")
        return self.api_context.put(f"/api/v1/products/{product_id}", data=update_product)

    def Delete_Product_id(self, product_id):
        self.logger.info("********* Delete The Product *************")
        return self.api_context.delete(f"/api/v1/products/{product_id}")