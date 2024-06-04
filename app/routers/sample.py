# FastAPI & SQLAlchemy imports
from fastapi import APIRouter, Response, status, Depends
from sqlalchemy.orm import Session

# Optional imports
from sqlalchemy import func
from typing import Optional, List

# Local application imports
from .. import database, models, schemas, oauth2

# Initialize (edit prefix & tags)
pool = database.get_pool()
router = APIRouter(
    prefix="/samples",
    tags=['Sample']
)

# Samples (Edit from here)
# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.SampleResponse)
def create_posts(sample_input: schemas.SampleCreate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_sample = models.Sample(owner_id=current_user.id, **sample_input.model_dump())

    db.add(new_sample)
    db.commit()
    db.refresh(new_sample)

    return new_sample

# Read
    # Read All
@router.get("/", response_model=List[schemas.SampleResponse])
def get_sample(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    joined = db.query(models.Sample, func.count(models.CompositeSample.sample_id).label("composite_samples")).join(models.CompositeSample, models.CompositeSample.sample_id == models.Sample.sample_id, isouter=True).group_by(models.Sample.sample_id)
    filtered = joined.filter(models.Sample.string_field.contains(search)).limit(limit).offset(skip)
    sample = filtered.all()

    return sample
    # Read My
@router.get("/my", response_model=List[schemas.SampleResponse])
def get_sample(db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    joined = db.query(models.Sample, func.count(models.CompositeSample.sample_id).label("composite_samples")).join(models.CompositeSample, models.CompositeSample.sample_id == models.Sample.sample_id, isouter=True).group_by(models.Sample.sample_id)
    filtered = joined.filter(models.Sample.owner_id == current_user.user_id)
    sample = filtered.all()

    return sample

    # Read Id
@router.get("/{id}", response_model=schemas.SampleResponse)
def get_post(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    joined = db.query(models.Sample, func.count(models.CompositeSample.sample_id).label("composite_samples")).join(models.CompositeSample, models.CompositeSample.sample_id == models.Sample.sample_id, isouter=True).group_by(models.Sample.sample_id)
    filtered = joined.filter(models.Sample.sample_id == id)
    sample = filtered.one()

    # not available
    
    return sample

# Update
@router.put("/{id}", response_model=schemas.SampleResponse)
def get_post(id: int, sample_input: schemas.SampleUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    
    joined = db.query(models.Sample, func.count(models.CompositeSample.sample_id).label("composite_samples")).join(models.CompositeSample, models.CompositeSample.sample_id == models.Sample.sample_id, isouter=True).group_by(models.Sample.sample_id)
    filtered = joined.filter(models.Sample.sample_id == id)
    sample = filtered.one()

    # sample not available
    # sample is it mine

    filtered.updated(**sample_input.model_dump(), synchronize_session=False)
    db.commit()
    
    return filtered.first()

# Delete
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get_post(id: int, sample_input: schemas.SampleUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    
    joined = db.query(models.Sample, func.count(models.CompositeSample.sample_id).label("composite_samples")).join(models.CompositeSample, models.CompositeSample.sample_id == models.Sample.sample_id, isouter=True).group_by(models.Sample.sample_id)
    filtered = joined.filter(models.Sample.sample_id == id)
    sample = filtered.one()

    # sample not available
    # sample is it mine
    # deleted

    filtered.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)