SVG42PDF
========

.. image:: https://badge.fury.io/py/svg42pdf.svg
    :target: https://badge.fury.io/py/svg42pdf

Unlike other graphic formats, SVG is usually hard to convert to PDF.
Existing tools often suffer from the following limitations:

* Do not work on all operating systems
* Versions for different operating systems have different command-line interfaces
* SVG is interpreted incorrectly
* Dependencies are difficult to install
* Have licencing issues

SVG42PDF is a tool for converting SVG to PDF using existing tools and
libraries. Method of conversion can be specified by user, or it can be
selected automatically.


Installation
------------

From PyPI::

	pip install --upgrade svg42pdf

From Github::

	pip install --upgrade git+https://github.com/karel-brinda/svg42pdf


Examples
--------

Use first working method::

	svg42pdf input.svg output.pdf

Use `Cairo <https://cairographics.org/>`_::

	svg42pdf -m cairo input.svg output.pdf

Use `ReportLab <http://www.reportlab.com/>`_::

	svg42pdf -m reportlab input.svg output.pdf

Use `Inkscape <https://inkscape.org>`_::

	svg42pdf -m inkscape input.svg output.pdf

Use `ImageMagick <https://www.imagemagick.org>`_ (does not keep vector representation)::

	svg42pdf -m imagemagick input.svg output.pdf

Use `Wkhtmltopdf <https://wkhtmltopdf.org>`_ (using the Qt WebKit, creates big white margins)::

	svg42pdf -m wkhtmltopdf input.svg output.pdf


FAQ
---

* Why is there 42 in the name?

	There are already too many tools called svg2pdf.

