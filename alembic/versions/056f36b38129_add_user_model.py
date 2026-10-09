"""Add_user_model.

Revision ID: 056f36b38129
Revises: 
Create Date: 2026-10-08 19:57:53.228102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '056f36b38129'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('surname', sa.String(length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('dni', sa.String(length=20), unique=True, nullable=False),
                    sa.Column('password', sa.String(length=255), nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('users')
