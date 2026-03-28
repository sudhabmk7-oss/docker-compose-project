# Docker Compose Flask + MySQL Project

## Overview

This project demonstrates a multi-container application using Docker Compose.
A Flask backend connects to a MySQL database running in a separate container.

---

## 🛠 Tech Stack

* Python (Flask)
* MySQL
* Docker
* Docker Compose

---

## Features

* Multi-container setup using Docker Compose
* Flask-based backend API
* MySQL database integration
* Automatic service communication via Docker network

---

## How to Run

```bash
docker compose up --build
```

---

## Access Application

Open in browser:
http://localhost:5000

---

## Project Structure

```
docker-compose-project/
│
├── docker-compose.yml
└── app/
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
```

---

## Key Learnings

* Dockerfile vs Docker Compose
* Container networking
* Docker build cache issues and debugging
* Database persistence in containers

---

##  Author: 
Sudha