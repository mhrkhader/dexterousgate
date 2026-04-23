from flask import Flask, render_template, request
import smtplib
import os
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# HOME
@app.route("/")
def index():
    return render_template("index.html")

# EXCEL
@app.route("/excel")
def excel():
    return render_template("excel.html")

# SQL
@app.route("/sql")
def sql():
    return render_template("sql.html")

# POWER BI
@app.route("/powerbi")
def powerbi():
    return render_template("powerbi.html")

# CONTACT
@app.route("/contact", methods=["GET", "POST"])
def contact():

    success = False

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

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

            server.login(
                "maher.zoom.training@gmail.com",
                "yitf zszp ueyy hupb"
            )

            server.send_message(msg)
            server.quit()

            success = True

        except Exception as e:
            print("EMAIL ERROR:", e)

    return render_template("contact.html", success=success)


# RUN (FIXED FOR RENDER)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)