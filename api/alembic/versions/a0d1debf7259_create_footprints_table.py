"""create footprints table

Revision ID: a0d1debf7259
Revises: b81f68b5a82c
Create Date: 2020-03-11 17:47:45.646308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0d1debf7259'
down_revision = 'b81f68b5a82c'
branch_labels = None
depends_on = None


def upgrade():
  op.execute("""CREATE TABLE Footprints (
     id SERIAL PRIMARY KEY,
     footprint DOUBLE PRECISION NOT NULL,
     location GEOMETRY(POINT, 4326) NOT NULL,
     emission_date DATE
  )""")

def downgrade():
  op.drop_table('Footprints')
