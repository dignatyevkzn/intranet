"""request_day

Revision ID: 0b69b3264b15
Revises: 855cc6a517ee
Create Date: 2019-01-17 05:09:04.914538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b69b3264b15'
down_revision = '855cc6a517ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('pick_up_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('request', 'pick_up_date')
    # ### end Alembic commands ###
