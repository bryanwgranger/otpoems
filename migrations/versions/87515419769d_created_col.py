"""created col

Revision ID: 87515419769d
Revises: b390b0fc6f31
Create Date: 2023-03-21 21:20:59.039619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87515419769d'
down_revision = 'b390b0fc6f31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poem', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poem', schema=None) as batch_op:
        batch_op.drop_column('created')

    # ### end Alembic commands ###