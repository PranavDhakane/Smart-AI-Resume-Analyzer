# 🚀 Deployment Guide - Smart AI Resume Analyzer

## 📋 **Table of Contents**
1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Option 1: Streamlit Cloud (FREE & EASIEST)](#option-1-streamlit-cloud-free--easiest)
3. [Option 2: Render.com (FREE)](#option-2-rendercom-free)
4. [Option 3: Heroku](#option-3-heroku)
5. [Post-Deployment Configuration](#post-deployment-configuration)

---

## ✅ **Pre-Deployment Checklist**

Before deploying, make sure:

- [ ] You have a GitHub account
- [ ] Your code is pushed to GitHub
- [ ] You have your Google Gemini API Key ready
- [ ] All dependencies are in `requirements.txt`
- [ ] `.env` file is in `.gitignore` (already done ✅)
- [ ] Database files are in `.gitignore` (already done ✅)

---

## 🌟 **Option 1: Streamlit Cloud (FREE & EASIEST) - RECOMMENDED**

### **Why Streamlit Cloud?**
- ✅ **100% FREE** forever
- ✅ **No credit card required**
- ✅ **One-click deployment**
- ✅ **Auto-updates** from GitHub
- ✅ **Built specifically for Streamlit apps**

### **Step-by-Step Deployment:**

#### **1. Prepare Your GitHub Repository**

```bash
# Make sure you're in the project directory
cd Smart-AI-Resume-Analyzer-main

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Ready for deployment"

# Create GitHub repository and push
# Go to github.com and create a new repository named: Smart-AI-Resume-Analyzer
# Then run:
git remote add origin https://github.com/PranavDhakane/Smart-AI-Resume-Analyzer.git
git branch -M main
git push -u origin main
```

#### **2. Sign Up for Streamlit Cloud**

1. Go to: **https://streamlit.io/cloud**
2. Click **"Sign up"** or **"Get started"**
3. Sign in with your **GitHub account**
4. Authorize Streamlit Cloud to access your repositories

#### **3. Deploy Your App**

1. Click **"New app"** button
2. Select:
   - **Repository**: `PranavDhakane/Smart-AI-Resume-Analyzer`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Click **"Advanced settings"** (Important!)

#### **4. Configure Secrets (API Keys)**

In the **"Secrets"** section, add your API key in TOML format:

```toml
GOOGLE_API_KEY = "your_actual_google_gemini_api_key_here"
```

**How to get your API Key:**
- Visit: https://aistudio.google.com/app/apikey
- Create/copy your API key
- Paste it in the secrets section

#### **5. Deploy!**

1. Click **"Deploy!"** button
2. Wait 2-5 minutes for deployment
3. Your app will be live at: `https://your-app-name.streamlit.app`

#### **6. Update Code to Use Streamlit Secrets**

After deployment, you need to update your code to read from Streamlit secrets:

**Current code** (in `utils/.env`):
```
GOOGLE_API_KEY=YOUR_KEY_HERE
```

**Will be read by app using** `python-dotenv` for local, and Streamlit secrets for cloud.

The app already handles this! ✅

---

## 🎨 **Option 2: Render.com (FREE)**

### **Step 1: Prepare Files**

Create `render.yaml` in project root:

```yaml
services:
  - type: web
    name: smart-resume-analyzer
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: GOOGLE_API_KEY
        sync: false
```

### **Step 2: Deploy**

1. Go to: **https://render.com**
2. Sign up with GitHub
3. Click **"New +"** → **"Web Service"**
4. Select your repository
5. Configure:
   - **Name**: smart-resume-analyzer
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
6. Add Environment Variable:
   - **Key**: `GOOGLE_API_KEY`
   - **Value**: Your Google Gemini API key
7. Click **"Create Web Service"**

---

## 🔧 **Option 3: Heroku**

### **Files Already Present:**
- ✅ `Procfile` - Already exists
- ✅ `setup.sh` - Already exists
- ✅ `requirements.txt` - Already exists

### **Step 1: Install Heroku CLI**

**Windows:**
Download from: https://devcenter.heroku.com/articles/heroku-cli

### **Step 2: Deploy**

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create pranav-resume-analyzer

# Set environment variables
heroku config:set GOOGLE_API_KEY=your_api_key_here

# Add buildpacks
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python

# Deploy
git push heroku main

# Open app
heroku open
```

---

## ⚙️ **Post-Deployment Configuration**

### **1. Update URLs in Code**

After deployment, update these URLs in your code:

**In `README.md`:**
```markdown
Live Demo: https://your-app.streamlit.app
```

**In social media links:** (if needed)
Update any hardcoded URLs to point to your deployed app.

### **2. Test All Features**

After deployment, test:
- [ ] Resume upload (PDF/DOCX)
- [ ] AI Analysis (requires API key)
- [ ] Resume Builder
- [ ] Admin Login
- [ ] Dashboard
- [ ] Job Search
- [ ] Feedback system

### **3. Monitor Usage**

**For Streamlit Cloud:**
- Check analytics at: https://streamlit.io/cloud
- Monitor app health
- View logs

**For Heroku:**
```bash
heroku logs --tail
```

---

## 🔐 **Security Best Practices**

### **Before Going Live:**

1. **Change Default Admin Password:**
   ```python
   # Don't use admin@example.com / admin123 in production
   ```

2. **Use Strong API Keys:**
   - Don't share your Google Gemini API key
   - Set usage limits in Google Cloud Console

3. **Enable Rate Limiting:**
   - Monitor API usage
   - Set request limits

4. **Database Backup:**
   - Regularly backup `resume_data.db`
   - Use cloud storage for persistence

---

## 📊 **Monitoring & Maintenance**

### **Check App Health:**

**Streamlit Cloud:**
- Dashboard shows app status
- Email notifications for errors

**Heroku:**
```bash
heroku ps
heroku logs --tail
```

### **Update Deployment:**

```bash
# Make changes to your code
git add .
git commit -m "Update features"
git push origin main

# Streamlit Cloud auto-deploys ✅
# For Heroku:
git push heroku main
```

---

## 🆘 **Troubleshooting**

### **Common Issues:**

1. **App won't start:**
   - Check `requirements.txt` has all dependencies
   - Verify Python version compatibility

2. **API errors:**
   - Verify API key is correctly set in secrets
   - Check API key is active in Google Cloud

3. **Database issues:**
   - SQLite works for development
   - For production, consider PostgreSQL

4. **Memory issues:**
   - Streamlit Cloud: 1GB limit (free tier)
   - Optimize large file processing

---

## 📞 **Support**

If you encounter issues:
1. Check Streamlit Cloud documentation
2. Visit: https://discuss.streamlit.io
3. GitHub Issues: Your repository issues page

---

## 🎉 **Your App is Live!**

Once deployed, share your app:
- **LinkedIn**: Post about your project
- **GitHub README**: Add live demo link
- **Resume**: Add as a project with live link

**Example Live URL:**
```
https://smart-resume-analyzer.streamlit.app
```

---

**Good luck with deployment! 🚀**
