from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, URL
from utils import generate_short_code

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def shorten_url(long_url: str, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    # Make sure the short code is unique
    while db.query(URL).filter(URL.short_code == short_code).first() is not None:
        short_code = generate_short_code()

    new_url = URL(long_url=long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if url:
        return RedirectResponse(url.long_url)
    raise HTTPException(status_code=404, detail="Short URL not found")
