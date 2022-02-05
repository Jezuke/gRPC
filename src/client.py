import logging
import sys
from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc

# Non-stream function
def printTodos(stub):
    task_list = stub.readTodos(todo_pb2.no_param())
    print('### Task List ###:\n')
    for task in task_list.items:
        print('{}. {}\n'.format(task.id, task.text))

# Stream function
def printTodosStream(stub):
    print('### Task List Streamed ###:\n')
    task_list = stub.readTodosStream(todo_pb2.no_param()) # Returns a MultiThreadedRendezvous object (a Generator)
    print('{}'.format(list(task_list)))
    for task in task_list:
        print(task.text)

if __name__=='__main__':
    channel = grpc.insecure_channel('localhost:4000')
    stub = todo_pb2_grpc.TodoStub(channel)
    try:
        todo_item = stub.createTodo(todo_pb2.TodoItem(id=-1,text=sys.argv[1]))
        print('Created task #{}: {}'.format(todo_item.id, todo_item.text))
        printTodos(stub)
        printTodosStream(stub) 
    except Exception as e:
        print(e)
        print('Request Failed...')

