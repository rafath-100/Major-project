import math
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# lottie_cricket = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_cflyho6s.json")

lottie_cricket = load_lottiefile("cricket.json")
st_lottie(
    lottie_cricket,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height="25%",
    width="25%",
    key=None
)

# st.write(pd.read_excel('dls.xlsx'))
df = pd.read_excel('dls.xlsx')

# df=df.astype("str")
# df["Wickets Lost"]=df["Wickets Lost"].astype(int)
# df["Overs Left"]=df["Overs Left"].astype(int)

# df.head()
# df.head()
# st.title('DLS Method')

activities = ["1st Innings", "2nd Innings",
              "Classifier", "About", "DLS Excel Sheet(For Resources Available)"]
# list = ["Classifier", "About", "DLS Method"]

st.sidebar.title("# MENU #")

choice = st.sidebar.selectbox("Select anyone", activities)
# select_item = st.sidebar.selectbox("Select from the list", list)


st.sidebar.write("----------------------------")
st.sidebar.title('**CONTRIBUTORS**')
st.sidebar.write('''
                    -------------------------------

                    **Rayees Ahmed Taj**
                    1604-18-733-091

                    **Syed Amir Ahmed Razvi**
                    1604-18-733-092

                    **Mir Rafath Ali**
                    1604-18-733-100

                    -------------------------------
            ''')


# def pred2rain2(overstplay, oversplayed, overslost, overslost_secondtime, wicketslost, t1s, t2s, overs_start2_suspension, overs_end2_suspension):
# 	r1 = df[0][51-overstplay]*100
#     g50 = 245
#    	a = (51-(overstplay-oversplayed-overslost_secondtime))
#     r2a = df[wicklost][a]*100
#     b = a+overslost
#     r2b = df[wicklost][b]*100
# 	if overslost == 0:
#         r2 = df[0][51-overstplay]*100
#     else:
#         r2 = 100-(r2a-r2b)
#     if r1 > r2:
#         rt2s = round(t1s*(r2/r1))
#     elif r2 > r1:
#         t2s = round(t1s+g50*(r2-r1)/100)+1
#     else:
#         rt2s = t1s
#     st.write("Required runs are:{}".format(rt2s-t2s))
#     st.write("from {} overs".format(overstplay-oversplayed-overslost))
#     # st.write(rt2s-t2s)
#     return rt2s


# rain interruption in 1st innings


def pred1(overstplay, oversplayed, overslost, wicklost, overstplaybyt2, t1s):
    a = (51-(overstplay-oversplayed))
    g50 = 245
    r1a = df[wicklost][a]*100
    b = a+overslost
    r1b = df[wicklost][b]*100
    # r1=r1a-r1b
    if overslost == 0:
        r1 = df[0][51-overstplay]*100
    else:
        r1 = 100-(r1a-r1b)
    r2 = df[0][51-(overstplaybyt2)]*100
    if r1 > r2:
        t2s = round(t1s*(r2/r1))
    elif r2 > r1:
        t2s = round(t1s+g50*(r2-r1)/100)+1
    else:
        t2s = t1s
    return t2s

# rain interruption in 2nd innings


def pred2(overstplay, oversplayed, overslost, wicklost, t1s, t2s):
    r1 = df[0][51-overstplay]*100
    g50 = 245
    a = (51-(overstplay-oversplayed))
    r2a = df[wicklost][a]*100
    b = a+overslost
    r2b = df[wicklost][b]*100
    if overslost == 0:
        r2 = df[0][51-overstplay]*100
    else:
        r2 = 100-(r2a-r2b)
    if r1 > r2:
        rt2s = round(t1s*(r2/r1))
    elif r2 > r1:
        rt2s = round(t1s+g50*(r2-r1)/100)+1
    else:
        rt2s = t1s
    st.write("Required runs are:{}".format(rt2s-t2s))
    st.write("from {} overs".format(overstplay-oversplayed-overslost))
    # st.write(rt2s-t2s)
    return rt2s


if choice == "1st Innings":
    # df=pd.read_excel('dls.xlsx')
    # df=df.astype("str")
    # st.write(int(df[0][2])*100)
    st.write(round(212*(82.7/95.0)))

    # st.write(d.head)
    st.title('DLS Method')
    st.write("Welcome to the Duckworth Lewis Method, this is a mathematical formulation designed to calculate the target score for the team batting second in a limited overs cricket match interrupted by weather or other circumstances.")
    st.write("--------------------------------")
    st.header("If interruption occurs in 1st Innings!")

    # enter the number of interruptiosn due to rain
    st.write("Enter number of interruptions that occured due to rain!")
    no_of_rains = st.selectbox('', options=['1', '2', '3', '4'])
    if no_of_rains == '1':
        overstplay = st.number_input("overs decided to be played at start")
        oversplayed = st.number_input("Number of overs played")
        overslost = st.number_input("Number of overs lost")
        wicklost = st.number_input("Number of wickets lost")
        overstplaybyt2 = st.number_input(
            "Number of overs to be played by team 2")
        t1s = st.number_input("Score at the end of the innings")
        result = ""
        if st.button("Find"):
            result = pred1(overstplay, oversplayed, overslost,
                           wicklost, overstplaybyt2, t1s)
        st.success("the par score is {}".format(result))

    # elif no_of_rains == '2':
    #     # overstplay_afterpred1, oversplayed_afterpred1, overslost_afterpred1, wicketslost, oversplaybyt2, t1s_afterpred1
    #     overstplay = st.number_input(
    #         "overs decided to be played at start for team 2")
    #     oversplayed = st.number_input("Number of overs played")
    #     overslost = st.number_input("Number of overs lost before 2nd interruption")
    #     overslost_secondtime = st.number_input("Number of overs lost after 2nd interruption")
    #     wicketslost = st.number_input("Number of wickets lost")
    #     oversplaybyt2 = st.number_input(
    #         "Number of overs to be played by team 2")
    #     t1s_afterpred1 = st.number_input("Score at the end of the innings")
    #     result = ""
    #     if st.button("Find"):
    #         result = pred2rain2(overstplay, oversplayed, overslost, overslost_secondtime, wicketslost, t1s, t2s, overs_start2_suspension, overs_end2_suspension)
    #     st.success("the par score is {}".format(result))


elif choice == "2nd Innings":
    st.write("Welcome to the Duckworth Lewis Method")
    st.write("--------------------------------")
    st.header("If interruption occurs in 2nd Innings!")
    overstplay = st.number_input("overs decided to be played at start")
    oversplayed = st.number_input("Number of overs played by t2")
    t2s = st.number_input("Score of Team-2")
    wicklost = st.number_input("Number of wickets lost")
    overslost = st.number_input("Number of overs lost")
    t1s = st.number_input("Runs scored by Team-1")
    result = ""
    if st.button("Find"):
        result = pred2(overstplay, oversplayed,
                       overslost, wicklost, t1s, t2s)
    st.success("Revised target is {}".format(result))

elif choice == "Classifier":
    st.write("Welcome to the Duckworth Lewis Method")
    st.write("--------------------------------")
    st.write("Choose anyone of the following Supervised Learning Algorithms:")
    algo = ["SVM", "Random Forest", "Linear REgression",
            "Logistic Regression", "Naive Bayes"]
    select_algo = st.selectbox("Select algorithm", algo)
    if select_algo == "SVM":
        st.write("SVM-Support Vector Machine")
        st.write('''
                :o: SVM is a supervised machine learning algorithm which can be used for classification or regression problems. It uses a technique called the kernel trick to transform your data and then based on these transformations it finds an optimal boundary between the possible outputs.
                
                ''')

    elif select_algo == "Random Forest":
        st.write("Random Forest")
        st.write('''
                :o: Random forest is a Supervised Machine Learning Algorithm 
                    that is used widely in Classification and Regression 
                    problems. It builds decision trees on different samples 
                    and takes their majority vote for classification and average 
                    in case of regression.
                
                ''')

    elif select_algo == "Linear Regression":
        st.write("Linear Regression")
        st.write(''' 
            :o: Linear Regression is a supervised machine learning algorithm where the predicted output is continuous and has a constant slope. It's used to predict values within a continuous range, (e.g. sales, price) rather than trying to classify them into categories (e.g. cat, dog).
             ''')

    elif select_algo == "Logistic Regression":
        st.write("Logistic Regression")
        st.write(''' 
            :o: Logistic Regression is a Machine Learning algorithm which is used for the classification problems, it is a predictive analysis algorithm and based on the concept of probability. ... The hypothesis of logistic regression tends it to limit the cost function between 0 and 1 .
            ''')
    else:
        st.write("Naive Bayes")
        st.write(''' 
            :o: Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions. It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.
            ''')

elif choice == "About":

    st.title("\n ** :tophat: Improved D/L Method :tophat: ** \n")
    st.write("-----------")
    st.header("PROBLEM")
    st.write('''
                :o: Duckworth Lewis methodology is used in rain-interrupted matches in cricket to predict par scores.
                    It uses parameters like overs, wickets to predict the target.
                
                :o: But, it is not fair if we don’t consider batsmen statistics like his average in the respected format 
                    of the game, his Strike Rate, or any bowler’s economy, and some other terms that are not defined by 
                    the Standard Duckworth Lewis Method.

                :o: our project intends to improve the existing  Duckworth Lewis method including the above attributes 
                    and for that, It requires Machine Learning practices and algorithms to complete this project.
                ''')

    st.write("-----------")
    st.header("SOLUTION")
    st.write('''
                :ballot_box_with_check: We propose to improve this method using different Machine Learning algorithms.
                :ballot_box_with_check: A Web Application that can predict the par score and winning chances of a team.
                :ballot_box_with_check: This Web App will predict the score for any rain interrupted matches depending on player's stats which is not yet implemented by ICC.
                ''')
