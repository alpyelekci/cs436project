# Cloud-Native To-Do Application

This project is a cloud-native to-do list web application developed for the CS436 course. It demonstrates practical skills in designing, deploying, and evaluating scalable applications using Google Cloud Platform (GCP). Demo video and screenshots which are taken during designing process can be seen in this repository.

## 🛠 Technologies Used

- **Backend:** Python, Flask, Gunicorn (WSGI)
- **Cloud Provider:** Google Cloud Platform (GCP)
- **Containerization:** Docker
- **Orchestration:** Google Kubernetes Engine (GKE)
- **Database:** MySQL on Compute Engine VM (initially SQLite)
- **Performance Testing:** Locust

## 📦 Features

- RESTful API with full CRUD operations for to-do items:
  - `POST /todos` – create item
  - `GET /todos` – retrieve items
  - `PUT /todos/{id}` – update item
  - `DELETE /todos/{id}` – delete item
- Simple web UI (mockup for home, login, and new task pages)
- Dummy Cloud Function endpoint for email confirmation
- Optional future support for user login, caching (Redis), HTTPS with TLS

## ☁️ Cloud Architecture
Client (browser)
↓
Cloud Load Balancer
↓
Kubernetes Cluster (GKE)
↓
Flask App (Docker container in Pod)
↓
MySQL Database (on GCP VM)

## 🚀 Deployment Steps

1. **Dockerize** the Flask app using `Dockerfile` and `boot.sh`
2. **Push** the Docker image to Google Container Registry
3. **Create** a GKE cluster and deploy the app using Kubernetes YAML files
4. **Configure** firewall rules for ports 80/443 and expose via external IP
5. **Set up** a MySQL instance on GCP VM and connect it to the app
6. **Deploy** Cloud Functions (optional)
7. **Verify** deployment via public IP: `http://34.46.145.252`

## 🔬 Performance Testing

- Tool: **Locust**
- Endpoint tested: `GET /`
- Results:
  - Avg RPS: 19.5
  - Max response time: 21s
  - Failure rate: ~1%
- Observations:
  - System performs stably under load with occasional latency spikes


