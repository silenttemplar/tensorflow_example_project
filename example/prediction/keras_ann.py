import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

def create_train_data(xData, step):
    m = np.arange(len(xData) - step)

    x, y = [], []

    for i in m:
        a = xData[i:(i + step)]
        x.append(a)
    xBatch = np.reshape(np.array(x), (len(m), step, 1))

    for i in m + 1:
        a = xData[i:(i + step)]
        y.append(a[-1])
    yBatch = np.reshape(np.array(y), (len(m), 1))

    return xBatch, yBatch

def result_visualization(history, lastData, estimate):
    # Loss history를 그린다
    plt.figure(figsize=(8, 4))
    plt.plot(history.history['loss'], color='red')
    plt.title("Loss History")
    plt.xlabel("epoch")
    plt.ylabel("loss")
    plt.show()

    # 원 시계열과 예측된 시계열을 그린다
    ax1 = np.arange(1, len(lastData) + 1)
    ax2 = np.arange(len(lastData), len(lastData) + len(estimate))
    plt.figure(figsize=(8, 4))
    plt.plot(ax1, lastData, 'b-o', color='blue', markersize=3, label='Time series', linewidth=1)
    plt.plot(ax2, estimate, 'b-o', color='red', markersize=3, label='Estimate')
    plt.axvline(x=ax1[-1], linestyle='dashed', linewidth=1)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # time series data (with noisy)
    data = np.sin(2 * np.pi * 0.03 * np.arange(1001)) + np.random.random(1001)

    nInput = 1
    nOutput = 1
    nStep = 20
    nHidden = 50

    # create train data
    x, y = create_train_data(data, nStep)
    print('x.shape: {}, y.shape: {}'.format(x.shape, y.shape))

    # define model
    LR = 0.001
    loss_object = MeanSquaredError()
    optimizers = Adam(learning_rate=LR)

    xInput = Input(batch_shape=(None, nStep, nInput))
    xDense1 = Dense(units=nHidden, activation='relu')(xInput)
    xDense2 = Dense(units=nHidden, activation='relu')(xDense1)
    xOutput = Dense(nOutput)(xDense2)
    model = Model(xInput, xOutput)

    model.compile(loss=loss_object, optimizer=optimizers)
    model.summary()

    # training
    EPOCHS = 100
    BATCH_SIZE = 10

    history = model.fit(x, y,
                        epochs=EPOCHS,
                        batch_size=BATCH_SIZE,
                        shuffle=True)

    # 향후 20 기간 데이터를 예측한다. 향후 1 기간을 예측하고, 예측값을 다시 입력하여 2 기간을 예측한다.
    # 이런 방식으로 20 기간까지 예측한다.
    nFuture = 20
    if len(data) > 100:
        lastData = np.copy(data[-100:])  # 원 데이터의 마지막 100개만 그려본다
    else:
        lastData = np.copy(data)

    dx = np.copy(lastData)
    estimate = [dx[-1]]
    for i in range(nFuture):
        # 마지막 nStep 만큼 입력데이로 다음 값을 예측한다
        px = dx[-nStep:].reshape(1, nStep, 1)

        # 다음 값을 예측한다.
        yHat = model.predict(px)[0][0]

        # 예측값을 저장해 둔다
        estimate.append(yHat)

        # 이전 예측값을 포함하여 또 다음 값을 예측하기위해 예측한 값을 저장해 둔다
        dx = np.insert(dx, len(dx), yHat)

    result_visualization(history, lastData, estimate)
