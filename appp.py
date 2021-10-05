#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask,redirect,render_template,request
import pickle


# In[19]:


model1 = pickle.load(open('mod.pkl','rb'))


# In[20]:


model2 = pickle.load(open('model.pkl','rb'))


# In[29]:


app = Flask(__name__)


# In[30]:


@app.route('/')
def home():
    return render_template('okk.html')


# In[31]:


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        int_feature = request.form['Feedback']
        input_data = [int_feature]
        input_data = model1.transform(input_data).toarray()
        input_pred = model2.predict(input_data)
    res = ""
    if input_pred == 1:
        res = "Feedback is Positive"
    else:
        res = "Feedback is Negative"
    return render_template('okk.html',result=res)


# In[32]:


if __name__ == '__main__':
    app.run(debug=True)

