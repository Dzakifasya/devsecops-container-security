# DevSecOps Container Security

![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-Security%20Scanning-1904DA?logo=aqua&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Focus-Container%20Security-success)

Repository praktikum **DevOpsSec – Container Security** yang berisi pembelajaran, implementasi, dan pengujian keamanan container menggunakan Docker, Trivy, serta GitHub Actions.

Proyek ini berfokus pada penerapan prinsip keamanan container, identifikasi kerentanan pada Docker image, pembuatan Secure Dockerfile, dan otomatisasi vulnerability scanning melalui CI/CD pipeline.

---

## Project Overview

Container Security merupakan salah satu aspek penting dalam praktik DevSecOps. Penggunaan container mempermudah proses deployment aplikasi, tetapi image dan dependensi di dalamnya tetap berpotensi memiliki kerentanan keamanan.

Melalui praktikum ini, dilakukan beberapa tahapan untuk memahami dan menerapkan keamanan container, mulai dari penggunaan Docker hingga integrasi pemindaian keamanan secara otomatis.

### Objectives

- Memahami konsep dasar Docker dan containerization.
- Mengenal proses pengelolaan Docker image dan container.
- Melakukan vulnerability scanning menggunakan Trivy.
- Mengidentifikasi kerentanan pada OS packages dan dependencies.
- Menerapkan prinsip Secure Dockerfile.
- Menggunakan multi-stage build untuk menghasilkan image yang lebih efisien.
- Menerapkan prinsip least privilege dengan non-root user.
- Mengintegrasikan Trivy ke dalam GitHub Actions.
- Mengotomatisasi pemeriksaan keamanan setiap terjadi push atau pull request.

---

## Project Structure

```text
devsecops-container-security/
│
├── .github/
│   └── workflows/
│       └── trivy-scan.yml
│
├── Lab 1 - Docker Fundamentals/
│   └── Catatan Praktikum Lab 1 - Docker Fundamentals.txt
│
├── Lab 2 - Trivy Scanning/
│   └── lab-trivy/
│       └── requirements.txt
│   └── scan-result.json
│   └── scan-result.sarif
│
├── Lab 3 - Secure Dockerfile/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile.insecure
│   ├── Dockerfile.secure
│   └── .dockerignore
│
├── Lab 4 - GitHub Actions/
│
├── Tugas Praktikum/
│
├── Laporan/
│
└── README.md
```

---

## Practical Labs

### Lab 1 – Docker Fundamentals

Mempelajari dasar-dasar Docker dan containerization.

Materi:
- Pengenalan Docker.
- Docker image dan container.
- Docker Engine dan Docker CLI.
- Menjalankan container.
- Mengelola image dan container.
- Melihat container logs dan status.

### Lab 2 – Trivy Scanning

Melakukan pemeriksaan keamanan menggunakan Trivy untuk mengidentifikasi kerentanan pada file system dan dependencies.

Materi:
- Pengenalan Trivy.
- Filesystem vulnerability scanning.
- Identifikasi vulnerability severity.
- Output hasil scanning dalam format JSON dan SARIF.
- Analisis hasil vulnerability scanning.

### Lab 3 – Secure Dockerfile

Menerapkan praktik keamanan dalam pembuatan Docker image.

Implementasi:
- Perbandingan insecure dan secure Dockerfile.
- Penggunaan base image yang lebih modern.
- Multi-stage Docker build.
- Penggunaan non-root user.
- Pembaruan OS packages.
- Dependency management.
- Penggunaan `.dockerignore`.

**Security improvements:**

| Aspek | Implementasi |
|---|---|
| Base image | Python 3.12 Alpine |
| Build strategy | Multi-stage build |
| User privilege | Non-root (`appuser`) |
| OS packages | APK package upgrade |
| Dependencies | Flask 2.3.2 |
| Build context | `.dockerignore` |

### Lab 4 – GitHub Actions

Mengintegrasikan Trivy ke dalam GitHub Actions untuk mengotomatisasi pemeriksaan keamanan Docker image.

Fitur workflow:
- Automatic repository checkout.
- Docker image build.
- Trivy vulnerability scanning.
- Pemeriksaan severity HIGH dan CRITICAL.
- CI pipeline dengan security gate.

Workflow:
`.github/workflows/trivy-scan.yml`

Pemindaian dijalankan ketika terjadi:
- Push ke branch `main`.
- Pull request menuju branch `main`.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Dockerfile | Docker image build |
| Python | Application runtime |
| Alpine Linux | Container base OS |
| Trivy | Vulnerability scanning |
| Git & GitHub | Version control |
| GitHub Actions | CI/CD automation |
| PowerShell | Command-line environment |

---

## Running the Secure Container

Pastikan Docker Desktop dan Docker Engine sudah berjalan.

### 1. Build Docker Image

```powershell
docker build --no-cache `
  -f ".\Lab 3 - Secure Dockerfile\Dockerfile.secure" `
  -t app-secure:v2 `
  ".\Lab 3 - Secure Dockerfile"
```

### 2. Run Container

```powershell
docker run -d `
  --name app-secure `
  -p 8080:8080 `
  app-secure:v2
```

### 3. Access Application

Buka browser:

```text
http://localhost:8080
```

### 4. Verify Container

```powershell
docker ps
```

Periksa user yang digunakan:

```powershell
docker exec app-secure whoami
```

Expected output:

```text
appuser
```

---

## Vulnerability Scanning

Lakukan pemindaian keamanan pada Docker image menggunakan Trivy.

### Scan Docker Image

```powershell
trivy image app-secure:v2
```

### Filter HIGH and CRITICAL Vulnerabilities

```powershell
trivy image --severity HIGH,CRITICAL app-secure:v2
```

### Scan Filesystem

```powershell
trivy fs --severity CRITICAL,HIGH .
```

### Security Scan Results

Hasil pemindaian lokal pada image `app-secure:v2`:

| Target | HIGH | CRITICAL |
|---|---:|---:|
| Alpine Linux 3.24.4 | 0 | 0 |
| Flask 2.3.2 | 0 | 0 |
| **Total** | **0** | **0** |

Hasil tersebut menunjukkan tidak ditemukan kerentanan dengan severity HIGH maupun CRITICAL pada target yang diperiksa oleh perintah Trivy tersebut.

---

## GitHub Actions – Automated Security Scanning

Repository ini menggunakan GitHub Actions untuk menjalankan proses build dan vulnerability scanning secara otomatis.

Workflow configuration:

```yaml
name: Container Security Scan

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  trivy-scan:
    name: Build and Scan Docker Image
    runs-on: ubuntu-latest
```

Security scanning menggunakan:

```yaml
uses: aquasecurity/trivy-action@v0.36.0
```

Konfigurasi pemeriksaan:

```yaml
with:
  image-ref: app-secure:ci
  format: table
  exit-code: '1'
  ignore-unfixed: true
  vuln-type: os,library
  severity: CRITICAL,HIGH
```

Workflow menggunakan security gate yang membuat job gagal apabila ditemukan kerentanan CRITICAL atau HIGH yang memenuhi kriteria pemindaian.

**CI/CD Status:** Workflow telah berhasil dijalankan dengan status sukses pada GitHub Actions setelah proses remediation.

[View GitHub Actions](https://github.com/Dzakifasya/devsecops-container-security/actions)

---

## Repository

**GitHub:**  
https://github.com/Dzakifasya/devsecops-container-security

**Branch:** `main`

---

## Author

**Dzaki Fasya**  
Informatika – DevOpsSec Practicum

Repository ini dibuat sebagai bagian dari kegiatan praktikum mata kuliah DevOpsSec dengan fokus pada implementasi keamanan container dan otomatisasi vulnerability scanning.

---

*DevSecOps – Container Security | Docker • Trivy • GitHub Actions*
