import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_locatoin = data["le_locatoin"]
le_furnishing = data["le_furnishing"]

def show_predict_page():
    st.title("Kuala Lumpur Properties Prediction Model")

    st.write("""### We need some information to predict the price""")

    location = ('ampang','ampang hilir','bandar damai perdana','bandar menjalara','bangsar',
    'bangsar south','batu caves','brickfields','bukit bintang','bukit jalil','bukit tunku (kenny hills)',
    'cheras','city centre','country heights damansara','damansara heights','desa pandan','desa parkcity','desa petaling',
    'dutamas','jalan ipoh','jalan klang lama (old klang road)','jalan kuching','jalan sultan ismail','kepong',
    'keramat','kl city','kl eco city','kl sentral','klcc','kuchai lama','mont kiara','oug','pandan perdana','pantai')

    furnishing = ("Partly Furnished","Fully Furnished","Unfurnished",)

    location = st.selectbox(" Location", location)
    furnishing = st.selectbox(" Furnishing", furnishing)

    rooms = ('1.0','2.0','3.0','4.0','5.0','6.0','0.7','0.8','0.9')
    bathrooms = ('1.0','2.0','3.0','4.0','5.0','6.0','0.7','0.8','0.9')
    carpark = ('1.0','2.0','3.0','4.0','5.0','6.0')




    rooms = st.selectbox(" Rooms Numbers", rooms)

    bathrooms = st.selectbox(" Bathrooms Numbers", bathrooms)

    carpark = st.selectbox(" Car Parks", carpark)

    size = st.slider("Size (sq. ft.)", 700.0, 10000.0, 700.0)

    ok = st.button("Predict Price")
    if ok:
        x_test = np.array([[location, furnishing, rooms, bathrooms, carpark, size ]])
        x_test[:, 0] = le_locatoin.transform(x_test[:,0])
        x_test[:, 1] = le_furnishing.transform(x_test[:,1])
        x_test = x_test.astype(float)


        price = regressor.predict(x_test)
        st.subheader(f"The estimated price is RM {price[0]:.2f}")
