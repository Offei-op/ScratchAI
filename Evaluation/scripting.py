import numpy as np
import pandas as pd


def evaluateCh1ex1(x,y):
    true_x = np.linspace(-15,15,150)
    if  np.array_equal(x,true_x): 
        print("X -> ✅ CORRECT !")
    else:
        print("X -> ❌ WRONG")
    if np.array_equal(y,np.cos(true_x)):
        print("Y -> ✅ CORRECT !")
    else:
        print("Y -> ❌ WRONG")
        
def evaluateCh1ex2(df):
    true_df = pd.DataFrame({'Item':['Laptop','Webcam','Keyboard'],'Price':['10000','450','120']})
    if true_df.equals(df):
        print("✅ CORRECT!")
    else:
        print("❌ WRONG")