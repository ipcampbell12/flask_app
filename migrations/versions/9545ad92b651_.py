"""empty message

Revision ID: 9545ad92b651
Revises: b20725f73388
Create Date: 2021-11-24 10:01:53.099428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9545ad92b651'
down_revision = 'b20725f73388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gradelevel', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=128), nullable=False),
    sa.Column('iep', sa.Boolean(), nullable=False),
    sa.Column('tag', sa.Boolean(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###