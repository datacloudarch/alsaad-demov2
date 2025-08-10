AL Saad Football Club – Analytics Web App

Monorepo with a FastAPI backend and React + Vite frontend. Designed for deployment to Azure App Service with Azure SQL Database.

Project structure

```
alsaad-demov2/
├─ backend/
│  ├─ app/
│  │  ├─ api/v1/routes/
│  │  ├─ core/
│  │  ├─ models/
│  │  ├─ schemas/
│  │  ├─ services/
│  │  └─ utils/
│  ├─ tests/
│  ├─ requirements.txt
│  └─ .env.example
├─ frontend/
│  ├─ public/
│  ├─ src/
│  ├─ package.json
│  ├─ tsconfig.json
│  └─ vite.config.ts
└─ .github/workflows/
   ├─ backend.yml
   └─ frontend.yml
```

Quick start

- Backend
  - Create a virtualenv, install requirements, run the API:
    ```bash
    cd backend
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
- Frontend
  - Install and run dev server:
    ```bash
    cd frontend
    npm ci
    npm run dev
    ```

Deployment

- Uses GitHub Actions to deploy `backend` and `frontend` directories to separate Azure App Services.
- Set repository secrets: `AZURE_WEBAPP_BACKEND_NAME`, `AZURE_WEBAPP_BACKEND_PUBLISH_PROFILE`, `AZURE_WEBAPP_FRONTEND_NAME`, `AZURE_WEBAPP_FRONTEND_PUBLISH_PROFILE`.
- Backend expects `DATABASE_URL` in environment (see `backend/.env.example`).


