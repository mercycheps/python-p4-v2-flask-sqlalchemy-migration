"""Initial migration.

Revision ID: 222b9e00b125
Revises: 
Create Date: 2025-06-11 12:04:03.957998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222b9e00b125'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
