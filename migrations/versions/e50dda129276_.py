"""empty message

Revision ID: e50dda129276
Revises: 44b12e46589c
Create Date: 2019-10-11 16:15:36.401478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e50dda129276'
down_revision = '44b12e46589c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('business_name', sa.String(length=255), nullable=False))
    op.drop_index('shop_name', table_name='account')
    op.create_unique_constraint(None, 'account', ['business_name'])
    op.drop_column('account', 'shop_name')
    op.add_column('user', sa.Column('account_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('location_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'account', ['account_id'], ['id'])
    op.create_foreign_key(None, 'user', 'location', ['location_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'location_id')
    op.drop_column('user', 'account_id')
    op.add_column('account', sa.Column('shop_name', mysql.VARCHAR(length=255), nullable=False))
    op.drop_constraint(None, 'account', type_='unique')
    op.create_index('shop_name', 'account', ['shop_name'], unique=True)
    op.drop_column('account', 'business_name')
    # ### end Alembic commands ###