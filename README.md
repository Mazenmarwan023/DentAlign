# DentAlign - Dental Clinic Management System with CDSS

[![React](https://img.shields.io/badge/Frontend-React_19-blue.svg)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Build_Tool-Vite-646CFF.svg)](https://vitejs.dev/)
[![Django](https://img.shields.io/badge/Backend-Django_6.0-092E20.svg)](https://www.djangoproject.com/)
[![PyTorch](https://img.shields.io/badge/AI_Model-PyTorch_U--Net-EE4C2C.svg)](https://pytorch.org/)

**DentAlign** is an enterprise-grade Dental Health Information System (HIS) with an integrated **Clinical Decision Support System (CDSS)** powered by Deep Learning. It streamlines clinic management, patient booking, radiology image filtering, and automated dental caries segmentation.

---

## Key Features

- **AI Clinical Decision Support System (CDSS)**: Automated dental caries segmentation built using PyTorch U-Net (EfficientNet-B0 backbone). Returns confidence metrics and base64 overlay masks.
- **Radiology & Image Processing**: SimpleITK filters (Sharpening, Gaussian Smoothing, Noise Reduction) for dental X-rays.
- **Interactive DICOM Viewer**: High-resolution viewer with Zoom, Pan, Rotation, Contrast, and Brightness adjustments.
- **Analytics & Visual Reports**: Interactive Charts (Bar, Pie, Line) powered by `Chart.js` for clinic KPIs, financial performance, and patient growth.
- **Role-Based Access Control (RBAC)**: Secure routes tailored for Doctors, Nurses, Staff, and Patients.


## Website Screenshots & Previews


### 1. Homepage & Landing Portal

<img width="1792" height="948" alt="Screenshot 2026-07-31 at 6 13 11 PM" src="https://github.com/user-attachments/assets/01ee30c4-55e9-4cd8-9b2b-b4bd486d7af3" />

<img width="1792" height="1025" alt="Screenshot 2026-07-31 at 6 13 37 PM" src="https://github.com/user-attachments/assets/172ab7c7-dfab-4462-addd-f5aacc2fb12b" />

---

### 2. Login & Role Authentication

<img width="1765" height="1036" alt="Screenshot 2026-07-31 at 6 14 44 PM" src="https://github.com/user-attachments/assets/1f873c16-d9b1-47c9-b71e-8487cf62a48b" />

---

### 3. Doctor & Staff Dashboard

<img width="1791" height="595" alt="Screenshot 2026-07-31 at 6 17 55 PM" src="https://github.com/user-attachments/assets/1187e7bf-431b-4e6a-b864-6ca72ff46838" />

<img width="1788" height="905" alt="Screenshot 2026-07-31 at 6 19 14 PM" src="https://github.com/user-attachments/assets/45dfe963-a7af-41c3-8d5a-aea1c27c87d4" />

<img width="1768" height="1014" alt="Screenshot 2026-07-31 at 6 19 40 PM" src="https://github.com/user-attachments/assets/c2524253-654a-4b83-b55e-41e194512b8d" />

---

### 4. AI Caries Detection (CDSS)

<img width="1787" height="1033" alt="Screenshot 2026-07-31 at 6 16 40 PM" src="https://github.com/user-attachments/assets/9bfa420e-c7eb-4caf-beb5-fb749038f207" />


---

### 5. Patient Portal & Booking Flow

<img width="1775" height="867" alt="Screenshot 2026-07-31 at 6 22 31 PM" src="https://github.com/user-attachments/assets/67a106ed-6bed-4ab8-bd6c-2fa33c293e2c" />

<img width="1784" height="1012" alt="Screenshot 2026-07-31 at 6 22 48 PM" src="https://github.com/user-attachments/assets/7f46d54a-9d09-4ab0-8053-928889bc7559" />

<img width="1782" height="839" alt="Screenshot 2026-07-31 at 6 23 08 PM" src="https://github.com/user-attachments/assets/1257217b-986f-40b1-917d-ef106aab8f07" />


---


## Tech Stack

- **Frontend**: React 19, Vite, React Router v7, Chart.js, CornerstoneJS, Vanilla CSS Modules.
- **Backend**: Python 3.12, Django 6.0, Django REST Framework, Token Auth.
- **AI & Imaging**: PyTorch, torchvision, segmentation_models_pytorch, SimpleITK, Pillow, NumPy.
- **Database**: SQLite / PostgreSQL.

---

## Quick Start Guide

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

## Demo Login Credentials

| Role | Email | Password | Allowed Access |
| :--- | :--- | :--- | :--- |
| 👨‍⚕️ **Doctor** | `doctor@dentalign.com` | `password123` | Full Staff Access, Radiology, CDSS, Analytics |
| 👤 **Patient** | `patient@dentalign.com` | `password123` | Booking, Prescriptions, Treatment History |

---

## Project Structure

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

## Contributors

- [Mazen Marwan](https://github.com/Mazenmarwan023)
- [Saif Taha](https://github.com/seiftaha)
- [Mohamed Yasser](https://github.com/mahmoudmo22)
- [Malak Emad](https://github.com/malak-emad)
- [Nariman Ahmed](https://github.com/nariman-ahmed)

---

## 📝 License & Contact

Developed for **DentAlign Clinical Information Systems**.  
Repository: [https://github.com/Mazenmarwan023/DentAlign](https://github.com/Mazenmarwan023/DentAlign)
