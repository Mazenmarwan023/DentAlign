# 🦷 DentAlign - AI-Powered Dental Clinic Management System & CDSS

[![React](https://img.shields.io/badge/Frontend-React_19-blue.svg)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Build_Tool-Vite-646CFF.svg)](https://vitejs.dev/)
[![Django](https://img.shields.io/badge/Backend-Django_6.0-092E20.svg)](https://www.djangoproject.com/)
[![PyTorch](https://img.shields.io/badge/AI_Model-PyTorch_U--Net-EE4C2C.svg)](https://pytorch.org/)

**DentAlign** is an enterprise-grade Dental Health Information System (HIS) with an integrated **Clinical Decision Support System (CDSS)** powered by Deep Learning. It streamlines clinic management, patient booking, radiology image filtering, and automated dental caries segmentation.

---

## 🖼️ Application Screenshots & Previews

Add your website screenshots into the `docs/screenshots/` folder matching the filenames below.

### 1. Homepage & Landing Portal
> **Image Path**: `docs/screenshots/01-home-page.png`  
> **What to capture**: The hero section, clinic services, and top navigation bar on [http://localhost:5173/](http://localhost:5173/)

![Homepage & Landing Portal](./docs/screenshots/01-home-page.png)

---

### 2. Login & Role Authentication
> **Image Path**: `docs/screenshots/02-login-page.png`  
> **What to capture**: The sign-in form with email/password input on [http://localhost:5173/login](http://localhost:5173/login)

![Login & Authentication](./docs/screenshots/02-login-page.png)

---

### 3. Doctor & Staff Dashboard
> **Image Path**: `docs/screenshots/03-staff-dashboard.png`  
> **What to capture**: The staff navigation sidebar, metric stat cards, upcoming appointments, and patient lists on [http://localhost:5173/staff/dashboard](http://localhost:5173/staff/dashboard)

![Doctor & Staff Dashboard](./docs/screenshots/03-staff-dashboard.png)

---

### 4. AI Caries Detection (CDSS)
> **Image Path**: `docs/screenshots/04-cdss-segmentation.png`  
> **What to capture**: An uploaded dental X-ray with the red AI lesion segmentation mask overlay and confidence percentage on [http://localhost:5173/cdss](http://localhost:5173/cdss)

![AI Caries Detection CDSS](./docs/screenshots/04-cdss-segmentation.png)

---

### 5. Radiology & SimpleITK Image Filtering
> **Image Path**: `docs/screenshots/05-radiology-suite.png`  
> **What to capture**: The radiology upload panel, filter buttons (Sharpen, Smooth, Noise Reduction), and side-by-side scan inspector on [http://localhost:5173/staff/radiology](http://localhost:5173/staff/radiology)

![Radiology Suite](./docs/screenshots/05-radiology-suite.png)

---

### 6. Practice Analytics & Financial Reports
> **Image Path**: `docs/screenshots/06-analytics-reports.png`  
> **What to capture**: The revenue bar chart, appointment status pie chart, and patient growth line chart on [http://localhost:5173/staff/reports](http://localhost:5173/staff/reports)

![Practice Analytics & Reports](./docs/screenshots/06-analytics-reports.png)

---

### 7. Interactive DICOM Viewer
> **Image Path**: `docs/screenshots/07-dicom-viewer.png`  
> **What to capture**: The DICOM image viewport with zoom, rotation, contrast slider, and brightness controls on [http://localhost:5173/dicom](http://localhost:5173/dicom)

![Interactive DICOM Viewer](./docs/screenshots/07-dicom-viewer.png)

---

### 8. Patient Portal & Booking Flow
> **Image Path**: `docs/screenshots/08-patient-portal.png`  
> **What to capture**: The patient dashboard, appointment booking form, and treatment history on [http://localhost:5173/patient/dashboard](http://localhost:5173/patient/dashboard)

![Patient Portal](./docs/screenshots/08-patient-portal.png)

---

## ✨ Key Features

- **⚡ AI Clinical Decision Support System (CDSS)**: Automated dental caries segmentation built using PyTorch U-Net (EfficientNet-B0 backbone). Returns confidence metrics and base64 overlay masks.
- **🩻 Radiology & Image Processing**: SimpleITK filters (Sharpening, Gaussian Smoothing, Noise Reduction) for dental X-rays.
- **👁️ Interactive DICOM Viewer**: High-resolution viewer with Zoom, Pan, Rotation, Contrast, and Brightness adjustments.
- **📊 Analytics & Visual Reports**: Interactive Charts (Bar, Pie, Line) powered by `Chart.js` for clinic KPIs, financial performance, and patient growth.
- **🔐 Role-Based Access Control (RBAC)**: Secure routes tailored for Doctors, Nurses, Staff, and Patients.

---

## 🛠️ Tech Stack

- **Frontend**: React 19, Vite, React Router v7, Chart.js, CornerstoneJS, Vanilla CSS Modules.
- **Backend**: Python 3.12, Django 6.0, Django REST Framework, Token Auth.
- **AI & Imaging**: PyTorch, torchvision, segmentation_models_pytorch, SimpleITK, Pillow, NumPy.
- **Database**: SQLite / PostgreSQL.

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Mazenmarwan023/DentAlign.git
cd DentAlign
```

### 2. Backend Setup (Django)
```bash
# Activate Virtual Environment
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install Dependencies
pip install -r backend/requirements.txt

# Run Migrations & Seed Demo Accounts
python backend/manage.py migrate
python backend/seed_demo_accounts.py

# Start Django Backend Server (Port 8000)
python backend/manage.py runserver 0.0.0.0:8000
```

### 3. Frontend Setup (Vite + React)
```bash
# Navigate to frontend directory
cd frontend

# Install Dependencies
npm install

# Start Vite Development Server
npm run dev
```

Application endpoints:
- **Frontend App**: [http://localhost:5173](http://localhost:5173)
- **Backend REST API**: [http://localhost:8000](http://localhost:8000)

---

## 🔑 Demo Login Credentials

| Role | Email | Password | Allowed Access |
| :--- | :--- | :--- | :--- |
| 👨‍⚕️ **Doctor** | `doctor@dentalign.com` | `password123` | Full Staff Access, Radiology, CDSS, Analytics |
| 👩‍⚕️ **Nurse / Staff** | `nurse@dentalign.com` | `password123` | Patient Management, Appointments, Radiology |
| 👤 **Patient** | `patient@dentalign.com` | `password123` | Booking, Prescriptions, Treatment History |

---

## 📂 Project Structure

```
DentAlign/
├── backend/                  # Django REST Framework backend
│   ├── accounts/             # Authentication & user roles
│   ├── appointments/         # Appointment scheduling logic
│   ├── cdss/                 # PyTorch model inference & overlay generator
│   ├── imaging/              # SimpleITK DICOM processing
│   ├── medical/              # Patient medical history & diagnoses
│   ├── patients/             # Patient management endpoints
│   ├── staff/                # Doctor & staff profile views
│   ├── manage.py
│   └── seed_demo_accounts.py # Demo user seeder script
├── frontend/                 # React + Vite application
│   ├── src/
│   │   ├── app/              # Routes & navigation
│   │   ├── components/       # Common UI components
│   │   ├── features/         # Feature modules (cdss, imaging, staff, patient)
│   └── package.json
├── docs/                     # Screenshots & documentation assets
│   └── screenshots/          # Place site screenshot PNG files here
└── README.md
```

---

## 📝 License & Contact

Developed for **DentAlign Clinical Information Systems**.  
Repository: [https://github.com/Mazenmarwan023/DentAlign](https://github.com/Mazenmarwan023/DentAlign)