# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:23:52 2018

@author: hanquanjie
"""

import numpy as np  
import struct  
       
def loadImageSet(filename):  
    print "load image set",filename  
    binfile= open(filename, 'rb')  
    buffers = binfile.read()  
     
    head = struct.unpack_from('>IIII' , buffers ,0)  
    print "head,",head  
     
    offset = struct.calcsize('>IIII')  
    imgNum = head[1]  
    width = head[2]  
    height = head[3]  
    #[60000]*28*28  
    bits = imgNum * width * height  
    bitsString = '>' + str(bits) + 'B' #like '>47040000B'  
       
    imgs = struct.unpack_from(bitsString,buffers,offset)  
       
    binfile.close()  
    imgs = np.reshape(imgs,[imgNum,width*height])  
    print "load imgs finished"  
    return imgs  
       
def loadLabelSet(filename):  
       
    print "load label set",filename  
    binfile = open(filename, 'rb')  
    buffers = binfile.read()  
       
    head = struct.unpack_from('>II' , buffers ,0)  
    print "head,",head  
    imgNum=head[1]  
       
    offset = struct.calcsize('>II')  
    numString = '>'+str(imgNum)+"B"  
    labels = struct.unpack_from(numString , buffers , offset)  
    binfile.close()  
    labels = np.reshape(labels,[imgNum,1])  
       
    print 'load label finished'  
    return labels  
       
if __name__=="__main__":  
       
    x_train= loadImageSet("/home/hanquanjie/Datasets/mnist/train-images.idx3-ubyte")  
    y_train= loadLabelSet("/home/hanquanjie/Datasets/mnist/train-labels.idx1-ubyte") 
    x_test= loadImageSet("/home/hanquanjie/Datasets/mnist/t10k-images.idx3-ubyte")  
    y_test= loadLabelSet("/home/hanquanjie/Datasets/mnist/t10k-labels.idx1-ubyte") 
