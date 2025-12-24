# DevOps Assignment: Automated CI/CD Deployment on AWS

## 📖 Project Overview
This project demonstrates a complete **DevOps Lifecycle** for a 2-tier web application. The system is hosted on an AWS EC2 instance and uses **Jenkins** to automate the deployment of a **Node.js Frontend** and **Python Flask Backend**.

### 🏗 Architecture
* **Frontend:** Node.js (Express) serving an HTML contact form.
* **Backend:** Python (Flask) API receiving POST requests.
* **Infrastructure:** AWS EC2 (Ubuntu 24.04).
* **Automation:** Jenkins Pipelines (CI/CD).
* **Process Management:** Linux Systemd Services.

---

## ⚙️ Infrastructure Setup

### 1. Server Provisioning
* **Cloud Provider:** AWS
* **Instance Type:** t2.micro (Free Tier eligible)
* **OS:** Ubuntu 24.04 LTS
* **Storage:** **20 GB EBS Volume** (Resized from default 8GB to prevent build failures).

### 2. Performance Optimizations (Crucial Fixes)
To prevent Jenkins from crashing on a small server, the following optimizations were applied:

* **Swap Memory:** Created a 2GB Swap file to prevent Out-Of-Memory (OOM) crashes.
    ```bash
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```
* **Disk Expansion:** Resized the root filesystem to utilize the full 20GB.
    ```bash
    sudo growpart /dev/nvme0n1 1
    sudo resize2fs /dev/root
    ```

### 3. Software Installation
```bash
# Update System
sudo apt update && sudo apt upgrade -y

# Install Runtime Dependencies
sudo apt install nodejs npm -y
sudo apt install python3-pip -y
pip3 install flask flask-cors --break-system-packages

# Install Jenkins (Java 17 required)
sudo apt install fontconfig openjdk-17-jre -y
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc [https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key](https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key)
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] [https://pkg.jenkins.io/debian-stable](https://pkg.jenkins.io/debian-stable) binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y
