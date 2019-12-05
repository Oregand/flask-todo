from models import ToDoModel

class ToDoService:
    def __inti__(self):
        self.model = ToDoModel()
    
    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.mode.list_items()
        return response
        