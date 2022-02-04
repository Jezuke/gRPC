import logging
from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc

class TodoServicer(todo_pb2_grpc.TodoServicer):
    """Provides methods that implement functionality of TodoServicer."""
    def __init__(self):
        self.todos = []

    def createTodo(self, request, context):
        todoItem = todo_pb2.TodoItem(id=len(self.todos)+1, text=request.text)
        self.todos.append(todoItem)
        return todoItem
    
    def readTodos(self, request, context):
        taskList = todo_pb2.TodoItems()
        taskList.items.extend(self.todos)
        print(taskList)
        return taskList

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)
    server.add_insecure_port('[::]:4000')
    server.start()
    server.wait_for_termination()

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting Todo Server...')
    serve()
