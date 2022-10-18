from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from  database import engine
from .routers import post, user, auth, vote, jps
from .config import settings




print(settings.database_username)



#models.Base.metadata.create_all(bind = engine) 

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(jps.router)



#@app.get("/")
#def server():
#    return {'server running well!!!!'}


