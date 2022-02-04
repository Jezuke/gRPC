import logging
import sys
from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc

if __name__=='__main__':
    channel = grpc.insecure_channel('localhost:4000')
    stub = todo_pb2_grpc.TodoStub(channel)
    try:
        todo_item = stub.createTodo(todo_pb2.TodoItem(id=-1,text=sys.argv[1]))
        print('Created task #{}: {}'.format(todo_item.id, todo_item.text))
        print('\n\n')
        print('### Task List ###:\n')
        task_list = stub.readTodos(todo_pb2.no_param())
        print(task_list)
    except Exception as e:
        print(e)
        print('Request Failed...')

