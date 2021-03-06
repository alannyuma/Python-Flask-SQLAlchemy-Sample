"""empty message

Revision ID: b907db3673aa
Revises: None
Create Date: 2016-07-15 21:58:51.044889

"""

# revision identifiers, used by Alembic.
revision = 'b907db3673aa'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('case_subcribers', 'case_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable='false')
    op.alter_column('case_subcribers', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable='false')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('case_subcribers', 'user_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('case_subcribers', 'case_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###
