from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------------- EXCEL ----------------
@app.route("/excel")
def excel():
    return render_template("excel.html")

# ---------------- SQL ----------------
@app.route("/sql")
def sql():
    return render_template("sql.html")

# ---------------- POWER BI ----------------
@app.route("/powerbi")
def powerbi():
    return render_template("powerbi.html")

# ---------------- CONTACT ----------------
@app.route("/contact", methods=["GET", "POST"])
def contact():

    success = False

    if request.method == "POST":

        # FORM DATA
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # DATE & TIME
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

        # EMAIL BODY
        body = f"""
New Contact Message Received:

Name: {name}
Email: {email}
Date & Time: {formatted_time}

Message:
{message}
"""

        msg = MIMEText(body)
        msg["Subject"] = f"Website Contact - {name}"
        msg["From"] = "maher.zoom.training@gmail.com"
        msg["To"] = "maher.zoom.training@gmail.com"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            # ⚠️ MUST BE GMAIL APP PASSWORD
            server.login(
                "maher.zoom.training@gmail.com",
                "yitf zszp ueyy hupb"
            )

            server.send_message(msg)
            server.quit()

            success = True
            print("EMAIL SENT SUCCESSFULLY")

        except Exception as e:
            print("EMAIL ERROR:", e)

    return render_template("contact.html", success=success)


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)