"""empty message

Revision ID: f94ab0825cde
Revises: 66ad1c1c360f
Create Date: 2018-10-14 16:44:42.120142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f94ab0825cde'
down_revision = '66ad1c1c360f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('Email', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'Email')
    # ### end Alembic commands ###
