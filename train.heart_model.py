import pandas as pd
import tensorflow as tf 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
#read csv file
df=pd.read_csv("heart.csv")
x=df.drop('target',axis=1)
y=df['target']
scalar=StandardScaler()
x_scaled=scalar.fit_transform(x)
joblib.dump(scalar,"heart_scalar.pkl")
x_train,x_test,y_train,y_test=train_test_split(
    x_scaled,y,test_size=0.2
)
model=tf.keras.Sequential([
    tf.keras.layers.Dense(32,activation='relu', input_shape=(x.shape[1],)),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=25,batch_size=16)
model.save("heart_model.h5")