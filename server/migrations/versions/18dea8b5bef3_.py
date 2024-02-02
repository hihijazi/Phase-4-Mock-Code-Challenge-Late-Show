"""empty message

Revision ID: 18dea8b5bef3
Revises: 584099051e86
Create Date: 2024-02-01 19:38:57.330482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18dea8b5bef3'
down_revision = '584099051e86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.drop_column('occupation')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('occupation', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###