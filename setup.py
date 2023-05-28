from setuptools import setup

setup(
    name="arbscan-python",
    version="2.0.0",
    description="A python API for arbscan.io.",
    url="https://github.com/pcko1/bscscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "bscscan",
        "bscscan.configs",
        "bscscan.core",
        "bscscan.enums",
        "bscscan.modules",
        "bscscan.utils",
    ],
    python_requires='>=3.8',
    install_requires=["aiohttp", "requests"],
    include_package_data=True,
    zip_safe=False,
)
