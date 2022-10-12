import pickle


from flask import Flask, request

# Загружаем модель в память
with open('./model_gbr.pkl', 'rb') as model_pkl:
   cbc = pickle.load(model_pkl)

app = Flask(__name__)

@app.route('/predict')
def predict():
    dict_dataset = {'Cleveland': 1, 'Hungary': 2, 'VA Long Beach': 3, 'Switzerland': 4}
    dict_cp = {'typical angina': 1, 'asymptomatic': 2, 'non-anginal': 3, 'atypical angina': 4}
    dict_restecg = {'lv hypertrophy': 1, 'normal': 2, 'st-t abnormality': 3}
    dict_bool = {False: 0, True: 1}

    def replace_feature(feature, dict_repl):
        if feature in dict_repl:
            return dict_repl[feature]
        else:
            return 0

    age = int(request.args.get('age'))
    dataset = replace_feature(request.args.get('dataset'), dict_dataset)
    cp = replace_feature(request.args.get('cp'), dict_cp)
    trestbps = float(request.args.get('trestbps'))
    chol = float(request.args.get('chol'))
    restecg = replace_feature(request.args.get('restecg'), dict_restecg)
    thalch = float(request.args.get('thalch'))
    exang = replace_feature(bool(request.args.get('exang')), dict_bool)
    oldpeak = float(request.args.get('oldpeak'))

    unseen = [age, dataset, cp, trestbps, chol, restecg, thalch, exang, oldpeak]
    result = cbc.predict([unseen])

    return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)

if __name__ == '__main__':
    app.run()