# Deployment setup

## Frontend (web)
- Hosted on **Vercel** (Free Hobby plan).
- Auto-deploys on every push to `main`.
- Environment variables managed in Vercel dashboard.
- Preview deployments created for pull requests.

## Backend (api)
- Hosted on **Render** (Free Web Service plan).
- Defined in `render.yaml`:
  - Dockerfile in `api/`
  - Port `8000`
  - Connected to GitHub for auto-deploy on push to `main`.
- Secrets (`DATABASE_URL`, `REDIS_URL`) configured in Render dashboard.

## Environments
- **Staging** = `main` branch
- **Production** = manual promotion or separate service if needed