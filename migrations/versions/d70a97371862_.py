"""empty message

Revision ID: d70a97371862
Revises: de4a1ea122c9
Create Date: 2019-06-18 20:19:17.342218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70a97371862'
down_revision = 'de4a1ea122c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('team_id', sa.Integer(), nullable=False))
    op.drop_constraint('stats_round_id_key', 'stats', type_='unique')
    op.drop_constraint('stats_user_id_fkey', 'stats', type_='foreignkey')
    op.create_foreign_key(None, 'stats', 'team', ['team_id'], ['id'])
    op.drop_column('stats', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'stats', type_='foreignkey')
    op.create_foreign_key('stats_user_id_fkey', 'stats', 'team', ['user_id'], ['id'])
    op.create_unique_constraint('stats_round_id_key', 'stats', ['round_id'])
    op.drop_column('stats', 'team_id')
    # ### end Alembic commands ###
