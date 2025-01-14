"""empty message

Revision ID: 584099051e86
Revises: bca03f913541
Create Date: 2024-02-01 19:37:34.214198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '584099051e86'
down_revision = 'bca03f913541'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('occupation', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.drop_column('occupation')

    # ### end Alembic commands ###
