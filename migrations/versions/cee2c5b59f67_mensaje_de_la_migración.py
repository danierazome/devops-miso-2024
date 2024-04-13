"""mensaje de la migración

Revision ID: cee2c5b59f67
Revises: 
Create Date: 2024-04-13 09:48:30.086876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cee2c5b59f67'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist',
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('app_uuid', sa.String(length=50), nullable=False),
    sa.Column('blocked_reason', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('ip', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('app_uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist')
    # ### end Alembic commands ###
