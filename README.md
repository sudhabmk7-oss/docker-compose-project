# Docker Compose Flask + MySQL Project

## Overview

This project demonstrates a multi-container application using Docker Compose.
A Flask backend connects to a MySQL database running in a separate container.

---

## Tech Stack

* Python (Flask)
* MySQL
* Docker
* Docker Compose

---

## Features

* Multi-container setup using Docker Compose
* Backend API built with Flask
* MySQL database integration
* Automatic container communication

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
docker-compose-demo/
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
* Volume mapping
* Debugging build and dependency issues

---

## GitHub Repository

https://github.com/sudhabmk7-oss/docker-compose-project
