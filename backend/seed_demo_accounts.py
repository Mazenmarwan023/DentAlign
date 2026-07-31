import os
import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from accounts.models import User, Role
from staff.models import Patient, Staff

def seed():
    print("🌱 Seeding Roles and Users...")
    
    # 1. Create Roles
    roles = ['Doctor', 'Nurse', 'Staff', 'Patient', 'Admin']
    role_objs = {}
    for r_name in roles:
        r_obj, _ = Role.objects.get_or_create(name=r_name, defaults={'description': f'{r_name} role'})
        role_objs[r_name] = r_obj
        print(f"Role: {r_name}")

    # Helper function to create or update user
    def create_user(email, password, full_name, role_name, is_verified=True, license_num=''):
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': email,
                'full_name': full_name,
                'password_hash': make_password(password),
                'role': role_objs[role_name],
                'is_verified': is_verified,
                'medical_license_number': license_num
            }
        )
        if not created:
            user.full_name = full_name
            user.password_hash = make_password(password)
            user.role = role_objs[role_name]
            user.is_verified = is_verified
            user.medical_license_number = license_num
            user.save()
        print(f"✅ User {'created' if created else 'updated'}: {email} ({role_name})")
        return user

    # Create Doctor
    doc_user = create_user('doctor@dentalign.com', 'password123', 'Dr. Ahmed Aly', 'Doctor', True, 'MED-12345')
    Staff.objects.get_or_create(
        user=doc_user,
        defaults={
            'first_name': 'Ahmed',
            'last_name': 'Aly',
            'role_title': 'Dentist / Orthodontist',
            'license_number': 'MED-12345',
            'specialization': 'Orthodontics & CDSS Specialist'
        }
    )

    # Create Nurse
    nurse_user = create_user('nurse@dentalign.com', 'password123', 'Nurse Sarah Vance', 'Nurse', True, 'NUR-9982')
    Staff.objects.get_or_create(
        user=nurse_user,
        defaults={
            'first_name': 'Sarah',
            'last_name': 'Vance',
            'role_title': 'Dental Nurse',
            'license_number': 'NUR-9982'
        }
    )

    # Create Patient
    patient_user = create_user('patient@dentalign.com', 'password123', 'Sarah Jenkins', 'Patient')
    Patient.objects.get_or_create(
        user=patient_user,
        defaults={
            'first_name': 'Sarah',
            'last_name': 'Jenkins',
            'email': 'patient@dentalign.com',
            'phone': '+1 (555) 234-5678',
            'gender': 'Female',
            'medical_history': 'No major allergies. Routine dental cleanings.'
        }
    )

    print("\n🎉 Seeding complete! Demo credentials configured.")

if __name__ == '__main__':
    seed()
