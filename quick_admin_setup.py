"""
Quick Admin Setup - One command to set admin credentials
"""
from config.database import add_admin, init_database

# Initialize database first
init_database()

# Add default admin
email = "admin@example.com"
password = "admin123"

try:
    add_admin(email, password)
    print(f"✅ Admin created successfully!")
    print(f"📧 Email: {email}")
    print(f"🔑 Password: {password}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("ℹ️  Admin might already exist. Use add_admin.py to update.")
