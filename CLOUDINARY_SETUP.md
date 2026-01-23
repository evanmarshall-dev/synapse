# Cloudinary Setup for Heroku Deployment

## 1. Create a Free Cloudinary Account

1. Go to [cloudinary.com](https://cloudinary.com/)
2. Sign up for a free account
3. After signing in, go to your **Dashboard**
4. You'll see your credentials:
   - **Cloud Name**
   - **API Key**
   - **API Secret**

## 2. Configure Heroku Environment Variables

Run these commands in your terminal (replace with your actual Cloudinary credentials):

```bash
heroku config:set CLOUDINARY_CLOUD_NAME=your_cloud_name
heroku config:set CLOUDINARY_API_KEY=your_api_key
heroku config:set CLOUDINARY_API_SECRET=your_api_secret
heroku config:set ON_HEROKU=1
```

## 3. Deploy to Heroku

```bash
git add .
git commit -m "Add Cloudinary for media file storage"
git push heroku main
```

## 4. Local Development (Optional)

If you want to test Cloudinary locally, create a `.env` file in the project root:

```
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
ON_HEROKU=1
```

Otherwise, your local development will continue to use the `uploads/` folder.

## 5. Free Tier Limits

- 25 GB storage (free forever)
- 25 GB bandwidth/month (free forever)
- Automatic image optimization and CDN

Perfect for student projects! 🎓
