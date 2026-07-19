
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
<img width="1806" height="939" alt="SWAGGER" src="https://github.com/user-attachments/assets/6140026f-b217-4829-a7d2-736b823072f9" />
<img width="1863" height="957" alt="MinIO" src="https://github.com/user-attachments/assets/294d547c-6e31-4a03-9b49-861a0f50a668" />
<img width="600" height="83" alt="KUBERNETES PODS" src="https://github.com/user-attachments/assets/e8dfadae-8cd3-4e79-9bbf-6af3b00eb90a" />
<img width="839" height="49" alt="HPA" src="https://github.com/user-attachments/assets/ef5a1cbf-a706-49c0-a2d6-68eeef2c31a7" />





---

# ⭐ If you found this project useful, please consider giving it a star.
