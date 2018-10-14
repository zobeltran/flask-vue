"""empty message

Revision ID: 2f9cd3035142
Revises: 
Create Date: 2018-10-07 16:08:35.803120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9cd3035142'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('Password', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('Role', sa.String(length=25), nullable=True))
    op.add_column('users', sa.Column('Username', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'Username')
    op.drop_column('users', 'Role')
    op.drop_column('users', 'Password')
    # ### end Alembic commands ###
