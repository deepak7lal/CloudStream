# ☁️ CloudStream

CloudStream is a cloud-native file storage backend built using **FastAPI**, **PostgreSQL**, **MinIO**, and **Docker**. It provides secure JWT-based authentication and file management APIs, making it a scalable foundation for cloud applications.

---

## 🚀 Features

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 📤 File Upload
- 📥 File Download
- 📋 List Uploaded Files
- 🗑️ Delete Files
- 🐘 PostgreSQL for metadata storage
- 📦 MinIO for object storage
- 🐳 Docker & Docker Compose support
- 📖 Interactive Swagger API documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend API |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| MinIO | Object Storage |
| JWT | Authentication |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Python 3.11 | Programming Language |

---

## 📂 Project Structure

```text
CloudStream/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   └── files.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── file_models.py
│   │   ├── minio_client.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/deepak7lal/CloudStream.git
cd CloudStream
```

### Start the application

```bash
docker compose up --build
```

---

## 🌐 Services

| Service | URL |
|---------|-----|
| FastAPI Docs | http://localhost:8000/docs |
| MinIO Console | http://localhost:9001 |
| PostgreSQL | localhost:5432 |

---

## 🔑 Default MinIO Credentials

Username

```text
minioadmin
```

Password

```text
minioadmin123
```

---

## 🔒 Authentication

CloudStream uses **JWT (JSON Web Tokens)**.

### Register

```
POST /auth/register
```

### Login

```
POST /auth/login
```

After logging in, use the generated **Bearer Token** to access protected endpoints.

---

## 📁 File APIs

### Upload File

```
POST /files/upload
```

### List Files

```
GET /files
```

### Download File

```
GET /files/{id}
```

### Delete File

```
DELETE /files/{id}
```

---

## 🏗️ Architecture

```text
                User
                  │
                  ▼
            FastAPI Backend
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 PostgreSQL            MinIO Object Storage
(File Metadata)          (Uploaded Files)
                  │
           Docker Compose
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- FastAPI REST API Development
- JWT Authentication
- SQLAlchemy ORM
- PostgreSQL Integration
- MinIO Object Storage
- Docker Containerization
- Docker Compose
- Secure API Development
- Cloud-native Backend Design

---

## 🚀 Future Enhancements

- Kubernetes Deployment
- CI/CD with GitHub Actions
- Role-Based Access Control (RBAC)
- File Versioning
- File Sharing
- AWS S3 Support
- Redis Caching
- Monitoring with Prometheus & Grafana

---

## 👨‍💻 Author

**Deepak Lal**

GitHub: https://github.com/deepak7lal

---

## 📄 License

This project is licensed under the MIT License.
