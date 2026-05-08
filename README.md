# Smart Observability & Log Intelligence Platform using Grafana Stack, Maven, Docker & CI/CD Automation

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Maven](https://img.shields.io/badge/maven-build-C71A36)
![Spring Boot](https://img.shields.io/badge/spring--boot-microservice-6DB33F)
![Grafana](https://img.shields.io/badge/grafana-monitoring-orange)

## 📌 Project Overview
A complete, production-grade DevOps automation and observability platform. It features a centralized Control Dashboard that manages multiple containerized microservices (including a Maven/Spring Boot application), automatically aggregates logs using Promtail and Loki, and visualizes system health via Grafana with Alertmanager anomaly detection.

## 🏗️ Architecture
The platform is designed around a Dockerized microservices architecture. It includes:
- **Mock Services (Java Spring Boot, Node.js, etc.)**: Generate traffic and logs.
- **Promtail**: Scrapes logs from all running Docker containers.
- **Loki**: Stores and indexes logs sent by Promtail.
- **Alertmanager**: Evaluates alerting rules against Loki's logs and manages alert notifications.
- **Grafana**: Visualizes logs, metrics, and alerts via provisioned dashboards.
- **Control Dashboard**: A Flask-based web UI to easily start, stop, and test the stack.

## 📁 Repository Structure
```text
.
├── .github/workflows/       # CI/CD pipelines
├── alerts/                  # Alertmanager rules for log anomalies
├── apps/                    # Microservices (auth, payment, order, notification)
├── control-dashboard/       # Python/Flask central control UI
├── dashboards/              # Grafana dashboard JSON models
├── docs/                    # Academic and planning documentation
├── monitoring/              # Configuration for Loki, Promtail, Grafana, Alertmanager
├── docker-compose.yml       # Main orchestration file
└── test_stack.py            # Script to simulate traffic and generate errors
```

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose installed.
- Python 3.8+ (for running the test scripts).

### Setup Instructions
1. **Start the Stack**:
   Run the following command to spin up all microservices and the observability pipeline:
   ```bash
   docker compose up -d
   ```
2. **Access the Control Dashboard**:
   Open your browser and navigate to `http://localhost:5500`. From here, you can manage the stack and access other UIs.
3. **Simulate Traffic**:
   Run the test script to generate normal traffic and simulated anomalies:
   ```bash
   python test_stack.py
   ```
4. **View Dashboards**:
   Access Grafana at `http://localhost:3005` (No login required) to view the auto-provisioned anomaly detection dashboards.


## 🛠️ Built With
- **Docker & Docker Compose** - Containerization & Orchestration
- **Java Spring Boot & Maven** - Enterprise Microservice Architecture
- **Flask & Bootstrap** - Control Dashboard UI
- **Loki & Promtail** - Log Aggregation & Scraping
- **Grafana** - Visualization
- **Alertmanager** - Alerting
- **GitHub Actions** - CI/CD Automation
