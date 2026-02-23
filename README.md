A production-style **Django Todo web application** containerized with Docker and integrated with a full **CI/CD pipeline** using Jenkins and GitHub Actions. This project simulates a real-world DevOps workflow where every code push automatically triggers build, test, and deployment stages.

---

## 🚀 Project Overview

This project demonstrates core DevOps practices including:

- Containerizing a Django application using **Docker**
- Writing a multi-stage `Dockerfile` for a clean, minimal image
- Automating the build and deployment process using **Jenkins** and/or **GitHub Actions**
- Managing environment variables and application configuration for containers
- Running the full app stack consistently across any environment

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Django | Python web framework |
| Docker | Containerization |
| Jenkins | CI/CD pipeline automation |
| GitHub Actions | Automated build & deployment |
| SQLite / PostgreSQL | Database |
| Gunicorn | WSGI HTTP Server |

---

## 📁 Project Structure

```
django-todo-cicd/
├── todoapp/               # Django application
├── templates/             # HTML templates
├── Dockerfile             # Container build instructions
├── docker-compose.yml     # Multi-container orchestration
├── Jenkinsfile            # CI/CD pipeline definition
├── requirements.txt       # Python dependencies
├── manage.py              # Django management CLI
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

### 1. Clone the Repository

```bash
git clone https://github.com/saeedtamboli01/django-todo-cicd.git
cd django-todo-cicd
```

### 2. Build and Run with Docker

```bash
docker build -t django-todo-app .
docker run -p 8000:8000 django-todo-app
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

Visit `http://localhost:8000` in your browser.

---

## 🔄 CI/CD Pipeline

The CI/CD pipeline is triggered automatically on every push to the `main` branch.

### Pipeline Stages

```
Code Push → GitHub → Jenkins/GitHub Actions
    ↓
[ Stage 1: Checkout Code ]
    ↓
[ Stage 2: Install Dependencies ]
    ↓
[ Stage 3: Run Tests ]
    ↓
[ Stage 4: Build Docker Image ]
    ↓
[ Stage 5: Deploy Container ]
```

### Jenkinsfile (Pipeline Definition)

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { git 'https://github.com/saeedtamboli01/django-todo-cicd.git' }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t django-todo-app .' }
        }
        stage('Run Tests') {
            steps { sh 'docker run django-todo-app python manage.py test' }
        }
        stage('Deploy') {
            steps { sh 'docker-compose up -d' }
        }
    }
}
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

## 📌 Key Learnings

- How to write a production-ready `Dockerfile` for a Python/Django app
- Setting up an automated CI/CD pipeline from scratch
- Connecting GitHub with Jenkins for webhook-triggered deployments
- Managing containerized environments with Docker Compose

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

> Built by [Saeed Tamboli](https://github.com/saeedtamboli01) — DevOps Enthusiast
