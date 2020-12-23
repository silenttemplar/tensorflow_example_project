import os

'''
[Tensorflow2 강의] 29강 Serial Training 강의 예제샘플
'''

learning_rates = [0.01, 0.03, 0.1, 0.3]
n_exp = len(learning_rates)

for exp_cnt, exp_idx in enumerate(range(0, n_exp)):
    learning_rate = learning_rates[exp_cnt]

    command_template = 'python3 ../serial_training_LeNet5.py ' \
                       + '-l ' + str(learning_rate) \
                       + ' -c ' + str(exp_idx)
    print(command_template)
    os.system(command_template)

