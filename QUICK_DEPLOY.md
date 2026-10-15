# ⚡ Quick Deployment Guide

## 🚀 Deploy in 10 Minutes (Streamlit Cloud - FREE)

### **Prerequisites:**
- ✅ GitHub account
- ✅ Google Gemini API Key ([Get it here](https://aistudio.google.com/app/apikey))

---

## 📝 **Step-by-Step Process:**

### **1. Push Code to GitHub (5 minutes)**

Open terminal in project folder and run:

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Add remote (replace with your GitHub username)
git remote add origin https://github.com/PranavDhakane/Smart-AI-Resume-Analyzer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Or use the batch file:**
```bash
deploy_to_github.bat
```

---

### **2. Deploy on Streamlit Cloud (3 minutes)**

1. **Go to:** https://streamlit.io/cloud

2. **Sign in** with your GitHub account

3. **Click "New app"** button

4. **Fill in the form:**
   - Repository: `PranavDhakane/Smart-AI-Resume-Analyzer`
   - Branch: `main`
   - Main file path: `app.py`

5. **Click "Advanced settings"**

6. **Add Secrets (IMPORTANT!):**
   ```toml
   GOOGLE_API_KEY = "paste_your_actual_api_key_here"
   ```

7. **Click "Deploy!"**

8. **Wait 2-5 minutes** ⏳

9. **Done!** Your app is live! 🎉

---

### **3. Your Live URL:**

Your app will be available at:
```
https://[your-app-name].streamlit.app
```

Example:
```
https://smart-resume-analyzer.streamlit.app
```

---

## 🔐 **Get Your Google Gemini API Key:**

1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key
4. Paste it in Streamlit Cloud secrets (Step 2.6 above)

---

## ✅ **After Deployment:**

### **Test Your App:**
1. Upload a resume (PDF/DOCX)
2. Try AI Analysis
3. Build a resume
4. Login to admin panel:
   - Email: `dhakanepranav40@gmail.com`
   - Password: `Pranav@12349`

### **Share Your App:**
- Add live demo link to your resume
- Share on LinkedIn
- Update GitHub README with live link

---

## 🔄 **Update Deployed App:**

Whenever you make changes:

```bash
git add .
git commit -m "Update description"
git push origin main
```

Streamlit Cloud **auto-deploys** the changes! ✨

---

## 🆘 **Troubleshooting:**

### **App won't load?**
- Check deployment logs in Streamlit Cloud dashboard
- Verify API key is correctly added to secrets
- Ensure all files are pushed to GitHub

### **API errors?**
- Verify your Google Gemini API key is active
- Check API key format (no quotes or extra spaces)
- Test API key here: https://aistudio.google.com

### **Need help?**
- Streamlit Community: https://discuss.streamlit.io
- Check logs in Streamlit Cloud dashboard

---

## 📊 **What Gets Deployed:**

✅ Resume Analyzer  
✅ AI-Powered Analysis  
✅ Resume Builder (4 templates)  
✅ Job Search  
✅ Admin Dashboard  
✅ Feedback System  

---

## 💰 **Cost:**

**FREE FOREVER! 🎉**
- No credit card needed
- 1GB RAM, 1 CPU core
- Unlimited public apps
- Auto SSL certificate
- Custom domain (optional)

---

## 🎯 **Pro Tips:**

1. **Custom Domain:**
   - Go to app settings in Streamlit Cloud
   - Add your custom domain
   - Update DNS records

2. **Analytics:**
   - Monitor usage in Streamlit Cloud dashboard
   - Track API usage in Google Cloud Console

3. **Updates:**
   - Make changes locally
   - Test thoroughly
   - Push to GitHub
   - Auto-deploys in 2-3 minutes

---

## ✨ **You're All Set!**

Your Smart AI Resume Analyzer is now live and accessible worldwide!

Share it proudly! 🚀
