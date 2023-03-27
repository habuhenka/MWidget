def grid(void=0):
  if void == 90811:
    print(
"""params = {'depth'       : [4, 5, 6, 7, 8, 9, 10],
    'learning_rate' : [0.01, 0.02, 0.03, 0.04],
    'iterations'    : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

cbc_grid = cbc.grid_search(
    params,
    X, y,
    cv=3,
    partition_random_seed=42,
    calc_cv_statistics=True,
    search_by_train_test_split=True,
    refit=True,
    shuffle=True,
    stratified=None,
    train_size=0.8,
    verbose=False,
    plot=True)"""
    )

def roc(void=0):
  if void == 90811:
    print(
"""
from sklearn import metrics as mt

y_pred = cbc.predict_proba(X_test)[::,1]
fpr, tpr, _ = mt.roc_curve(y_test, y_pred)

plt.figure(figsize=[8, 6])
plt.plot(fpr, tpr, label=f"AUC={mt.roc_auc_score(y_test, y_pred)}")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()
"""
    )

def fun(void=0):
  if void == 90811:
    print(
"""
import pickle
pickle.dump(???, open('model.pkl','wb'))
from google.colab.output import eval_js
print(eval_js("google.colab.kernel.proxyPort(5000)"))
from flask import Flask, render_template, request

app = Flask(__name__,template_folder='')
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():
  input = [x for x in request.form.values()]
  final_input = [np.array(input)]
  pediction = model.predict(final_output)

  return render_template('index.html', ouitput=f'Penyakit Ginjal {pediction}')

if __name__ = "__main__":
  app.run()
"""
    )