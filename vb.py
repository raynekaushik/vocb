import streamlit as st
import csv

# Initialize your state variables so they persist across reruns
if "index" not in st.session_state:
    st.session_state.index = 0  # Track which card we are on

if "revealed" not in st.session_state:
    st.session_state.revealed = False  # Track if the translation is visible

if "review_mode" not in st.session_state:
    st.session_state.review_mode = False # Review mode to change lists

if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []

# Write a function to load the vocab list
def load_vocab():
    vocab = []
    with open('vocab.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                vocab.append(row)
    return vocab

main_vocab = load_vocab()

if st.session_state.review_mode:
    vocab_list = st.session_state.wrong_answers
else:
    vocab_list = main_vocab

# Check BEFORE accessing the list
if st.session_state.index >= len(vocab_list):

    if (
        not st.session_state.review_mode
        and "wrong_answers" in st.session_state
        and len(st.session_state.wrong_answers) > 0
    ):
        st.session_state.review_mode = True
        st.session_state.index = 0
        st.rerun()

    st.write("Finished!")
    st.stop()

#get the current card based on the index in the session state
current_card = vocab_list[st.session_state.index]
german_word = current_card[0]
english_word = current_card[1]

# Display the German word
st.title("Vocab Trainer")
st.write(f"### Word: {german_word}")

#THE STATE-BASED LOGIC

if not st.session_state.revealed:
    # State is HIDDEN: Show the reveal button
    if st.button("Reveal Translation"):
        st.session_state.revealed = True
        st.rerun()

else:
    # State is REVEALED: Show the actual translation and the "Next" button
    st.write(f"### Translation: {english_word}")
    
    if st.button("Next"):
        st.session_state.index += 1
        st.session_state.revealed = False  # Reset for the next card!
        st.rerun()

#if clicked got wrong the inext will be recorded and sent in a seperate list 
if st.button("I got it wrong"):
    #store the wrong answers in a separate list in session state
    if "wrong_answers" not in st.session_state:
        st.session_state.wrong_answers = []
    
    st.session_state.wrong_answers.append(current_card)
    st.session_state.index += 1
    st.session_state.revealed = False  # Reset for the next card
    st.rerun()       

#Next feature after the innitial list ends, the session_state.wrong_answers starts and 
#when it ends the session reverts to the initial list

if st.session_state.index >= len(vocab_list):

    if not st.session_state.review_mode and len(st.session_state.wrong_answers) > 0:
        st.session_state.review_mode = True
        st.session_state.index = 0
        st.rerun()

    st.write("Finished!")
    st.stop()