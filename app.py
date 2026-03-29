import streamlit as st
from speech_to_text import get_voice_input
from llm_to_sql import generate_sql
from db import execute_query
import pandas as pd

# -------------------------------
# ✅ SQL VALIDATION FUNCTION
# -------------------------------
def validate_sql(query):
    if not query:
        return False

    if "DROP" in query.upper():
        return False
    if "DELETE" in query.upper():
        return False

    return True


# -------------------------------
# ✅ LOAD SCHEMA
# -------------------------------
with open("schema.txt", "r") as f:
    schema = f.read()


# -------------------------------
# ✅ UI START
# -------------------------------
st.title("🎤 Voice to SQL AI System")

# Input method
option = st.radio("Choose Input Method:", ["Voice", "Text"])


# -------------------------------
# 🎤 VOICE INPUT
# -------------------------------
if option == "Voice":
    if st.button("🎤 Speak"):
        user_text = get_voice_input()
        st.write("🗣 You said:", user_text)

        sql_query = generate_sql(user_text, schema)
        st.write("🧠 Generated SQL:", sql_query)

        # 🚨 ERROR CHECK (IMPORTANT — ADD HERE)
        if sql_query == "ERROR":
            st.error("❌ Could not understand query")
        
        else:
            try:
                if validate_sql(sql_query):
                    results = execute_query(sql_query)

                    # Show raw results (debug)
                    st.write("📦 Raw Results:", results)

                    if results:
                        df = pd.DataFrame(results)
                        st.subheader("📋 Query Results")
                        st.dataframe(df)
                    else:
                        st.warning("⚠️ No data found")

                else:
                    st.error("❌ Unsafe query blocked!")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")


# -------------------------------
# ⌨️ TEXT INPUT (Optional but useful)
# -------------------------------
else:
    user_text = st.text_input("Type your query")

    if user_text:
        st.write("🗣 You typed:", user_text)

        sql_query = generate_sql(user_text, schema)
        st.write("🧠 Generated SQL:", sql_query)

        # 🚨 ERROR CHECK
        if sql_query == "ERROR":
            st.error("❌ Could not understand query")

        else:
            try:
                if validate_sql(sql_query):
                    results = execute_query(sql_query)

                    st.write("📦 Raw Results:", results)

                    if results:
                        df = pd.DataFrame(results)
                        st.subheader("📋 Query Results")
                        st.dataframe(df)
                    else:
                        st.warning("⚠️ No data found")

                else:
                    st.error("❌ Unsafe query blocked!")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")

    

