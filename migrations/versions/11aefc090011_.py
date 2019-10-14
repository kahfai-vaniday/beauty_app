"""empty message

Revision ID: 11aefc090011
Revises: e50dda129276
Create Date: 2019-10-11 16:24:13.340107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11aefc090011'
down_revision = 'e50dda129276'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'account', 'user', ['creator_id'], ['id'])
    op.add_column('location', sa.Column('creator_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'location', 'user', ['creator_id'], ['id'])
    op.drop_constraint('user_ibfk_1', 'user', type_='foreignkey')
    op.drop_constraint('user_ibfk_2', 'user', type_='foreignkey')
    op.drop_column('user', 'location_id')
    op.drop_column('user', 'account_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('account_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('location_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('user_ibfk_2', 'user', 'location', ['location_id'], ['id'])
    op.create_foreign_key('user_ibfk_1', 'user', 'account', ['account_id'], ['id'])
    op.drop_constraint(None, 'location', type_='foreignkey')
    op.drop_column('location', 'creator_id')
    op.drop_constraint(None, 'account', type_='foreignkey')
    op.drop_column('account', 'creator_id')
    # ### end Alembic commands ###
