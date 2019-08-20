# import tensorflow as tf
#
# tf.enable_eager_execution()

# A = tf.constant([[1, 2], [1, -1]])
# B = tf.constant([[1, 2, -3], [-1, 1, 2]])
# C = tf.matmul(A, B)
#
# print(C)

# tf.enable_eager_execution()
#
# x = tf.get_variable('x', shape=[1], initializer=tf.constant_initializer(3.))
# with tf.GradientTape() as tape:  # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
#     y = tf.square(x)
# y_grad = tape.gradient(y, x)  # 计算y关于x的导数
# print([y.numpy(), y_grad.numpy()])


import numpy as np

X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)


X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())
# print(X, y)

a, b = 0, 0

num_epoch = 10000
learning_rate = 1e-3
for e in range(num_epoch):
    # 手动计算损失函数关于自变量（模型参数）的梯度
    y_pred = a * X + b
    grad_a, grad_b = (y_pred - y).dot(X), (y_pred - y).sum()

    # 更新参数
    a, b = a - learning_rate * grad_a, b - learning_rate * grad_b

print(a, b)
