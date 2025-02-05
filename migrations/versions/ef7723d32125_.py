"""empty message

Revision ID: ef7723d32125
Revises: 
Create Date: 2023-03-12 23:36:02.327336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef7723d32125'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.alter_column('property_title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('no_of_rooms',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               nullable=True)
        batch_op.alter_column('no_of_bath',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               nullable=True)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(),
               type_=sa.Text(),
               nullable=True)
        batch_op.alter_column('property_type',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               nullable=True)
        batch_op.alter_column('photo',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['property_title'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('photo',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('property_type',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.Text(),
               type_=sa.NUMERIC(),
               nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('no_of_bath',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('no_of_rooms',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('property_title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
