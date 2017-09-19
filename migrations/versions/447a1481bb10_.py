"""
Add created at columns, name to item

Revision ID: 447a1481bb10
Revises: 06482b687bae
Create Date: 2017-09-18 21:21:03.350671

"""

# revision identifiers, used by Alembic.
revision = '447a1481bb10'
down_revision = '06482b687bae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('item', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('item', sa.Column('name', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    op.drop_column('item', 'name')
    op.drop_column('item', 'created_at')
    op.drop_column('category', 'created_at')
    ### end Alembic commands ###
