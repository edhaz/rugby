"""Remove unique from round

Revision ID: 4fc9b4d10ec3
Revises: 512589ee4d52
Create Date: 2019-06-18 20:02:03.181223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fc9b4d10ec3'
down_revision = '512589ee4d52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_stats_place', table_name='stats')
    op.create_index(op.f('ix_stats_place'), 'stats', ['place'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stats_place'), table_name='stats')
    op.create_index('ix_stats_place', 'stats', ['place'], unique=True)
    # ### end Alembic commands ###
