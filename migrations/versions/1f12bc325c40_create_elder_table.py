"""create Elder table

Revision ID: 1f12bc325c40
Revises: 7dcfc4efb808
Create Date: 2023-09-15 10:43:08.702476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f12bc325c40'
down_revision = '7dcfc4efb808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elder',
    sa.Column('full_name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('is_alone', sa.Boolean(), nullable=True),
    sa.Column('gender', sa.String(length=1), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('pincode', sa.Integer(), nullable=True),
    sa.Column('landmark', sa.String(length=64), nullable=True),
    sa.Column('illness', sa.Text(), nullable=True),
    sa.Column('client_relationship', sa.String(length=32), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('contact_number', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('elder')
    # ### end Alembic commands ###
