import streamlit as st
import random

def set_difficulty(level):
    if level == "Easy":
        return 1, 10
    elif level == "Medium":
        return 1, 50
    else:
        return 1, 100

def main():
    st.title("🎯 Number Guessing Game")

    # Select difficulty
    difficulty = st.selectbox("Choose Difficulty Level:", ["Easy", "Medium", "Hard"])
    min_val, max_val = set_difficulty(difficulty)

    # Game instructions
    st.write(f"I'm thinking of a number between **{min_val} and {max_val}**.")
    st.write("You have **5 attempts** to guess it!")

    # Initialize game state
    if "target" not in st.session_state or st.session_state.get("difficulty") != difficulty:
        st.session_state.target = random.randint(min_val, max_val)
        st.session_state.attempts = 0
        st.session_state.max_attempts = 5
        st.session_state.game_over = False
        st.session_state.difficulty = difficulty

    if not st.session_state.game_over:
        guess = st.number_input("Enter your guess:", min_value=min_val, max_value=max_val, step=1)

        if st.button("Submit Guess"):
            st.session_state.attempts += 1

            if guess < st.session_state.target:
                st.info("🔻 Too low!")
            elif guess > st.session_state.target:
                st.info("🔺 Too high!")
            else:
                st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} tries.")
                st.session_state.game_over = True

            # Check for max attempts
            if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
                st.error(f"❌ Game Over! You've used all {st.session_state.max_attempts} attempts.")
                st.info(f"The correct number was **{st.session_state.target}**.")
                st.session_state.game_over = True

    else:
        if st.button("🔄 Play Again"):
            # Reset everything
            st.session_state.target = random.randint(min_val, max_val)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.session_state.difficulty = difficulty

if __name__ == "__main__":
    main()
