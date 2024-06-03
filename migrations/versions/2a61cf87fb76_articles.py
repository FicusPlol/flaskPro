"""Articles.

Revision ID: 2a61cf87fb76
Revises: ebf74091dd4e
Create Date: 2024-05-24 23:28:18.992462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a61cf87fb76'
down_revision = 'ebf74091dd4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts.css',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('data_post', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(length=60), nullable=False),
    sa.Column('image_post', sa.String(length=30), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts.css')
    # ### end Alembic commands ###
