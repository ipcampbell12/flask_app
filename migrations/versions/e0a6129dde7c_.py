"""empty message

Revision ID: e0a6129dde7c
Revises: 9712c42bb030
Create Date: 2021-11-24 10:09:45.397721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a6129dde7c'
down_revision = '9712c42bb030'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scores',
                    sa.Column('teacher_id', sa.Integer(), nullable=False),
                    sa.Column('student_id', sa.Integer(), nullable=False),
                    sa.Column('standard_id', sa.Integer(), nullable=False),
                    sa.Column('score', sa.Integer(), nullable=False),
                    sa.Column('test_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['standard_id'], ['standards.id'], ),
                    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
                    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
                    sa.PrimaryKeyConstraint(
                        'teacher_id', 'student_id', 'standard_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scores')
    # ### end Alembic commands ###