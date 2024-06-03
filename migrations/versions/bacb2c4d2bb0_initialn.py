"""Initialn.

Revision ID: bacb2c4d2bb0
Revises: 
Create Date: 2024-04-24 14:45:44.028287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bacb2c4d2bb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('psw', sa.String(length=500), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('extra__info__profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job', sa.String(length=50), nullable=True),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.Column('github', sa.String(length=100), nullable=True),
    sa.Column('twiter', sa.String(length=100), nullable=True),
    sa.Column('insta', sa.String(length=100), nullable=True),
    sa.Column('facebook', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('prof_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prof_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extra__info__profile')
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###
