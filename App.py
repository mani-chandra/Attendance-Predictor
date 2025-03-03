import streamlit as st

def calculate_attendance(attended_classes, total_classes):
    return (attended_classes / total_classes) * 100

def predict_future_attendance(attended_classes, total_classes, remaining_classes):
    total_future_classes = total_classes + remaining_classes
    future_attendance = (attended_classes + remaining_classes) / total_future_classes * 100
    return future_attendance

def safe_bunk_calculator(attended_classes, total_classes, remaining_classes, min_attendance):
    safe_bunks = 0
    total_future_classes = total_classes + remaining_classes

    for bunked_classes in range(remaining_classes + 1):
        future_attendance = (attended_classes + (remaining_classes - bunked_classes)) / total_future_classes * 100
        if future_attendance >= min_attendance:
            safe_bunks = bunked_classes
        else:
            break

    return safe_bunks

st.title("🎓 Attendance Predictor & Bunk Calculator")

total_classes = st.number_input("Total classes conducted so far", min_value=1, value=50)
attended_classes = st.number_input("Total classes attended so far", min_value=0, value=35)
remaining_classes = st.number_input("Total remaining classes", min_value=0, value=20)
min_attendance = st.number_input("Minimum required attendance (%)", min_value=0, max_value=100, value=75)

if st.button("Predict Attendance"):
    current_attendance = calculate_attendance(attended_classes, total_classes)
    future_attendance = predict_future_attendance(attended_classes, total_classes, remaining_classes)
    safe_bunks = safe_bunk_calculator(attended_classes, total_classes, remaining_classes, min_attendance)

    st.write(f"✅ **Current Attendance:** {current_attendance:.2f}%")
    st.write(f"📊 **Future Attendance (if attending all classes):** {future_attendance:.2f}%")
    st.write(f"🚀 **Safe Bunk Limit:** {safe_bunks} classes")

    if current_attendance >= min_attendance:
        st.success("🟢 Attendance is Safe!")
    elif future_attendance >= min_attendance:
        st.warning("🟡 Attendance is recoverable if you attend all future classes.")
    else:
        st.error("🔴 High Risk! Even if you attend all classes, you may fall below the required attendance.")

st.info("📚 Plan your bunks wisely!")

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        👨‍💻 Developed by <b>Mani Chandra Rao</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center;">
        👨‍💻 Developed by <b>👨‍💻 Connect with me on LinkedIn](https://www.linkedin.com/in/manichandrarao</b>
    </div>
    """,
    unsafe_allow_html=True
)
