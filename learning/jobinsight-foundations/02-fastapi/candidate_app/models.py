from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from candidate_app.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    target_job: Mapped[str] = mapped_column(Text, nullable=False)
    