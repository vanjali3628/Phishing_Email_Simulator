import tkinter as tk
from tkinter import ttk


# =========================================================
# COLORS
# =========================================================

BG = "#080D1A"
CARD = "#11182B"
CARD2 = "#0D1424"

WHITE = "#F5F7FF"
MUTED = "#8993B5"

CYAN = "#00F5D4"
PURPLE = "#9B5DE5"
GREEN = "#00E676"
RED = "#FF4D6D"
YELLOW = "#FFD166"


# =========================================================
# EMAIL DATABASE
# =========================================================

emails = [

    {
        "sender": "security-alert@microsoft-support.com",
        "subject": "URGENT: Your account will be suspended!",
        "body": """Dear User,

We detected unusual activity on your account.

Your account will be permanently suspended within 24 hours.

Click the link below immediately to verify your account:

[ Verify Your Account ]

Thank you,
Security Team""",
        "answer": "phishing",
        "explanation":
            "The sender uses a suspicious domain that imitates a "
            "trusted company. The message also creates urgency "
            "and asks the user to verify the account.",
        "indicators": [
            "Suspicious sender domain",
            "Urgent and threatening language",
            "Unexpected verification request"
        ]
    },

    {
        "sender": "library@vvitu.ac.in",
        "subject": "Library Book Return Reminder",
        "body": """Dear Student,

This is a reminder that the library book currently
issued to you is due for return.

Please return the book before the due date.

Regards,
VVITU Library""",
        "answer": "legitimate",
        "explanation":
            "This appears legitimate because it is a normal "
            "library reminder from an official-looking college "
            "domain and does not request sensitive information.",
        "indicators": [
            "Official-looking college domain",
            "Normal informational message",
            "No sensitive information requested"
        ]
    },

    {
        "sender": "hr@company-careers.com",
        "subject": "Congratulations! You Won a Job Offer",
        "body": """Congratulations!

You have been selected for an immediate job opportunity.

To confirm your offer, send:

Username
Password
Bank Account Details

Reply within 30 minutes.

HR Department""",
        "answer": "phishing",
        "explanation":
            "The email unexpectedly offers a job and requests "
            "highly sensitive information such as a password and "
            "bank details. The short deadline creates pressure.",
        "indicators": [
            "Requests password and bank details",
            "Unexpected job offer",
            "Artificial time pressure"
        ]
    },

    {
        "sender": "events@vvitu.ac.in",
        "subject": "Cybersecurity Workshop Registration",
        "body": """Hello Student,

Your registration for the Cybersecurity Awareness
Workshop has been successfully received.

The event details will be shared through the
official college communication channel.

Regards,
Event Coordination Team""",
        "answer": "legitimate",
        "explanation":
            "This appears legitimate because it provides normal "
            "registration information and does not request passwords "
            "or financial information.",
        "indicators": [
            "Normal registration confirmation",
            "Official-looking college domain",
            "No sensitive information requested"
        ]
    },

    {
        "sender": "support@paypa1-security.com",
        "subject": "Suspicious Login Detected",
        "body": """Dear Customer,

A suspicious login was detected on your account.

To prevent account closure, verify your identity
immediately using the link below.

[ Confirm Identity ]

Failure to respond may result in account suspension.

Security Department""",
        "answer": "phishing",
        "explanation":
            "The sender domain imitates a trusted payment service "
            "using a misleading character substitution. The message "
            "also uses fear and urgency.",
        "indicators": [
            "Misleading sender domain",
            "Fear-based language",
            "Immediate verification request"
        ]
    },

    {
        "sender": "examcell@vvitu.ac.in",
        "subject": "Semester Examination Schedule",
        "body": """Dear Students,

The semester examination schedule has been
published on the official college notice board.

Students are requested to check the notice board
for examination dates and timings.

Regards,
Examination Cell""",
        "answer": "legitimate",
        "explanation":
            "This is a normal academic notification. It does not "
            "request credentials, payment, or suspicious actions.",
        "indicators": [
            "Normal academic communication",
            "No password request",
            "No suspicious action required"
        ]
    },

    {
        "sender": "delivery-update@fastcourier-track.com",
        "subject": "Your Package Could Not Be Delivered",
        "body": """Dear Customer,

We were unable to deliver your package.

Your delivery address needs to be confirmed.

Click below and pay a small redelivery fee:

[ Confirm Delivery ]

Your package will be returned if you do not respond today.""",
        "answer": "phishing",
        "explanation":
            "The message uses delivery failure as a reason to request "
            "payment and personal information. The urgency and "
            "suspicious sender domain are warning signs.",
        "indicators": [
            "Suspicious delivery domain",
            "Unexpected payment request",
            "Urgent deadline"
        ]
    },

    {
        "sender": "careers@vvitu.ac.in",
        "subject": "Internship Orientation Session",
        "body": """Dear Students,

An internship orientation session will be conducted
for interested students.

Date: Monday
Time: 10:00 AM
Venue: Seminar Hall

Students may attend the session to learn about
available opportunities.

Regards,
Career Development Cell""",
        "answer": "legitimate",
        "explanation":
            "This is a normal college career announcement. It "
            "provides event information without requesting sensitive "
            "credentials or financial details.",
        "indicators": [
            "Normal college announcement",
            "Clear event details",
            "No sensitive information requested"
        ]
    },

    {
        "sender": "bank-reward@secure-banking-alert.com",
        "subject": "You Have Won a ₹25,000 Reward!",
        "body": """Congratulations!

Your account has been selected for a ₹25,000 reward.

To receive your reward, confirm your:

ATM PIN
OTP
Internet Banking Password

Offer expires in 15 minutes.

[ Claim Reward ]""",
        "answer": "phishing",
        "explanation":
            "This is phishing because it asks for an ATM PIN, OTP "
            "and banking password. Legitimate organizations should "
            "never ask users to disclose these authentication secrets.",
        "indicators": [
            "Requests OTP and PIN",
            "Fake reward claim",
            "Extreme time pressure"
        ]
    },

    {
        "sender": "notifications@vvitu.ac.in",
        "subject": "Student Portal Maintenance Notice",
        "body": """Dear Students,

The student portal will undergo scheduled maintenance
from 11:00 PM to 1:00 AM.

During this period, some services may be temporarily
unavailable.

No action is required from students.

Regards,
IT Support Team""",
        "answer": "legitimate",
        "explanation":
            "This is a routine system maintenance notification. "
            "It does not ask students to provide passwords, payment "
            "information, or click suspicious links.",
        "indicators": [
            "Routine maintenance notice",
            "No credentials requested",
            "No suspicious action required"
        ]
    }
]


# =========================================================
# VARIABLES
# =========================================================

current_email = 0
score = 0
answered = False


# =========================================================
# LOAD EMAIL
# =========================================================

def load_email():

    global answered

    answered = False

    email = emails[current_email]

    email_number.config(
        text=f"EMAIL {current_email + 1} OF {len(emails)}"
    )

    score_label.config(
        text=f"SCORE: {score}"
    )

    progress_value.set(
        (current_email / len(emails)) * 100
    )

    sender_label.config(
        text=email["sender"]
    )

    subject_label.config(
        text=email["subject"]
    )

    body_text.config(state="normal")
    body_text.delete("1.0", tk.END)
    body_text.insert(tk.END, email["body"])
    body_text.config(state="disabled")

    feedback_title.config(
        text="ANALYZE THE EMAIL",
        fg=CYAN
    )

    feedback_text.config(
        text="Choose whether this email is phishing or legitimate.",
        fg=MUTED
    )

    explanation_title.config(
        text="💡 WHY?",
        fg=YELLOW
    )

    explanation_text.config(
        text="The explanation will appear after you answer.",
        fg=MUTED
    )

    for label in indicator_labels:
        label.config(
            text="○ Waiting for analysis",
            fg=MUTED
        )

    phishing_button.config(
        state="normal"
    )

    legitimate_button.config(
        state="normal"
    )

    next_button.config(
        state="disabled"
    )


# =========================================================
# ANSWER
# =========================================================

def answer(choice):

    global score
    global answered

    if answered:
        return

    answered = True

    email = emails[current_email]

    phishing_button.config(
        state="disabled"
    )

    legitimate_button.config(
        state="disabled"
    )

    if choice == email["answer"]:

        score += 1

        feedback_title.config(
            text="✓ CORRECT ANSWER",
            fg=GREEN
        )

        feedback_text.config(
            text=(
                "Excellent! You correctly identified this email as "
                + email["answer"].upper()
                + "."
            ),
            fg=GREEN
        )

    else:

        feedback_title.config(
            text="✗ INCORRECT ANSWER",
            fg=RED
        )

        feedback_text.config(
            text=(
                "This email is actually "
                + email["answer"].upper()
                + "."
            ),
            fg=RED
        )

    score_label.config(
        text=f"SCORE: {score}"
    )

    progress_value.set(
        ((current_email + 1) / len(emails)) * 100
    )

    explanation_title.config(
        text="💡 WHY IS THIS EMAIL "
        + email["answer"].upper()
        + "?",
        fg=YELLOW
    )

    explanation_text.config(
        text=email["explanation"],
        fg=WHITE
    )

    for i, indicator in enumerate(email["indicators"]):

        indicator_labels[i].config(
            text="• " + indicator,
            fg=YELLOW
        )

    # NEXT BUTTON BECOMES ACTIVE
    next_button.config(
        state="normal"
    )


# =========================================================
# NEXT EMAIL
# =========================================================

def next_email():

    global current_email

    if not answered:
        return

    current_email += 1

    if current_email >= len(emails):

        show_final_report()

    else:

        load_email()


# =========================================================
# RESTART
# =========================================================

def restart_simulation():

    global current_email
    global score
    global answered

    current_email = 0
    score = 0
    answered = False

    load_email()


# =========================================================
# FINAL REPORT
# =========================================================

def show_final_report():

    percentage = int(
        (score / len(emails)) * 100
    )

    phishing_total = sum(
        1 for email in emails
        if email["answer"] == "phishing"
    )

    legitimate_total = len(emails) - phishing_total

    if percentage >= 80:

        level = "EXCELLENT AWARENESS"
        level_color = GREEN

    elif percentage >= 60:

        level = "GOOD AWARENESS"
        level_color = YELLOW

    else:

        level = "NEEDS IMPROVEMENT"
        level_color = RED

    report = tk.Toplevel(root)

    report.title(
        "Phishing Awareness Report"
    )

    report.geometry(
        "540x650"
    )

    report.resizable(
        False,
        False
    )

    report.configure(
        bg=BG
    )

    tk.Label(
        report,
        text="🛡",
        font=("Segoe UI", 38),
        bg=BG,
        fg=CYAN
    ).pack(
        pady=(15, 0)
    )

    tk.Label(
        report,
        text="SIMULATION COMPLETE",
        font=("Segoe UI", 19, "bold"),
        bg=BG,
        fg=WHITE
    ).pack()

    tk.Label(
        report,
        text=f"{score} / {len(emails)}",
        font=("Segoe UI", 32, "bold"),
        bg=BG,
        fg=CYAN
    ).pack(
        pady=(10, 0)
    )

    tk.Label(
        report,
        text=f"AWARENESS SCORE: {percentage}%",
        font=("Segoe UI", 11, "bold"),
        bg=BG,
        fg=WHITE
    ).pack()

    tk.Label(
        report,
        text=level,
        font=("Segoe UI", 13, "bold"),
        bg=BG,
        fg=level_color
    ).pack(
        pady=6
    )

    # Statistics card
    stats = tk.Frame(
        report,
        bg=CARD,
        padx=20,
        pady=12
    )

    stats.pack(
        padx=25,
        pady=5,
        fill="x"
    )

    tk.Label(
        stats,
        text="📊 SIMULATION STATISTICS",
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=PURPLE
    ).pack(
        anchor="w",
        pady=(0, 7)
    )

    tk.Label(
        stats,
        text=f"Total emails analyzed: {len(emails)}",
        font=("Segoe UI", 8),
        bg=CARD,
        fg=MUTED
    ).pack(
        anchor="w"
    )

    tk.Label(
        stats,
        text=f"Phishing examples: {phishing_total}",
        font=("Segoe UI", 8),
        bg=CARD,
        fg=RED
    ).pack(
        anchor="w"
    )

    tk.Label(
        stats,
        text=f"Legitimate examples: {legitimate_total}",
        font=("Segoe UI", 8),
        bg=CARD,
        fg=GREEN
    ).pack(
        anchor="w"
    )

    # Tips
    tips_card = tk.Frame(
        report,
        bg=CARD,
        padx=20,
        pady=12
    )

    tips_card.pack(
        padx=25,
        pady=5,
        fill="x"
    )

    tk.Label(
        tips_card,
        text="🛡 PHISHING PREVENTION TIPS",
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=PURPLE
    ).pack(
        anchor="w",
        pady=(0, 5)
    )

    tips = [
        "Check the sender's email address.",
        "Be careful with urgent messages.",
        "Never share passwords or OTPs.",
        "Avoid suspicious links and attachments.",
        "Verify unexpected requests independently."
    ]

    for tip in tips:

        tk.Label(
            tips_card,
            text="✓ " + tip,
            font=("Segoe UI", 8),
            bg=CARD,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=1
        )

    tk.Button(
        report,
        text="↻  RESTART SIMULATION",
        command=lambda: [
            report.destroy(),
            restart_simulation()
        ],
        font=("Segoe UI", 9, "bold"),
        bg=PURPLE,
        fg=WHITE,
        relief="flat",
        padx=20,
        pady=8,
        cursor="hand2"
    ).pack(
        pady=7
    )

    tk.Button(
        report,
        text="CLOSE",
        command=report.destroy,
        font=("Segoe UI", 8, "bold"),
        bg="#252D46",
        fg=WHITE,
        relief="flat",
        padx=20,
        pady=6,
        cursor="hand2"
    ).pack()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Phishing Email Awareness Simulator"
)

root.geometry(
    "900x720"
)

root.minsize(
    850,
    650
)

root.configure(
    bg=BG
)


# =========================================================
# HEADER
# =========================================================

tk.Label(
    root,
    text="◈",
    font=("Segoe UI", 25, "bold"),
    bg=BG,
    fg=CYAN
).pack(
    pady=(5, 0)
)

tk.Label(
    root,
    text="PHISHING EMAIL SIMULATOR",
    font=("Segoe UI", 20, "bold"),
    bg=BG,
    fg=WHITE
).pack()

tk.Label(
    root,
    text="CYBERSECURITY AWARENESS TRAINING",
    font=("Segoe UI", 8, "bold"),
    bg=BG,
    fg=PURPLE
).pack(
    pady=(1, 5)
)


# =========================================================
# EMAIL NUMBER + SCORE
# =========================================================

top_frame = tk.Frame(
    root,
    bg=BG
)

top_frame.pack(
    padx=30,
    fill="x"
)

email_number = tk.Label(
    top_frame,
    text="EMAIL 1 OF 10",
    font=("Segoe UI", 8, "bold"),
    bg=BG,
    fg=CYAN
)

email_number.pack(
    side="left"
)

score_label = tk.Label(
    top_frame,
    text="SCORE: 0",
    font=("Segoe UI", 8, "bold"),
    bg=BG,
    fg=WHITE
)

score_label.pack(
    side="right"
)


# =========================================================
# PROGRESS
# =========================================================

progress_value = tk.DoubleVar()

progress = ttk.Progressbar(
    root,
    variable=progress_value,
    maximum=100,
    length=840
)

progress.pack(
    padx=30,
    pady=(3, 6)
)


# =========================================================
# EMAIL CARD
# =========================================================

email_card = tk.Frame(
    root,
    bg=CARD,
    padx=20,
    pady=10
)

email_card.pack(
    padx=30,
    fill="x"
)


tk.Label(
    email_card,
    text="FROM",
    font=("Segoe UI", 7, "bold"),
    bg=CARD,
    fg=MUTED
).pack(
    anchor="w"
)

sender_label = tk.Label(
    email_card,
    text="",
    font=("Consolas", 9),
    bg=CARD,
    fg=WHITE
)

sender_label.pack(
    anchor="w"
)


tk.Label(
    email_card,
    text="SUBJECT",
    font=("Segoe UI", 7, "bold"),
    bg=CARD,
    fg=MUTED
).pack(
    anchor="w",
    pady=(3, 0)
)

subject_label = tk.Label(
    email_card,
    text="",
    font=("Segoe UI", 10, "bold"),
    bg=CARD,
    fg=WHITE
)

subject_label.pack(
    anchor="w"
)


body_text = tk.Text(
    email_card,
    height=5,
    font=("Segoe UI", 9),
    bg=CARD2,
    fg=WHITE,
    relief="flat",
    wrap="word",
    padx=12,
    pady=7
)

body_text.pack(
    fill="x",
    pady=(5, 0)
)

body_text.config(
    state="disabled"
)


# =========================================================
# QUESTION
# =========================================================

tk.Label(
    root,
    text="IS THIS EMAIL PHISHING OR LEGITIMATE?",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=CYAN
).pack(
    pady=(6, 4)
)


# =========================================================
# ANSWER BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack()


phishing_button = tk.Button(
    button_frame,
    text="🚨 PHISHING",
    command=lambda: answer("phishing"),
    font=("Segoe UI", 9, "bold"),
    bg="#3A1825",
    fg=RED,
    activebackground="#552033",
    activeforeground=WHITE,
    relief="flat",
    padx=25,
    pady=7,
    cursor="hand2"
)

phishing_button.pack(
    side="left",
    padx=5
)


legitimate_button = tk.Button(
    button_frame,
    text="✓ LEGITIMATE",
    command=lambda: answer("legitimate"),
    font=("Segoe UI", 9, "bold"),
    bg="#123328",
    fg=GREEN,
    activebackground="#194936",
    activeforeground=WHITE,
    relief="flat",
    padx=25,
    pady=7,
    cursor="hand2"
)

legitimate_button.pack(
    side="left",
    padx=5
)


# =========================================================
# FEEDBACK
# =========================================================

feedback_card = tk.Frame(
    root,
    bg=CARD,
    padx=15,
    pady=6
)

feedback_card.pack(
    padx=30,
    pady=6,
    fill="x"
)


feedback_title = tk.Label(
    feedback_card,
    text="ANALYZE THE EMAIL",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=CYAN
)

feedback_title.pack(
    anchor="w"
)


feedback_text = tk.Label(
    feedback_card,
    text="Choose an answer to analyze the email.",
    font=("Segoe UI", 8),
    bg=CARD,
    fg=MUTED,
    wraplength=820,
    justify="left"
)

feedback_text.pack(
    anchor="w"
)


# =========================================================
# EXPLANATION
# =========================================================

explanation_card = tk.Frame(
    root,
    bg=CARD,
    padx=15,
    pady=6
)

explanation_card.pack(
    padx=30,
    fill="x"
)


explanation_title = tk.Label(
    explanation_card,
    text="💡 WHY?",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=YELLOW
)

explanation_title.pack(
    anchor="w"
)


explanation_text = tk.Label(
    explanation_card,
    text="The explanation will appear after you answer.",
    font=("Segoe UI", 8),
    bg=CARD,
    fg=MUTED,
    wraplength=820,
    justify="left"
)

explanation_text.pack(
    anchor="w"
)


# =========================================================
# INDICATORS
# =========================================================

indicator_card = tk.Frame(
    root,
    bg=CARD,
    padx=15,
    pady=5
)

indicator_card.pack(
    padx=30,
    pady=6,
    fill="x"
)


tk.Label(
    indicator_card,
    text="🔎 EMAIL INDICATORS",
    font=("Segoe UI", 9, "bold"),
    bg=CARD,
    fg=PURPLE
).pack(
    anchor="w"
)


indicator_labels = []

for i in range(3):

    label = tk.Label(
        indicator_card,
        text="○ Waiting for analysis",
        font=("Segoe UI", 8),
        bg=CARD,
        fg=MUTED
    )

    label.pack(
        anchor="w"
    )

    indicator_labels.append(label)


# =========================================================
# NEXT EMAIL
# =========================================================

next_button = tk.Button(
    root,
    text="NEXT EMAIL  →",
    command=next_email,
    font=("Segoe UI", 10, "bold"),
    bg=PURPLE,
    fg=WHITE,
    activebackground="#B47CFF",
    relief="flat",
    padx=30,
    pady=7,
    cursor="hand2",
    state="disabled"
)

next_button.pack(
    pady=(2, 3)
)


# =========================================================
# RESTART
# =========================================================

tk.Button(
    root,
    text="↻ RESTART",
    command=restart_simulation,
    font=("Segoe UI", 7, "bold"),
    bg="#252D46",
    fg=CYAN,
    activebackground="#343D60",
    relief="flat",
    padx=15,
    pady=4,
    cursor="hand2"
).pack()


# =========================================================
# FOOTER
# =========================================================

tk.Label(
    root,
    text="🛡 EDUCATIONAL SIMULATION • NO REAL EMAILS • NO CREDENTIALS COLLECTED",
    font=("Segoe UI", 6, "bold"),
    bg=BG,
    fg="#626B91"
).pack(
    pady=(2, 3)
)


# =========================================================
# START APPLICATION
# =========================================================

load_email()

root.mainloop()