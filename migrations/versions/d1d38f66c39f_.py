"""empty message

Revision ID: d1d38f66c39f
Revises: eec17fb24a4b
Create Date: 2022-05-09 16:07:40.941421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1d38f66c39f'
down_revision = 'eec17fb24a4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['author_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'author_id')
    op.drop_table('author')
    # ### end Alembic commands ###
