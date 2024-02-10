class EntityNotFound(Exception):
    def __init__(self):
        super().__init__("Entity not found")
