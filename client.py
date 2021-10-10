import grpc
import proto_sample_pb2, proto_sample_pb2_grpc

import os 
import glob
import cv2
import argparse

def request(ip, port, frame):

    print('request: client -> server : {}{}'.format(ip,port))
    with grpc.insecure_channel(ip+port) as channel:
        stub = proto_sample_pb2_grpc.AI_ModelServiceStub(channel)
        response = stub.process(
            proto_sample_pb2.InferenceRequest(
                img_bytes=bytes(frame),
                width=frame.shape[1],
                height=frame.shape[0],
                channel=frame.shape[2]
            )
        )
        return response

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='50051', help='port number (default: 50051)')
    parser.add_argument('--ip', type=str, default='localhost:', help='ip adress (default: localhost:)')
    return parser.parse_args()
    
def main():
    args = opt()

    image_list = ['images.jpeg', 'images.png']

    for idx, file_name in enumerate(image_list):
        img = cv2.imread(file_name)

        response = request(args.ip, args.port, img)

        print(response.class_index)
        print(response.prob)


if __name__ == '__main__':
    main()