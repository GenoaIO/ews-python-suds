#!/usr/bin/python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the (LGPL) GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the 
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library Lesser General Public License for more details at
# ( http://www.gnu.org/licenses/lgpl.html ).
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# written by: Jeff Ortel ( jortel@redhat.com )

import sys
import suds
from setuptools import setup, find_packages

version = 0.003

setup(
    name="ews-python-suds",
    #version=suds.__version__,
    version=version,
    description="Fork of Lightweight SOAP client",
    author="Robert Betts",
    author_email="robert.betts@navohpartners.com",
    maintainer="Robert Betts ",
    maintainer_email="robert.betts@navohpartners.com",
    url="https://github.com/navohpartners/ews-python-suds",
    packages=find_packages('src',exclude=['*tests*', '*ntlm-examples*']),
    package_dir = {'':'src'},
    install_requires = [
        'setuptools',
        'tornado>=3.1.1',
      ],    
)
