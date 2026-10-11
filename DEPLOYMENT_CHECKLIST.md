# 🚀 Deployment Checklist

## Before Deploying, Make Sure:

### ✅ Environment Variables
- [ ] Add `GOOGLE_API_KEY` in platform settings
- [ ] Never commit `.env` file to GitHub

### ✅ Security
- [ ] Change default admin password
- [ ] Update admin credentials in database
- [ ] Add `.env` to `.gitignore`

### ✅ Database
- [ ] Ensure `resume_data.db` is in `.gitignore` (don't commit)
- [ ] Database will be created automatically on first run

### ✅ Dependencies
- [ ] All packages in `requirements.txt`
- [ ] spaCy model will auto-download on first run

### ✅ Files to Commit
- [ ] `app.py`
- [ ] `requirements.txt`
- [ ] `Dockerfile` (if using Docker)
- [ ] `Procfile` (if using Heroku)
- [ ] All `.py` files
- [ ] `packages.txt` (for Streamlit Cloud)

### ✅ Files NOT to Commit
- [ ] `.env` files
- [ ] `*.db` files
- [ ] `venv/` folder
- [ ] `__pycache__/` folders
- [ ] `.pyc` files

### ✅ Testing
- [ ] Test locally first
- [ ] Check all features work
- [ ] Test with sample resume

## Platform-Specific:

### Streamlit Cloud
- [ ] Add secrets in dashboard
- [ ] Add `packages.txt` for system dependencies

### AWS EC2
- [ ] Open port 8501 in security group
- [ ] Use screen or systemd for background process

### Heroku
- [ ] Add `Procfile`
- [ ] Add `setup.sh`
- [ ] Set config vars

### Docker
- [ ] Test Docker image locally
- [ ] Push to Docker Hub (optional)
