#reduce_mean
'''
temp = self.Y_one_hot * tf.log(self.hypothesis)
v = tf.reshape(temp,[1,-1])
self.cost = -tf.reshape(tf.matmul(v, tf.ones_like(v), transpose_b=True),[],name = 'cost')  
'''

import tensorflow as tf
sess = tf.Session()

a = tf.constant([[1,2,3],[4,5,6]],dtype=tf.float32)
b = tf.reduce_mean(a)
print("tf.reduce_sum : ",sess.run(b))

c = tf.reshape(a,[1,-1])
e = tf.cast(tf.multiply(tf.shape(a)[0], tf.shape(a)[1]), tf.float32)
d = tf.divide(tf.reshape(tf.matmul(c, tf.ones_like(c), transpose_b=True),[]), e, name='cost')
print("my reduce_sum : ", sess.run(d))