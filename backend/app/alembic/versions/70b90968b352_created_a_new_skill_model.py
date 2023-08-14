"""created a new  skill  model

Revision ID: 70b90968b352
Revises: d4867f3a4c0a
Create Date: 2023-08-14 15:01:56.171832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70b90968b352'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skill',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Python', sa.Integer(), nullable=True),
    sa.Column('OLGA', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('HYSYS', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_skill_HYSYS'), 'skill', ['HYSYS'], unique=False)
    op.create_index(op.f('ix_skill_OLGA'), 'skill', ['OLGA'], unique=False)
    op.create_index(op.f('ix_skill_Python'), 'skill', ['Python'], unique=False)
    op.create_index(op.f('ix_skill_id'), 'skill', ['id'], unique=False)
    op.add_column('item', sa.Column('HYSYS', sa.String(), nullable=True))
    op.create_index(op.f('ix_item_HYSYS'), 'item', ['HYSYS'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_item_HYSYS'), table_name='item')
    op.drop_column('item', 'HYSYS')
    op.drop_index(op.f('ix_skill_id'), table_name='skill')
    op.drop_index(op.f('ix_skill_Python'), table_name='skill')
    op.drop_index(op.f('ix_skill_OLGA'), table_name='skill')
    op.drop_index(op.f('ix_skill_HYSYS'), table_name='skill')
    op.drop_table('skill')
    # ### end Alembic commands ###
