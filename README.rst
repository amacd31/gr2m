Python GR2M
===============

|Build Status| |Code Coverage|

Pure Python implementation of the GR2M hydrologic rainfall-runoff model.

Dependencies
------------

Requires Python 2.7 or 3.4 greater.

If Cython is available the Python code will be compiled by Cython during
installation. Running the unit tests requires numpy and pandas. These
dependencies are all optional as the base code is pure Python.

References
----------

Mouelhi, S., Michel, C., Perrin, C., & Andréassian, V. (2006). Stepwise development of a two-parameter monthly water balance model. Journal of Hydrology, 318(1-4), 200-214. http://doi.org/10.1016/j.jhydrol.2005.06.014


Operation of GR2M: http://webgr.irstea.fr/modeles/mensuel-gr2m/fonctionnement-gr2m/?lang=en

.. |Build Status| image:: https://img.shields.io/travis/amacd31/gr2m/master.svg
    :target: https://travis-ci.org/amacd31/gr2m

.. |Code Coverage| image:: https://img.shields.io/coveralls/amacd31/gr2m/master.svg
    :target: https://coveralls.io/github/amacd31/gr2m?branch=master
