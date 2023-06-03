"""integer task

Revision ID: b65bf7ac6601
Revises: 8b88edad7246
Create Date: 2023-06-02 00:06:19.939267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b65bf7ac6601'
down_revision = '8b88edad7246'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('level', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('level')

    # ### end Alembic commands ###
