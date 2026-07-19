# ☁️ CloudStream

A cloud-native file storage platform built using **FastAPI, PostgreSQL, MinIO, Docker, and Kubernetes**. CloudStream demonstrates modern DevOps practices including containerization, orchestration, autoscaling, object storage, and secure authentication.

---

## 🚀 Features

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 📁 File Upload API
- 🗄️ PostgreSQL Database
- ☁️ MinIO Object Storage
- 🐳 Docker & Docker Compose
- ☸️ Kubernetes Deployment
- 🌐 Kubernetes Ingress
- 📈 Horizontal Pod Autoscaler (HPA)
- ❤️ Health Checks
- 📖 Interactive Swagger API Documentation

---

# 🏗️ Architecture

```
                    User
                      │
                      ▼
                 Kubernetes Ingress
                      │
                      ▼
               FastAPI Backend
                 │          │
                 │          │
                 ▼          ▼
          PostgreSQL     MinIO
             Database   Object Storage
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| MinIO | Object Storage |
| Docker | Containerization |
| Kubernetes | Container Orchestration |
| Docker Compose | Local Development |
| JWT | Authentication |
| GitHub | Version Control |

---

# 📂 Project Structure

```
CloudStream/
│
├── backend/
├── frontend/
├── docker/
├── kubernetes/
├── monitoring/
├── docs/
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# ⚙️ Local Setup

## Clone Repository

```bash
git clone https://github.com/deepak7lal/CloudStream.git
cd CloudStream
```

---

## Docker Compose

```bash
docker compose up --build
```

---

## Kubernetes Deployment

```bash
kubectl apply -f kubernetes/
```

Check resources:

```bash
kubectl get all -n cloudstream
```

---

# 📡 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

---

# 📦 MinIO Console

```
http://localhost:9001
```

Default Credentials

Username

```
minioadmin
```

Password

```
minioadmin123
```

---

# 📊 Kubernetes Components

- Namespace
- Deployment
- Service
- Secret
- Persistent Volume Claim
- Ingress
- Horizontal Pod Autoscaler
- Metrics Server

---

# 📷 Screenshots

Add screenshots here:

- Swagger UI
- MinIO Dashboard
- Kubernetes Pods
- HPA
- Ingress
- Docker Desktop

---

# 🔮 Future Improvements

- CI/CD using GitHub Actions
- Monitoring with Prometheus & Grafana
- HTTPS using Cert-Manager
- AWS S3 Integration
- Redis Caching
- Role-Based Access Control (RBAC)

---

# 👨‍💻 Author

**Deepak Lal**

GitHub:
https://github.com/deepak7lal

---

# ⭐ If you found this project useful, please consider giving it a star.
