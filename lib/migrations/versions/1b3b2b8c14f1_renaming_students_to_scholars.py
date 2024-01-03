"""Renaming students to scholars

Revision ID: 1b3b2b8c14f1
Revises: 791279dd0760
Create Date: 2024-01-03 23:02:13.956089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b3b2b8c14f1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
