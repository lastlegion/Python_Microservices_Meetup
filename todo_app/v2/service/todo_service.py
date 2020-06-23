from typing import Dict


class ServiceLayerError(Exception):
    pass

class TodoService:
    def __init__(self, repository):
        self.repository = repository

    def add_todo(self, description: str, status: str) -> Dict:
        response = None
        try:
            response = self.repository.add_todo(description, status)
        except Exception:
            raise ServiceLayerError()
        return response

    def update_todo(self, id_: int, description: str, status: str):
        response = None
        try:
            response = self.repository.update_todo(id_=id_,
                                                   description=description,
                                                   status=status)
        except Exception:
            raise ServiceLayerError()
        return response

    def list_todo(self):
        r = None
        try:
            r = self.repository.get_all_todos()
        except Exception:
            raise ServiceLayerError()
        response = []
        for row in r:
            response.append({
                'id': row[0],
                'description': row[1],
                'status': row[2]
            })
        return response

    def delete_todo(self, id_: int):
        try:
            r = self.repository.delete_todo(id_=id_)
        except Exception:
            raise ServiceLayerError()
        return {}

