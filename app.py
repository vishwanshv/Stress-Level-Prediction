import numpy as np
import pickle
import streamlit as st  


model = pickle.load(open('model.pkl','rb'))

def stresslevel_prediction(input_data):
    
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "Stress Level: LOW"
    elif(prediction[0]==1):
        return "Stress Level: MEDIUM"
    else:
        return "Stress Level: HIGH"
    
def main():
    
    st.base="dark"
    st.primaryColor="yellow"
    st.image('nathan-dumlao-LPRrEJU2GbQ-unsplash.png')
    st.title('STRESS LEVEL PREDICTION')
    
    Humidity = st.text_input('Humidity Value')
    Temperature = st.text_input('Body Temperature')
    Step_count = st.text_input('Number of Steps')
    
    gender = ['<Select>','Male', 'Female']
    Gender_choice = st.selectbox('Gender', gender)
    

    Age = st.text_input('Age')
    
    
    heart = st.text_input('Heart-rate')

    Breathingrate = st.text_input('Breathing-rate')
    Emotion = ['<Neutral>','Happy', 'Sad','Anger','Disgust','Fear','Joy']
    emotion_choice = st.selectbox('Emotion', Emotion)
    
    #,Gender,Age,Heartrate
    diagnosis = ''
    
    if st.button('PREDICT'):
        diagnosis = stresslevel_prediction([Humidity, Temperature, Step_count])
        
    st.success(diagnosis)

    
if __name__=='__main__':
    main()