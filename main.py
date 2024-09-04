from flask import Flask, render_template, request

app = Flask(__name__)

# Kullanıcı puanı ve en yüksek puan için veri yapısı
scores = {"user": 0, "high_score": 0}

# Doğru cevaplar
correct_answers = {
    "question1": "OpenCV",
    "question2": "NLTK",
    "question3": "Boyut azaltma (Dimensionality Reduction)",
    "question4": "TensorFlow"
}

@app.route('/')
def home():
    # Ana sayfa: sınav formu ve en yüksek puanı gösterir
    return render_template('index.html', high_score=scores["high_score"])

@app.route('/submit', methods=['POST'])
def submit():
    # Kullanıcının cevaplarını al
    user_answers = {
        "question1": request.form.get('question1'),
        "question2": request.form.get('question2'),
        "question3": request.form.get('question3'),
        "question4": request.form.get('question4')
    }

    # Kullanıcının puanını hesapla
    user_score = 0
    for question, answer in user_answers.items():
        if answer == correct_answers.get(question):
            user_score += 1

    # En yüksek puanı güncelle
    if user_score > scores["high_score"]:
        scores["high_score"] = user_score

    return render_template('result.html', score=user_score, high_score=scores["high_score"])

if __name__ == '__main__':
    # Uygulama başlatılır
    app.run(debug=True)
