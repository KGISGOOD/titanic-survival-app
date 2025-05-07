from flask import Flask, render_template_string, request
import pandas as pd
import pickle

# 初始化 Flask app
app = Flask(__name__)

# 載入模型
with open('./model.pkl', 'rb') as f:
    model = pickle.load(f)

# HTML模板
html_template = '''
<!doctype html>
<html lang="zh-tw">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titanic 生存預測</title>
    <style>
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: url('https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg') no-repeat center center fixed;
            background-size: cover;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 30px 40px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4);
            width: 100%;
            max-width: 400px;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-top: 15px;
        }
        input, select {
            padding: 8px;
            margin-top: 5px;
            border: none;
            border-radius: 5px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            padding: 10px;
            margin-top: 20px;
            background-color: #ffd700;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 100%;
        }
        button:hover {
            background-color: #ffcc00;
        }
        .result {
            text-align: center;
            font-size: 1.2em;
            margin-top: 20px;
        }
        @media (max-width: 480px) {
            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>⛵ Titanic 生存預測</h2>
        <form method="POST">
            <label>年齡：</label>
            <input type="number" name="age" required min="0">
            
            <label>性別：</label>
            <select name="sex">
                <option value="male">男性</option>
                <option value="female">女性</option>
            </select>

            <label>旁系血親人數 (兄弟姐妹或配偶數)：</label>
            <input type="number" name="sibsp" required min="0">

            <label>直系血親人數 (父母或子女數)：</label>
            <input type="number" name="parch" required min="0">

            <button type="submit">預測存活</button>
        </form>
        {% if result %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # 取得使用者輸入
        age = float(request.form['age'])
        sex = request.form['sex']
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])

        # 驗證輸入是否小於 0
        if age < 0 or sibsp < 0 or parch < 0:
            result = "❗ 請輸入非負數值。"
            return render_template_string(html_template, result=result)

        # 性別轉換成模型需要的格式 (通常: female=0, male=1)
        #sex_female = True if sex == 'female' else False
        #sex_male = True if sex == 'male' else False
        # 模型預測（依照你的模型需求可能需要修改）
        #input_features = np.array([[age, sibsp, parch, sex_female, sex_male]])
        df = pd.DataFrame({
            'Age': [age],
            'Sex': [sex],
            'SibSp': [sibsp],
            'Parch': [parch]
        })
        input_features = pd.get_dummies(df)

        if 'Sex_male' in input_features.columns:
            input_features['Sex_female'] = False
        else:
            input_features['Sex_male'] = False

        input_features = input_features[['Age','SibSp','Parch','Sex_female','Sex_male']]
        print(input_features)
        prediction = model.predict(input_features)
        print(prediction)
        
        # 轉換預測結果
        result = "🎉 存活" if prediction[0] == 1 else "😢 無法存活"

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)