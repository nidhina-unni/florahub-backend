"""updated email and phone field

Revision ID: fa6229d2f0b1
Revises: d2c3e1745673
Create Date: 2025-01-13 08:00:20.841766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa6229d2f0b1'
down_revision = 'd2c3e1745673'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(length=15), nullable=True))
        batch_op.create_unique_constraint(None, ['phone_number'])
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admins', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
