import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
#tf.config.experimental.list_physical_devices('GPU')


sudo python3 example/train_supervised_cnn.py    --metric acc     --dataset wiki80    --batch_size 160    --lr 0.1     --weight_decay 1e-5    --max_epoch 3     --max_length 128        --encoder pcnn
