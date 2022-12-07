import setuptools


setuptools.setup(
    name="musiclang",
    version="0.0.1",
    author="Florian GARDIN",
    author_email="fgardin.pro@gmail.com",
    description=("A python package for music notation and generation"
                ),
    long_description="A python package for music notation and generation",
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "Cython==0.29.32",
        "grpcio==1.50.0",
        "h5py==3.7.0",
        "idna==3.3",
        "lxml==4.9.1",
        "miditok==1.3.1",
        "miditoolkit==0.1.16",
        "mido==1.2.10",
        "mlflow==2.0.1",
        "music21==8.1.0",
        "networkx==2.8.7",
        "numpy==1.23.4",
        "pandas==1.5.1",
        "partitura==1.1.1",
        "pytest==7.2.0",
        "scikit-learn==1.1.3",
        "scipy==1.9.3",
        "tensorflow==2.11.0",
        "tensorflow-estimator==2.11.0",
        "tensorflow-io-gcs-filesystem==0.28.0",
        "toml==0.10.2",
        "tomli==2.0.1",
        "tornado==6.2",
        "tqdm==4.64.1",
        "traitlets==5.5.0",
        "typing_extensions==4.4.0",
        "urllib3==1.26.13",
        "wcwidth==0.2.5",
        "webcolors==1.12",
        "webencodings==0.5.1",
        "websocket-client==1.4.2",
        "Werkzeug==2.2.2",
        "widgetsnbextension==4.0.3",
        "wrapt==1.14.1",
        "xmlschema==2.1.1",
        "zipp==3.11.0"
                      ],
    packages=setuptools.find_packages(include='*'),
    package_data={'musiclang': ['augmented_net/*.hdf5']},
    include_package_data=True,
    python_requires=">=3.6",
)