import numpy as np
import argparse
import os
import pickle as pkl
import numpy as np
import sys
import collections
import tensorflow as tf

a=tf.get_variable(name="sample_variable",shape=[2,3],dtype=tf.float32,initializer=tf.contrib.layers.xavier_initializer(uniform=True))
# a=tf.random.normal(shape=[2,5],dtype=tf.float32)
# a=tf.nn.softmax(a,-1)
# w=tf.constant([0.,1.],dtype=tf.float32)
# w_expand=tf.expand_dims(w,-1)
# y=w_expand*a+(1-w_expand)*1/5
# b=tf.constant([[0,5,4],[1,6,3]])
# c=tf.expand_dims(tf.one_hot(b,10),2)
# c_to_a=c*tf.to_float(a)
# d=tf.reduce_sum(c*tf.to_float(a),axis=-1)
# b_reshape=tf.reshape(b,[-1])
# a_reshape=tf.reshape(a,[6,10,5])
# c=tf.expand_dims(tf.to_float(tf.one_hot(b,10)),2)

# d=tf.reduce_sum(c*a,-1)
# d=tf.gather(a_reshape,b_reshape)

# b=tf.constant([0,2])
# c=tf.one_hot(b,3)
# d=tf.reduce_sum(c*a,-1)

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	a_print=sess.run(a)
	print('a_print',a_print)
	# print('y_print',y_print)


  # print('d_shape',sess.run(d).shape)  
  # print('d_output:',sess.run(d)[0,0,:])