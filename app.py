from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Little Champs School</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
            .header { display: flex; align-items: center; background-color: #007bff; padding: 15px; color: white; }
            .header h1 { flex: 1; font-size: 36px; margin: 0; padding-left: 20px; }
            .navbar { display: flex; justify-content: center; background-color: #0056b3; padding: 10px; }
            .navbar a { color: white; text-decoration: none; padding: 10px 20px; font-size: 18px; }
            .navbar a:hover { background-color: #003d80; border-radius: 5px; }
            .container { text-align: center; padding: 20px; }
            h2 { color: #007bff; }
            img { width: 100%; max-width: 800px; border-radius: 10px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Little Champs School</h1>
            <div class="navbar">
                <a href="#about">About Us</a>
                <a href="#admissions">Admissions</a>
                <a href="#events">Events</a>
                <a href="#login">Login</a>
                <a href="#signup">Sign Up</a>
                <a href="#contact">Contact</a>
            </div>
        </div>

        <div class="container">
            <h2>Welcome to Little Champs School</h2>
            <img src="/images/school_main.jpg" alt="School Building">
            <p>Empowering Young Minds with Knowledge and Creativity!</p>
        </div>

        <div id="about" class="container">
            <h2>About Us</h2>
            <img src="/images/school_students.jpg" alt="Students in Classroom">
            <p>Little Champs School is dedicated to nurturing young minds with innovative learning and creativity.</p>
        </div>

        <div id="admissions" class="container">
            <h2>Admissions</h2>
            <img src="/images/school_admissions.jpg" alt="Admissions Office">
            <p>Join our vibrant learning community! Contact us for enrollment details.</p>
        </div>

        <div id="events" class="container">
            <h2>Upcoming Events</h2>
            <img src="/images/school_events.jpg" alt="School Events">
            <p>Stay tuned for exciting school events and activities!</p>
        </div>

        <div id="contact" class="container">
            <h2>Contact Us</h2>
            <img src="/images/school_contact.jpg" alt="School Contact">
            <p>Email: info@littlechampsschool.com | Phone: +123 456 7890</p>
        </div>
    </body>
    </html>
    """

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == "__main__":
    app.run(debug=True)
