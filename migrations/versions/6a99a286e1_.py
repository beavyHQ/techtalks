"""empty message

Revision ID: 6a99a286e1
Revises: 44f6d7926bf
Create Date: 2015-09-11 23:31:26.111693

"""

# revision identifiers, used by Alembic.
revision = '6a99a286e1'
down_revision = '44f6d7926bf'

# add this here in order to use revision with branch_label
branch_labels = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activities', sa.Column('object_id', sa.Integer(), nullable=True))
    op.add_column('activities', sa.Column('subject_id', sa.Integer(), nullable=True))
    op.add_column('activities', sa.Column('whom_id', sa.Integer(), nullable=True))
    op.drop_constraint('activities_subject_fkey', 'activities', type_='foreignkey')
    op.drop_constraint('activities_whom_fkey', 'activities', type_='foreignkey')
    op.drop_constraint('activities_object_fkey', 'activities', type_='foreignkey')
    op.create_foreign_key(None, 'activities', 'user', ['whom_id'], ['id'])
    op.create_foreign_key(None, 'activities', 'user', ['subject_id'], ['id'])
    op.create_foreign_key(None, 'activities', 'objects', ['object_id'], ['id'])
    op.drop_column('activities', 'object')
    op.drop_column('activities', 'whom')
    op.drop_column('activities', 'subject')
    op.add_column('objects', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_constraint('objects_owner_fkey', 'objects', type_='foreignkey')
    op.create_foreign_key(None, 'objects', 'user', ['owner_id'], ['id'])
    op.drop_column('objects', 'owner')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('owner', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'objects', type_='foreignkey')
    op.create_foreign_key('objects_owner_fkey', 'objects', 'user', ['owner'], ['id'])
    op.drop_column('objects', 'owner_id')
    op.add_column('activities', sa.Column('subject', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('activities', sa.Column('whom', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('activities', sa.Column('object', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'activities', type_='foreignkey')
    op.drop_constraint(None, 'activities', type_='foreignkey')
    op.drop_constraint(None, 'activities', type_='foreignkey')
    op.create_foreign_key('activities_object_fkey', 'activities', 'objects', ['object'], ['id'])
    op.create_foreign_key('activities_whom_fkey', 'activities', 'user', ['whom'], ['id'])
    op.create_foreign_key('activities_subject_fkey', 'activities', 'user', ['subject'], ['id'])
    op.drop_column('activities', 'whom_id')
    op.drop_column('activities', 'subject_id')
    op.drop_column('activities', 'object_id')
    ### end Alembic commands ###