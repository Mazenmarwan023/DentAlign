from django.db import migrations

def add_columns_if_table_exists(apps, schema_editor):
    table_names = schema_editor.connection.introspection.table_names()
    if 'users' in table_names:
        with schema_editor.connection.cursor() as cursor:
            # Check existing columns
            cursor.execute("PRAGMA table_info(users)")
            columns = [column[1] for column in cursor.fetchall()]
            if 'full_name' not in columns:
                cursor.execute("ALTER TABLE users ADD COLUMN full_name VARCHAR(100) DEFAULT '';")
            if 'medical_license_number' not in columns:
                cursor.execute("ALTER TABLE users ADD COLUMN medical_license_number VARCHAR(50);")
            if 'is_verified' not in columns:
                cursor.execute("ALTER TABLE users ADD COLUMN is_verified BOOLEAN DEFAULT 0;")

class Migration(migrations.Migration):

    initial = True
    
    dependencies = [
    ]

    operations = [
        migrations.RunPython(add_columns_if_table_exists, reverse_code=migrations.RunPython.noop),
    ]