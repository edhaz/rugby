"""Add nullable

Revision ID: 5567d853b236
Revises: 124118afe226
Create Date: 2019-06-03 19:48:19.956711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5567d853b236'
down_revision = '124118afe226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stats', 'place',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'round_no',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('stats', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stats', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stats', 'round_no',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('stats', 'place',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
