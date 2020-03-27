# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Babelflow(CMakePackage):
    """BabelFlow is an Embedded Domain Specific Language to describes
       algorithms using a task graph abstraction which allows them
       to be executed on top of one of several available runtime systems.

       This package supports using BabelFlow in Ascent."""

    homepage = "https://github.com/sci-visus/BabelFlow"
    url      = "https://github.com/sci-visus/BabelFlow/archive/ascent.zip"

    maintainers = ['spetruzza']

    version('develop',
            git='https://github.com/sci-visus/BabelFlow.git',
            branch='ascent',
            commit='f63ded5698b3a50432fb09c658a9fa21646a9240',
            submodules=True,
            preferred=True)

    depends_on('mpi')

    variant("shared", default=True, description="Build Babelflow as shared libs")

    def cmake_install(self, spec, prefix):
        if "+shared" in spec:
            cmake_args.append('-DBUILD_SHARED_LIBS=ON')
        else:
            cmake_args.append('-DBUILD_SHARED_LIBS=OFF')
        make()
        make('install')
