from flask import Flask, render_template ,url_for,request,redirect
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

# @app.route('/works.html')
# def works():
#     return render_template('./works.html')

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

# @app.route('/work.html')
# def work():
#     return render_template('./work.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        # Collect form data
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Construct the email
        body = f"You received a new message from {email}\n\nSubject: {subject}\n\nMessage:\n{message}"
        msg = MIMEText(body)
        msg["Subject"] = f"Portfolio Contact: {subject}"
        msg["From"] = "admatieh@gmail.com"       # sender (your Gmail)
        msg["To"] = "admatieh@gmail.com"         # receiver (you again)

        # Send via Gmail SMTP (use App Password, not your real Gmail password)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("admatieh@gmail.com", "uuno roky pmmc gbpu")
            server.send_message(msg)

        return redirect("./thankyou.html")

    except Exception as e:
        return f"Something went wrong: {e}"
    
    
if __name__ == '__main__':
    app.run(debug=True)