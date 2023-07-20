"""empty message

Revision ID: 74f2419a8e7c
Revises: 
Create Date: 2023-07-18 17:50:27.248007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f2419a8e7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gafetes',
    sa.Column('id_gafete', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tipo', sa.String(length=20), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('prestado', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id_gafete')
    )
    op.create_table('usuarios',
    sa.Column('id_usuario', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('usuario', sa.String(length=20), nullable=False),
    sa.Column('hash', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id_usuario')
    )
    op.create_table('prestamos',
    sa.Column('id_prestamo', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('gafete_id', sa.Integer(), nullable=True),
    sa.Column('nombre_prestamo', sa.String(length=100), nullable=False),
    sa.Column('cedula', sa.String(length=20), nullable=True),
    sa.Column('empresa', sa.String(length=100), nullable=True),
    sa.Column('autoriza', sa.String(length=100), nullable=True),
    sa.Column('hora_inicio', sa.String(length=100), nullable=True),
    sa.Column('hora_fin', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['gafete_id'], ['gafetes.id_gafete'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id_usuario'], ),
    sa.PrimaryKeyConstraint('id_prestamo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prestamos')
    op.drop_table('usuarios')
    op.drop_table('gafetes')
    # ### end Alembic commands ###
