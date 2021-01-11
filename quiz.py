import pandas as pd
import configparser
import sys
import random

#設定ファイル読み込み
inifile="config/quiz.ini"
quizfilename=""
try:
    ini = configparser.ConfigParser()
    ini.read(inifile, 'UTF-8')
    quizfilename=ini['Filename']['QUIZFILE']

except Exception as e:
    print("エラー：設定ファイル({0})が読み込めません".format(inifile))
    print(e)
    sys.exit()



print(quizfilename)

#問題csv読み込み
df=""
try:
    df=pd.read_csv('csv/'+quizfilename)
except Exception as e:
    print("エラー：問題csv({0})の読み込み時にエラーが発生しました".format(quizfilename))
    print(e)
    sys.exit()

print(df.shape)

#全問題数
total=df.shape[0]
#ランダムに1個選ぶ
quiz_id=random.randrange(total)
#その問題を(リスト形式で)取ってくる
quiz=df.iloc[quiz_id,:].values.tolist()

print(quiz)
quiz_num,question,answer,correct_num,incorrect_num=*quiz


