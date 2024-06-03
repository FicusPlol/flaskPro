"""Articlesnew

Revision ID: ad0f664419cf
Revises: 9e8ad5f63c17
Create Date: 2024-05-29 18:06:45.361209

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ad0f664419cf'
down_revision = '9e8ad5f63c17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.TINYTEXT(),
               type_=sa.Text(length=60),
               existing_nullable=False)
        batch_op.alter_column('image_post',
               existing_type=mysql.VARCHAR(length=30),
               type_=sa.String(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('image_post',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=30),
               existing_nullable=True)
        batch_op.alter_column('content',
               existing_type=sa.Text(length=60),
               type_=mysql.TINYTEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
