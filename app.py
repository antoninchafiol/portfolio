from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html", is_homepage=True)


# Primary Color: Dark Blue (#003366)
# Accent Color: Coffee Brown (#6F4F28)
# Neutral Background: Light Grey (#F0F0F0) or Off-White (#E8E8E8)


# Portfolio page: returns full page or partial update via HTMX
healthcare_projects = [
    {
        "name": "AI-Powered No-Show Prediction",
        "image": "https://via.placeholder.com/300x200",
        "issue": "Huge amount of time lost due to preparing for a patient that'll not come to an appointment.",
        "tech": "Python, Pandas, TensorFlow",
        "resolution": "Implemented an AI-driven API that trains on specific data and predicts if a patient will attend with a High, Medium or Low probability.",
        "github_url": "#"
    },
    {
        "name": "Healthcare Virtual Library",
        "image": "https://via.placeholder.com/300x200",
        "issue": "Inefficient hospital workflow causing operational delays.",
        "tech": "JavaScript, Node.js, React",
        "resolution": "Developed an integrated dashboard to streamline tasks, cutting processing time by 35%.",
        "github_url": "#"
    },
    {
        "name": "ECG/EKG Myocardial Ischemia Prediction",
        "image": "https://via.placeholder.com/300x200",
        "issue": "Lack of real-time data affecting patient monitoring.",
        "tech": "IoT, MQTT, AWS",
        "resolution": "Deployed a real-time system to track vital signs, enabling prompt intervention.",
        "github_url": "#"
    },
    {
        "name": "Teachable Robots",
        "image": "https://via.placeholder.com/300x200",
        "issue": "Lack of quick response in dynamic environments.",
        "tech": "IoT, MQTT, AWS",
        "resolution": "Deployed a system that learns from user input to automate repetitive tasks.",
        "github_url": "#"
    }
]

other_projects = [
    {
        "name": "AI CIFAR-10 Classification Tuning",
        "category": "AI - Computer Vision",
        "description": "Tried to get the highest accuracy on the CIFAR10 Dataset without changing any data.",
        "technologies": "Python, TensorFlow", 
        "url" :"hhtps://google.com",
    },
    {
        "name": "COVID Data Analysis",
        "category": "Data Analysis",
        "description": "Tested the COVID dataset and analyzed the content to output insightful plots.",
        "technologies": "Python, Pandas, Matplotlib"
    },
    {
        "name": "AI Classification of Disaster Tweets",
        "category": "AI - Natural Language Processing",
        "description": "Preprocessed and classified tweets to detect disaster-related content using from-scratch AI modelling.",
        "technologies": "Python, TensorFlow"
    },
    {
        "name": "AI Sign Language Detection",
        "category": "AI - Computer Vision",
        "description": "Detected which sign language letter is present in an image.",
        "technologies": "Python, TensorFlow"
    },
    {
        "name": "AI Voice Activated Commands",
        "category": "AI - Computer Vision/Speech Recognition",
        "description": "Detected spoken words to activate specific routines.",
        "technologies": "Python, TensorFlow"
    },
    {
        "name": "Solar Powerplant Output Prediction",
        "category": "Machine Learning",
        "description": "Used machine learning to predict solar powerplant output based on historical data.",
        "technologies": "Python, TensorFlow"
    },
    {
        "name": "Automatic Robots for Payment",
        "category": "Video Games",
        "description": "Automated payment processing by detecting game’s internal billing events.",
        "technologies": "Python, OpenCV"
    },
    {
        "name": "Logistic Automation",
        "category": "Video Games",
        "description": "Automated employee admissions and inventory tracking using Google Sheets/Form and Discord bot commands.",
        "technologies": "Google Sheets/Form, Python, JS, Discord"
    },
    {
        "name": "Ansible automation",
        "category": "Automation/DevOps",
        "description": "Automation of the company's OS/Db Upgrading systems",
        "technologies": "Python, Ansible",

    }
]
@app.route("/portfolio")
def portfolio():
    # Show 2 healthcare projects and 3 other projects initially
    healthcare_initial = healthcare_projects[:2]
    other_initial = other_projects[:3]
    return render_template("portfolio.html", 
                           healthcare_projects=healthcare_initial, 
                           other_projects=other_initial)

# HTMX route to load remaining healthcare projects
@app.route("/portfolio/healthcare-more")
def portfolio_healthcare_more():
    remaining = healthcare_projects[2:]
    return render_template("partials/featured_more.html", healthcare_projects=remaining)

# HTMX route to load remaining other projects
@app.route("/portfolio/other-more")
def portfolio_other_more():
    remaining = other_projects[3:]
    return render_template("partials/other_more.html", other_projects=remaining)


# Blog page
@app.route("/blog")
def blog():
    posts = [
        {"title": "My First Post", "excerpt": "Welcome to my blog...", "url": "#"},
        {"title": "A Day in the Life", "excerpt": "Today I worked on...", "url": "#"},
        # add more posts as needed
    ]
    if request.headers.get("HX-Request"):
        return render_template("partials/blog_list.html", posts=posts)
    return render_template("blog.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    services = [
        {
            "title": "AI & Automation in Healthcare",
            "description": "Custom AI models for medical imaging (Object Detection, Image Segmentation). Automating repetitive tasks like report generation and data processing.",
            "icon": "💡",
        },
        {
            "title": "Healthcare Data & Analytics",
            "description": "Processing and visualizing medical data using Tableau, Pandas, and more. Optimizing databases for PACS, EHR, and healthcare APIs.",
            "icon": "📊",
        },
        {
            "title": "Web & API Development for Healthcare",
            "description": "Building secure web apps using Flask + HTMX. Integrating APIs like OpenFDA and Google Cloud Healthcare API.",
            "icon": "🖥️",
        },
    ]

    if request.headers.get("HX-Request"):
        return render_template("partials/service_list.html", services=services)

    return render_template("services.html", services=services)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Here, you can process the form (e.g., send an email)
        print(f"New Contact Request from {name} ({email}): {message}")

        return jsonify({"success": True, "message": "Your message has been sent!"})

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
