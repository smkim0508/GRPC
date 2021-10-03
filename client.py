import grpc
import proto_sample_pb2, proto_sample_pb2_grpc

import os 
import glob
import cv2
import argparse

def opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, default='50051', help='port number (default: 50051)')
    parser.add_argument('--ip', type=str, default='localhost:', help='ip adress (default: localhost:)')
    return parser.parse_args()
    
def main():
    args = opt()

if __name__ == '__main__':
    main()