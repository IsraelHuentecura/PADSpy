from setuptools import setup, find_packages

setup(
    name='mi_libreria',
    version='0.1.0',
    description='Una descripción breve de mi librería',
    author='Tu Nombre',
    author_email='tu_email@example.com',
    url='https://github.com/tu_usuario/mi_libreria',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
