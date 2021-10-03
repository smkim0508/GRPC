import grpc
import proto_sample_pb2, proto_sample_pb2_grpc
from concurrent import futures

import os
import cv2
import numpy as np
import argparse

from datetime import datetime
from pytz import timezone
import logging

class MyAI_Model(proto_sample_pb2_grpc.AI_ModelService):
    def __init__(self,args):
        super(MyAI_Model,self).__init__()

        print('MyAI_Model Initialization Finished')
    
    def process(self,input, context):

        reply_data = proto_sample_pb2.InferenceReply()
        reply_data.class_index = 1
        reply_data.prob = 0.7
        print('Inference Finished')
        return reply_data



def opt():
    parser = argparse.ArgumentParser()

    parser.add_argument('--port', type=str, default='50051', help='Port number, default: 50051')
    parser.add_argument('--num_worker', type=int, default=8, help='The number of threads, default: 8')
    parser.add_argument('--logdir', type=str, default='./service_log', help='directory where the logging files are saved')
    return parser.parse_args()

def serve():
    args = opt()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.num_worker))
    proto_sample_pb2_grpc.add_AI_ModelServiceServicer_to_server(
        MyAI_Model(args), server) 

    server.add_insecure_port('[::]:%s' %(args.port))
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
