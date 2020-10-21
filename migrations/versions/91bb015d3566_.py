"""empty message

Revision ID: 91bb015d3566
Revises: cd4ec2a9fd7d
Create Date: 2020-07-10 19:59:21.452186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91bb015d3566'
down_revision = 'cd4ec2a9fd7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('annotation_sentences', sa.Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'annotation_sentences', 'survey_groups', ['group_id'], ['id'])
    op.add_column('survey_groups', sa.Column('survey_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'survey_groups', 'surveys', ['survey_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'survey_groups', type_='foreignkey')
    op.drop_column('survey_groups', 'survey_id')
    op.drop_constraint(None, 'annotation_sentences', type_='foreignkey')
    op.drop_column('annotation_sentences', 'group_id')
    # ### end Alembic commands ###