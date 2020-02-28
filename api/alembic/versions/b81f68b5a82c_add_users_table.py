"""add users table

Revision ID: b81f68b5a82c
Revises: 
Create Date: 2020-02-19 16:50:07.822828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81f68b5a82c'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), unique=True),
        sa.Column('password', sa.String(70))
    )
    pass


def downgrade():
    op.drop_table('Users')
