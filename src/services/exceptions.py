class TaskNotFoundException(Exception):
    
    def __init__(self, message='Task not found'):
        self.message = message