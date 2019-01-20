"""id

Revision ID: 88ce6a52739e
Revises: 65e0be0aea04
Create Date: 2019-01-15 16:53:31.379803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88ce6a52739e'
down_revision = '65e0be0aea04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'supplier', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'supplier', type_='foreignkey')
    op.drop_column('supplier', 'user_id')
    # ### end Alembic commands ###