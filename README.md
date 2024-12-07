# CS Careers Website

Live deployment: [CS Careers Website](https://careers-website-52q0.onrender.com)  
Visit the link above to explore open positions, learn about the organization, and connect with us.

---

## Overview

The **CS Careers Website** is a responsive, user-friendly platform designed for showcasing job opportunities in computer science-related fields. It provides an interface to explore available roles, learn about the company, and easily contact the recruitment team.

## Technologies Used

### Frontend
- **HTML5**: Semantic structure.
- **Bootstrap 5.3.3**: For styling and responsive design.

### Backend
- **Jinja2 Templating**: To include reusable components (`nav.html`, `footer.html`, `jobitems.html`) and dynamically render job data.

### Hosting
- **Render**: Deployed and hosted at [https://careers-website-52q0.onrender.com](https://careers-website-52q0.onrender.com).

---

## Directory Structure

```plaintext
.
├── templates/
│   ├── nav.html        # Navbar template
│   ├── footer.html     # Footer template
│   ├── jobitems.html   # Job listing template
├── static/
│   ├── banner.jpg      # Banner image
│   ├── favicon.png     # Favicon for the site
│   ├── side-image.jpg  # Image for the About section
└── README.md           # Documentation (this file)
```

---

## Deployment

1. The project is hosted on [Render](https://render.com).
2. Deployed link: [CS Careers Website](https://careers-website-52q0.onrender.com).

---

## How to Run Locally

### Prerequisites
- **Python** (if using a Flask backend).
- A web browser for viewing the HTML file.

### Steps
1. Clone the repository:  
   ```bash
   git clone <repository-link>
   ```

2. Navigate to the project directory:  
   ```bash
   cd project-folder
   ```

3. (Optional) If Flask is used as the backend, start the server:  
   ```bash
   python app.py
   ```

4. Open `index.html` in your browser to view the site.
