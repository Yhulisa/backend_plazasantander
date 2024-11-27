from app import app, db
from app.routers import roles_router
from app.routers import users_router
from app.routers import auth_router
from app.routers import health_router
from app.routers import centros_comerciales_router
from app.models import BaseModel


BaseModel.set_session(db.session)

