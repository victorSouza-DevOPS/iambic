from typing import Optional

from iambic.aws.models import AccessModel


class Path(AccessModel):
    file_path: str


class MaxSessionDuration(AccessModel):
    max_session_duration: int


class Description(AccessModel):
    description: Optional[str] = ""