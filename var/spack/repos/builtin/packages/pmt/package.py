# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Pmt(CMakePackage):
    """A multi-runtime implementation of a distributed merge tree
       segmentation algorithm. The implementation relies on the
       framework BabelFlow, which allows to execute the algorithm
       on different runtime systems.

       This package supports using PMT in Ascent."""

    homepage = "https://bitbucket.org/cedmav/parallelmergetree"
    url      = "https://bitbucket.org/cedmav/parallelmergetree/get/ascent.zip"

    maintainers = ['spetruzza']

    version('develop',
            git='https://bitbucket.org/cedmav/parallelmergetree.git',
            branch='ascent',
            commit='5de031d43eee2906667a875e4c6abdf99fad8b09',
            submodules=True,
            preferred=True)

    depends_on('babelflow@develop')

    variant("shared", default=True, description="Build ParallelMergeTree as shared libs")

    def cmake_args(self):
      args = []

      args.append('-DLIBRARY_ONLY=ON')

      return args

    def cmake_install(self, spec, prefix):
        
        if "+shared" in spec:
            cmake_args.append('-DBUILD_SHARED_LIBS=ON')
        else:
            cmake_args.append('-DBUILD_SHARED_LIBS=OFF')

        make()
        make('install')
