"""type of loading

Revision ID: 94cba751c165
Revises: 0a37398d168c
Create Date: 2019-01-15 07:16:45.321248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94cba751c165'
down_revision = '0a37398d168c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('type_of_loading', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('request', 'type_of_loading')
    # ### end Alembic commands ###
