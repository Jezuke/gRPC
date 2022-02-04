# Why gRPC was invented?
* Communication protocols such as HTTP need a client library built for that specific language unless you're using a browser.
* So when developing a python/java/<insert-language-here>, you need to install a client libray (i.e. `import axios`)

# gRPC
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
