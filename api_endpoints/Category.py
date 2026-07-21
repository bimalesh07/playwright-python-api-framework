from utilities.Custom_logger import LogGen


class CategoryClient:
    logger = LogGen.loggen()

    def __init__(self, api_context):
        self.api_context = api_context


    def create_category(self, payload):
        self.logger.info(" Creating a new Product Category")
        return self.api_context.post("/api/v1/categories",data=payload)

    def get_category(self, category_id):
        self.logger.info(f"Fectching category details for id{category_id}")
        return self.api_context.get(f"/api/v1/categories/{category_id}")

    def update_category(self, category_id, payload):
        self.logger.info(f"Updating category Id: {category_id}",)
        return self.api_context.put(f"/api/v1/categories/{category_id}", data=payload)

    def delete_category(self, category_id):
        self.logger.info(f"Deleting category ID: {category_id}")
        return self.api_context.delete(f"/api/v1/categories/{category_id}")


    def get_category_by_slug(self, slug_name):
        self.logger.info(f"Fetching category via slug name: {slug_name}")
        return self.api_context.get(f"/api/v1/categories/slug/{slug_name}")

    def get_products_by_category(self, category_id):
        self.logger.info(f"Fetching all products under category ID: {category_id}")
        return self.api_context.get(f"/api/v1/categories/{category_id}/products")
    
        