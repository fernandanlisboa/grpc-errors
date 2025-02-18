import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.HelloServiceStub(channel)
    # ideally, you should have try catch block here too
    name = str(input("Digite seu nome: "))
    # response = stub.SayHello(hello_pb2.HelloReq(Name=name))
    # print(response.Result)
    age = int(input("Digite sua idade: "))

    try:
        response = stub.SayHelloStrict(hello_pb2.HelloReq(
            Name=name))
        response = stub.AgeHello(hello_pb2.HelloAge(Age=age))
    except grpc.RpcError as e:
        # ouch!
        # lets print the gRPC error message
        # which is "Length of `Name` cannot be more than 10 characters"
        print(e.details())
        # lets access the error code, which is `INVALID_ARGUMENT`
        # `type` of `status_code` is `grpc.StatusCode`
        status_code = e.code()
        # should print `INVALID_ARGUMENT`
        print(status_code.name)
        # should print `(3, 'invalid argument')`
        print(status_code.value)
        # want to do some specific action based on the error?
        if grpc.StatusCode.INVALID_ARGUMENT == status_code:
            # do your stuff here
            pass
        if grpc.StatusCode.OUT_OF_RANGE == status_code:
            pass
    else:
        print(response.Result)


if __name__ == '__main__':
    run()
