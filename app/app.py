from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.widgets import TextArea


from flask import Flask, render_template, flash

from sklearn.externals import joblib

from string import punctuation

app = Flask(__name__)

model = joblib.load('../best_model/svc.pkl')
trained_vec = joblib.load('../best_model/vect.pkl')


@app.route('/', methods=['GET', 'POST'])
def sentiment():
    form = SentimentForm()
    if form.validate_on_submit():
        text = form.body.data
        result = process_input(text)
        flash('This Review seems '.format(result))
    else:
        result = None
    return render_template('app.html', form=form, result=result)


def process_input(review):
    """

    Parameters
    ----------
    review

    Returns
    -------

    """
    review = [i.lower() for i in review if i not in punctuation + ' ']

    review_vec = trained_vec.transform(review)

    prediction = model.predict(review_vec)

    if prediction == 1:
        result = 'positive'
    elif prediction == 0:
        result = 'neutral'
    else:
        result = 'negative'


    return result



class SentimentForm(Form):
    body = StringField('Text', widget=TextArea())