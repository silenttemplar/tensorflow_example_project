import numpy as np
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam

from example.prediction.keras_ann import create_train_data, result_visualization

if __name__ == '__main__':
    # time series data (with noisy)
    data = np.sin(2 * np.pi * 0.03 * np.arange(1001)) + np.random.random(1001)

    # define data
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

    xLstm = LSTM(units=nHidden)(xInput)
    #xLstm = Bidirectional(LSTM(units=nHidden))(xInput)

    xOutput = Dense(units=nOutput)(xLstm)
    model = Model(xInput, xOutput)

    #model.summary()
    model.compile(loss=loss_object, optimizer=optimizers)

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