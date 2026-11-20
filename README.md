# Planar Point Patterns

> `planar-point-patterns` is the working repository name. The final package
> name will be selected before the first public release.

This repository hosts the early development of an open-source Python package
for generating synthetic spatial point patterns in two-dimensional Cartesian
coordinates.

The package is intended primarily for scientific simulation. It will implement
simulators for key families of spatial point processes and produce outputs
that integrate naturally with NumPy, Shapely, GeoPandas, and PySAL.

## Motivation

Python currently provides useful but fragmented tools for spatial point-process
simulation. Many packages include selected simulation methods within a broader
toolkit for spatial analysis, geospatial data processing, or a specific
scientific application. Others specialise in a single family of point processes
or provide building blocks for implementing simulators.

To my knowledge, there is no lightweight Python package that provides a
common interface for simulating binomial, Poisson, inhibitory, and cluster
processes and generating regular grids, with NumPy coordinate arrays,
Shapely study windows, and direct integration with GeoPandas and PySAL.

- **pointpats**, part of PySAL, focuses on planar point-pattern analysis and
  also provides Poisson and cluster samplers.
  [Documentation](https://pysal.org/pointpats/)
- **Locan** is designed for single-molecule localisation microscopy. It
  provides fixed-count uniform sampling and simulators for homogeneous Poisson,
  Matérn cluster, and Thomas cluster processes.
  [Simulation tutorial](https://locan.readthedocs.io/en/stable/tutorials/notebooks/Simulate_LocData.html)
- **GeoPandas** provides uniform point sampling and exposes selected
  pointpats samplers for polygons and multipolygons through
  `GeoSeries.sample_points()`.
  [Sampling documentation](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.sample_points.html)
- **SciPy** provides general tools for random sampling and spatial computation.
  Its Poisson disk sampler generates points with a specified minimum separation.
  [Poisson disk sampler](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.PoissonDisk.html)
- **DPPy** specialises in sampling determinantal point processes.
  [Documentation](https://dppy.readthedocs.io/en/latest/)
- **GSTools** is a geostatistics library that simulates spatial random fields.
  These fields can be used to construct random intensity surfaces for Cox processes.
  [Documentation](https://geostat-framework.readthedocs.io/projects/gstools/en/stable/)

In R, spatstat.random provides a broad collection of spatial point-process
simulators, including Poisson, inhibitory, cluster, Cox, and Gibbs models.
Using it from Python through rpy2 requires an R installation.
[spatstat.random](https://cran.r-project.org/package=spatstat.random) ·
[rpy2 requirements](https://rpy2.github.io/doc/latest/html/overview.html#requirements)

## Development approach

The project will implement each simulator directly from published mathematical
definitions and algorithms. Validation will check the statistical properties
of simulated patterns against theoretical expectations, published results,
and existing implementations.

Keeping dependencies limited is a design goal. NumPy, SciPy, and Shapely are
expected to form the initial simulation core. The project will develop and test
integration with GeoPandas and PySAL using the first group of generators.

The project also serves as practical training for the author in scientific
Python development. This learning goal informs some of the package’s design
and implementation decisions.

## Roadmap

✓ Complete · ↻ In progress · ☐ Planned

- ✓ Set up the repository.
- ☐ Set up the package structure and define a common `PointPattern` class.
  Support Shapely `Polygon` and `MultiPolygon` study windows, coordinate reference
  system metadata, and reproducible sampling with a seed or NumPy `Generator`.
- ☐ Implement and validate the first generators for fixed-count uniform
  (binomial), homogeneous Poisson, and inhomogeneous Poisson processes.
- ☐ Use the first group of generators to verify NumPy coordinate output
  and Shapely study-window handling, and to develop and test direct
  integration with GeoPandas and PySAL.
- ☐ Add rectangular and triangular grid generators.
- ☐ Add inhibitory processes, including simple sequential inhibition and
  Matérn type I and II hard-core processes.
- ☐ Add Matérn and Thomas cluster processes.
- ☐ Complete statistical validation, user documentation, and reproducible
  examples.
- ☐ Select the final package name, build the distribution, and publish the
  first release.

## License

This project is licensed under the BSD 3-Clause License.

The license permits use, modification, and redistribution in academic,
commercial, open-source, and proprietary projects. Redistributions must
include the copyright notice, license conditions, and disclaimer. Using the
copyright holder’s or contributors’ names to endorse or promote derived
products requires prior written permission.
