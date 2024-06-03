"""Articlesnew6

Revision ID: bf6b98d36572
Revises: ad0f664419cf
Create Date: 2024-05-30 09:06:20.974287

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf6b98d36572'
down_revision = 'ad0f664419cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=2000),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.Text(length=2000),
               type_=mysql.TINYTEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
