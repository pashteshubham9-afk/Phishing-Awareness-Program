import streamlit as st

st.set_page_config(
    page_title="Phishing Awareness Program",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ Phishing Awareness Program")

st.subheader("Learn how to identify and prevent phishing attacks")

st.write("""
This program helps users understand phishing attacks,
recognize warning signs, and learn safe online practices.
""")

st.markdown("---")


# What is Phishing
st.header("🎣 What is Phishing?")

st.info("""
Phishing is a cyber attack where attackers pretend to be
trusted organizations or individuals to steal sensitive
information like passwords, OTPs, banking details, and personal data.
""")


# Types of Phishing
st.header("📚 Types of Phishing Attacks")

st.subheader("📧 Email Phishing")
st.write("""
Attackers send fake emails that look like they come from
banks, companies, or services to steal user information.
""")


st.subheader("🎯 Spear Phishing")
st.write("""
A targeted phishing attack where attackers create
personalized messages for a specific person or organization.
""")


st.subheader("📱 Smishing (SMS Phishing)")
st.write("""
Phishing attacks through SMS messages.

Example:
"Congratulations! You won a prize. Click this link to claim."
""")


st.subheader("📞 Vishing (Voice Phishing)")
st.write("""
Phishing through phone calls where attackers pretend to be
bank employees or service providers.
""")


# Red Flags
st.header("🚩 Phishing Red Flags")

red_flags = [
    "Unknown sender email address",
    "Urgent messages asking for immediate action",
    "Requests for password or OTP",
    "Suspicious links",
    "Spelling and grammar mistakes",
    "Offers that look too good to be true"
]

for item in red_flags:
    st.warning("⚠️ " + item)


# Fake Email Example
st.header("📧 Fake Email Example")

st.error("""
From: support@paypa1-security.com

Your account has been blocked.

Click below immediately to verify your account.

Warning:
- Fake domain name
- Creates urgency
- Requests personal information
""")


st.success("""
Real companies never ask for passwords or OTP through email.
""")


# Website Example
st.header("🌐 Fake Website Example")

st.write("""
❌ Fake Website:
http://amaz0n-login-security.com


✅ Real Website:
https://www.amazon.com


Always check the spelling of website addresses.
""")


# Safety Tips
st.header("🛡️ Safety Tips")

tips = [
    "Enable Two-Factor Authentication (2FA)",
    "Never share OTP or passwords",
    "Verify links before clicking",
    "Keep software updated",
    "Use trusted websites only"
]

for tip in tips:
    st.success("✅ " + tip)



# Quiz Section
st.markdown("---")

st.header("🧠 Phishing Awareness Quiz")


questions = [
    {
        "question": "1. Phishing is mainly used to steal what?",
        "options": [
            "Sensitive information",
            "Computer speed",
            "Screen brightness",
            "Internet speed"
        ],
        "answer": "Sensitive information"
    },

    {
        "question": "2. What should you never share?",
        "options": [
            "OTP and Password",
            "Favorite color",
            "Wallpaper",
            "Username"
        ],
        "answer": "OTP and Password"
    },

    {
        "question": "3. Smishing is phishing through?",
        "options": [
            "SMS",
            "Bluetooth",
            "Games",
            "Camera"
        ],
        "answer": "SMS"
    },

    {
        "question": "4. What should you check before clicking a link?",
        "options": [
            "Website URL",
            "Screen size",
            "Keyboard",
            "Volume"
        ],
        "answer": "Website URL"
    },

    {
        "question": "5. A common phishing sign is?",
        "options": [
            "Urgent request for information",
            "Normal update",
            "Trusted website",
            "Official notice"
        ],
        "answer": "Urgent request for information"
    }
]


answers = []

for q in questions:
    answer = st.radio(
        q["question"],
        q["options"]
    )
    answers.append(answer)


if st.button("Submit Quiz"):

    score = 0

    for i in range(len(questions)):
        if answers[i] == questions[i]["answer"]:
            score += 1

    st.success(f"Your Score: {score}/5")

    if score >= 4:
        st.balloons()
        st.success("Excellent! You have good phishing awareness.")

    elif score >= 2:
        st.info("Good attempt! Keep improving your cyber security knowledge.")

    else:
        st.warning("Learn more about phishing attacks and stay safe.")


# Footer
st.markdown("---")

st.info("💡 Stay Alert! Think Before You Click.")