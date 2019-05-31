"""empty message

Revision ID: 8ca582fd4644
Revises: 819ffbaf64e3
Create Date: 2019-05-31 11:21:37.608491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca582fd4644'
down_revision = '819ffbaf64e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'email')
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###