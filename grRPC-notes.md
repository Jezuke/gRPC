# Why gRPC was invented?
* Communication protocols such as HTTP need a client library built for that specific language unless you're using a browser.
* So when developing a python/java/<insert-language-here>, you need to install a client libray (i.e. `import axios`)

# gRPC

Installing: `python -m pip install grpcio`
* Client Libary: One library for popular languages
* Protocol: HTTP/2
* Message Format: Protocol buffers

versus something like...

__Axios__ which is JavaScript specific HTTP client for Node.js or __urllib__ for Python.

# gRPC modes
* Unary RPC - client requests server => server responds
* Server streaming RPC - client requests once to server => multiple responses from server/continous stream of data (ex. Streaming a video)
* Client streaming RPC -  client sends continous data to server (ex. IoT data sending continous stream telemetry to server)
* Bidirectional streaming RPC - both client/server sending continous streams of data (ex. online gaming/chatting)

# Steps to setting up server/client

1. Write up proto establishing contract
2. Run `python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto`
    - Make sure the grpcio-tools are installed: `pip install grpcio-tools`
    - This generates a ...pb2.py and ...pb2_grpc.py
    - ...pb2.py contains your descriptors which allow you to invoke your Message types.
    - ...pb2_grpc.py contains the servicer which is what allow you to invoke the functions from the server defined by the proto
3. Fill in server functions and client functions. See Todo example in *src/*

Notes are written in comments.

## Stream vs. Non-stream type
Non-stream requires all the data be sent all at once in a request.

### Iterables vs. Iterators vs. Generators

**Iterator:**

```
for x in myList:
    ...loop body...
```

1. Gets an __iterator__ for myList:
    - Call `iter(myList)` which returns an object with a `next()` (or `__next__() in py3) method. (Sort of like a linked list?)
2.  Uses that __iterator__ to loop over items by calling the `next()` method on the iterator. The return value from `next()` is assigned to `x` and the loop body is executed. If an exception *StopIteration* is raised from within `next()`, it means there are no more values in the iterator and the loop is exited.

*myList* here is the **iterable** because it implements the iterator protocol and can be 'iterated' over.

So that's the iterator protocol, many objects implemente this protocol:

1. Built-in lists, dictionaries, tuples, sets, files.
2. User-defined classes that implement __iter__()
3. Generators

Note that a for loop doesn't know what kind of object it's dealing with - it just follows the iterator protocol, and is happy to get item after item as it calls next(). Built-in lists return their items one by one, dictionaries return the keys one by one, files return the lines one by one, etc. And generators return... well that's where yield comes in:

```
def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item
```

If that was a return statement it would exit once it hits the first return. Instead none of the yield values get returned. The function just returns a generator object and goes into a suspended state waiting for an iterator to iterate over the generator object. When the `for` loop tries to loop over the generator object, the function resumes from its suspended state at the next line after the yield it returned from, and continues until the function exits and the generator raises a *StopIteration* and the loop exits.