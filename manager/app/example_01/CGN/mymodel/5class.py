#!/usr/bin/python
#coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import os
import urllib
import random

tf.logging.set_verbosity(tf.logging.ERROR)              #日志级别设置成 ERROR，避免干扰
np.set_printoptions(threshold='nan')                    #打印内容不限制长度

QUADRANT_TRAINING = "CGN_training.csv"
QUADRANT_TEST = "CGN_test.csv"

def gen_data(file,count):
        with open(file,"w") as f:
                #首行，写入数据集的组数和特征的数量
                f.write("%d,2\n" % count)

                #产生一个随机坐标(x1,x2)
                for i in range(1,count):
                        x1 = random.uniform(-10, 40)
                        x2 = random.uniform(0, 1)


                        #获得action

                        if x1 <= 30 and x2 <= 0.6:
                                action = 0
                        elif x1 > 30 and x2 <= 0.6:
                                action = 1
                        elif x1 <= 30 and x2 > 0.6:
                                action = 2
                        elif x1 > 30 and x2 > 0.6:
                                action = 3

                        f.write("%.1f,%.2f,%d\n" % (x1,x2,action))

def main():
        # 生成训练集和测试集
        if not os.path.exists(QUADRANT_TRAINING):
                gen_data(QUADRANT_TRAINING,7000)

        if not os.path.exists(QUADRANT_TEST):
                gen_data(QUADRANT_TEST,3000)

        # 加载数据
        training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=QUADRANT_TRAINING,
               target_dtype=np.int, features_dtype=np.float32)

        test_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=QUADRANT_TEST,
                target_dtype=np.int, features_dtype=np.float32)

        # 2 维数据
        feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2)]

        # 改造一个分类器
        classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                                                                hidden_units=[10, 20, 10],
                                                                                                n_classes=4,
                                                                                                model_dir="mymodel")
        # 构造训练输入函数
        def get_train_inputs():
                x = tf.constant(training_set.data)
                y = tf.constant(training_set.target)
                return x, y

        # 训练模型
        classifier.fit(input_fn=get_train_inputs, steps=2000)

        # 构造测试输入函数
        def get_test_inputs():
                x = tf.constant(test_set.data)
                y = tf.constant(test_set.target)

                return x, y

        # 评估准确度
        print(classifier.evaluate(input_fn=get_test_inputs, steps=1))
        accuracy_score = classifier.evaluate(input_fn=get_test_inputs, steps=1)["accuracy"]
        print("Test Accuracy: {0:f}\n".format(accuracy_score))

        # 传入数据，对其进行分类
        def new_samples():
                return np.array([[34,0.7]], dtype=np.float32)

        predictions = list(classifier.predict(input_fn=new_samples))

        def tip(pre):
                for i in pre:
                        if i == 0:
                                print("Turn off the air condition")
                        elif i == 1:
                                print("Turn on the refrigeration function of air conditoning")
                        elif i == 2:
                                print("Turn on the dehumidification function of air conditioning")
                        elif i == 3:
                                print("Turn on the refrigeration function and dehumidification function of air conditioning")

        print("New Samples, Class Predictions:    {}\n".format(predictions))
        tip(predictions)
if __name__ == "__main__":
        main()


exit(0)
