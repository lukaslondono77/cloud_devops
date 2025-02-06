# Cloud DevOps Project 🚀
[![CI/CD Pipeline](https://github.com/lukaslondono77/cloud_devops/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/lukaslondono77/cloud_devops/actions/workflows/ci-cd.yml)
## **Overview**
This project is a **cloud-native SaaS (Software-as-a-Service) task management tool** built using modern **DevOps** and **cloud technologies**. It demonstrates a **real-world CI/CD pipeline**, **secure infrastructure automation**, and **scalable deployment**.

---

## **1️⃣ Backend - Python Flask API**
### 🔹 **Purpose:** 
Provides RESTful API endpoints for task management.  
### 🔹 **Technology:** 
Python (Flask), SQLAlchemy (ORM), PostgreSQL.  
### 🔹 **Key Features:**
- Fetch all tasks (`GET /tasks`)
- Add a new task (`POST /tasks`)
- Update a task (`PUT /tasks/<id>`)
- Delete a task (`DELETE /tasks/<id>`)

---

## **2️⃣ Database - AWS RDS (PostgreSQL)**
### 🔹 **Purpose:** 
Stores task data persistently in the cloud.  
### 🔹 **Technology:** 
**AWS RDS (Relational Database Service) - PostgreSQL**  
### 🔹 **Key Features:**
- Provides a fully managed SQL database.
- Handles backups, patching, and scaling automatically.
- Integrated with AWS security best practices.

---

## **3️⃣ Containerization - Docker**
### 🔹 **Purpose:** 
Ensures the application runs consistently in any environment.  
### 🔹 **Technology:** 
**Docker**  
### 🔹 **Key Features:**
- Defines an isolated runtime environment.
- Eliminates “works on my machine” problems.
- Simplifies deployment and scalability.

---

## **4️⃣ Kubernetes Deployment - AWS EKS**
### 🔹 **Purpose:** 
Orchestrates and scales containers efficiently.  
### 🔹 **Technology:** 
**AWS EKS (Elastic Kubernetes Service)**  
### 🔹 **Key Features:**
- Manages multiple containers across multiple machines.
- Automatically scales applications based on demand.
- Ensures high availability and reliability.

---

## **5️⃣ CI/CD Pipeline - GitHub Actions**
### 🔹 **Purpose:** 
Automates testing, security scanning, and deployment.  
### 🔹 **Technology:** 
**GitHub Actions**  
### 🔹 **Key Features:**
- Runs tests automatically on every code change.
- Builds and pushes Docker images to **AWS ECR**.
- Deploys to **AWS EKS** automatically.

---

## **6️⃣ Infrastructure as Code (IaC) - Terraform**
### 🔹 **Purpose:** 
Automates AWS resource provisioning.  
### 🔹 **Technology:** 
**Terraform**  
### 🔹 **Key Features:**
- Manages **AWS RDS (PostgreSQL)**, **AWS EKS**, **AWS S3**, **IAM roles**.
- Defines cloud infrastructure as **code**.
- Ensures consistent deployments across environments.

---

## **7️⃣ Security & Best Practices**
### 🔹 **Purpose:** 
Ensure a secure application and infrastructure.  
### 🔹 **Technology:** 
Flask-Talisman, AWS IAM, TLS Encryption.  
### 🔹 **Key Features:**
- **Flask-Talisman** secures HTTP headers.
- **AWS IAM Roles** follow the principle of **least privilege**.
- **Docker security scanning** ensures no vulnerabilities.
- **HTTPS enforced** for secure communication.

---

## **8️⃣ Logging & Monitoring - AWS CloudWatch**
### 🔹 **Purpose:** 
Monitor performance and troubleshoot issues.  
### 🔹 **Technology:** 
**AWS CloudWatch**  
### 🔹 **Key Features:**
- Tracks **API response times, errors, and logs**.
- Sends **alerts via AWS SNS** when an issue is detected.
- Provides **real-time monitoring dashboards**.

---

## **9️⃣ AWS Lambda - Serverless Functions**
### 🔹 **Purpose:** 
Automates background tasks.  
### 🔹 **Technology:** 
**AWS Lambda + SES (Simple Email Service)**  
### 🔹 **Key Features:**
- Sends **email notifications** when a task is created.
- Runs event-driven workflows **without servers**.

---

## **🔹 End-to-End Flow of the Project**
1️⃣ **User creates a task** → The Flask API saves it in **AWS RDS**.  
2️⃣ **Task is stored** in a managed **PostgreSQL database**.  
3️⃣ **Dockerized application runs** inside **AWS EKS** (Kubernetes).  
4️⃣ **GitHub Actions pipeline** tests, builds, and deploys the application automatically.  
5️⃣ **Terraform provisions AWS resources** automatically.  
6️⃣ **AWS CloudWatch monitors logs and performance.**  
7️⃣ **AWS Lambda sends email notifications when tasks are created.**  

---

## **🔹 Why This Project Matters?**
### **For DevOps Engineers** 🎯  
✅ **Demonstrates full CI/CD automation with GitHub Actions**  
✅ **Uses Infrastructure as Code (Terraform) for AWS provisioning**  
✅ **Deploys with Kubernetes & Docker for scalability**  
✅ **Ensures security with IAM, TLS, and security scanning**  
✅ **Implements monitoring with CloudWatch & alerts with SNS**  

### **For Developers** 💡  
✅ **Builds a RESTful API using Python & Flask**  
✅ **Manages data with SQLAlchemy & PostgreSQL**  
✅ **Uses AWS Lambda for serverless automation**  

---

## **🔹 Next Steps (Improvements)**
- [ ] **Add frontend (React or Vue.js)**
- [ ] **Improve task management features (authentication, UI, etc.)**
- [ ] **Use AWS DynamoDB for NoSQL scalability**
- [ ] **Implement GraphQL for better API performance**

---

## **📥 Download the Project**
You can download the latest version of this project as a ZIP file.

Let me know if you need modifications or additional features! 🚀
