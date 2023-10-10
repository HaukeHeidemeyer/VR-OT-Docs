# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VR-OT'
copyright = '2023, Hauke Heidemeyer'
author = 'Hauke Heidemeyer'
import subprocess
subprocess.call('make clean', shell=True)
subprocess.call('cd ../../doxygen ; doxygen', shell=True)
html_extra_path = ['../../doxygen/build/html']