"""
Admin User Add/Update Script
Run this script to add or update admin credentials
"""
import sqlite3

def add_or_update_admin(email, password):
    """Add or update admin credentials"""
    conn = sqlite3.connect('resume_data.db')
    cursor = conn.cursor()
    
    try:
        # Check if admin exists
        cursor.execute('SELECT id FROM admin WHERE email = ?', (email,))
        existing = cursor.fetchone()
        
        if existing:
            # Update existing admin
            cursor.execute('UPDATE admin SET password = ? WHERE email = ?', (password, email))
            print(f"✅ Admin password updated successfully for: {email}")
        else:
            # Add new admin
            cursor.execute('INSERT INTO admin (email, password) VALUES (?, ?)', (email, password))
            print(f"✅ New admin added successfully: {email}")
        
        conn.commit()
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
    finally:
        conn.close()

def list_admins():
    """List all admin accounts"""
    conn = sqlite3.connect('resume_data.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT id, email, created_at FROM admin')
        admins = cursor.fetchall()
        
        if admins:
            print("\n📋 Current Admin Accounts:")
            print("-" * 50)
            for admin in admins:
                print(f"ID: {admin[0]} | Email: {admin[1]} | Created: {admin[2]}")
        else:
            print("\n⚠️ No admin accounts found.")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("=" * 50)
    print("   ADMIN USER MANAGEMENT")
    print("=" * 50)
    
    # List current admins
    list_admins()
    
    print("\n" + "=" * 50)
    print("   ADD/UPDATE ADMIN")
    print("=" * 50)
    
    email = input("\nEnter admin email: ").strip()
    password = input("Enter admin password: ").strip()
    
    if email and password:
        add_or_update_admin(email, password)
    else:
        print("❌ Email and password cannot be empty!")
    
    print("\n" + "=" * 50)
    list_admins()
    print("=" * 50)
