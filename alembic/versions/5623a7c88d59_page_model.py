"""Page model

Revision ID: 5623a7c88d59
Revises: 4e0d604bdcc0
Create Date: 2016-09-22 14:21:20.764456

"""

# revision identifiers, used by Alembic.
revision = '5623a7c88d59'
down_revision = '4e0d604bdcc0'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Page',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('key', sa.Integer(), nullable=False),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('links', sqlalchemy_utils.types.json.JSONType(), nullable=True),
    sa.Column('site_key', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['site_key'], [u'Site.key'], ),
    sa.PrimaryKeyConstraint('key')
    )
    op.create_index(op.f('ix_Page_url'), 'Page', ['url'], unique=False)
    op.add_column(u'Site', sa.Column('url', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'Site', 'url')
    op.drop_index(op.f('ix_Page_url'), table_name='Page')
    op.drop_table('Page')
    ### end Alembic commands ###