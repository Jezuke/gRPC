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
    
    '''
    NOTE: when assigning to repeatable Message field types declare Message top Message object first (ie. todo_pb2.TodoItems()).
    This allows you to reference the fields inside when adding to them because extend() and append() return None and act on the params
    they're passed in.
    '''
    def readTodos(self, request, context):
        taskList = todo_pb2.TodoItems()
        taskList.items.extend(self.todos)
        return taskList
    # TODO: implement readTodos but with a stream which is better.

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
