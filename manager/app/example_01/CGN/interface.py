import tensorflow as tf
import numpy as np
import sys
import hfv
# 重新定义一个DNNClassifier的结构才能恢复原有的DNN模型，这也和使用tensorflow直接搭建的神经网络的保存和恢复操作一致。

feature_columns = [tf.contrib.layers.real_valued_column("", dimension=2)]
new_classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[10, 20, 10],
                                                n_classes=4,
                                                model_dir=
                                                "mymodel")

# 从外部传入数据，并且将其返回成所需格式

def new_samples():
    (x,y) = hfv.dht11_temp_humi('dht11','docker')
    return np.array([[x,y]], dtype=np.float32)


def tip(pre):
    for i in pre:
        if i == 0:
            print("Turn off the air condition")
            print(print(hfv.switch('switch','host')))
        elif i == 1:
            print("Turn on the refrigeration function of air conditoning")
        elif i == 2:
            print("Turn on the dehumidification function of air conditioning")
            print(print(hfv.switch('switch','host')))
        elif i == 3:
            print("Turn on the refrigeration function and dehumidification function of air conditioning")

#此处使用的new_samples不能加括号，因为此处是需要input_fn这个参数，输入是一个函数
#如果加括号的话，则输入的是一个返回值
predictions = list(new_classifier.predict(input_fn=new_samples))
print("New Samples, Class Predictions:    {}\n".format(predictions))
tip(predictions)
