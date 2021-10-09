#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : metis
Version  : 5.1.0
Release  : 11
URL      : http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
Source0  : http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: metis-bin = %{version}-%{release}
Requires: metis-filemap = %{version}-%{release}
Requires: metis-lib = %{version}-%{release}
Requires: metis-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
This file contains some test graphs and meshes
4elt.graph
copter2.graph
mdual.graph
These are small to medium size graphs corresponding to 2D and 3D
finite element mesh. They can be used as inputs to gpmetis and ndmetis.

%package bin
Summary: bin components for the metis package.
Group: Binaries
Requires: metis-license = %{version}-%{release}
Requires: metis-filemap = %{version}-%{release}

%description bin
bin components for the metis package.


%package dev
Summary: dev components for the metis package.
Group: Development
Requires: metis-lib = %{version}-%{release}
Requires: metis-bin = %{version}-%{release}
Provides: metis-devel = %{version}-%{release}
Requires: metis = %{version}-%{release}

%description dev
dev components for the metis package.


%package filemap
Summary: filemap components for the metis package.
Group: Default

%description filemap
filemap components for the metis package.


%package lib
Summary: lib components for the metis package.
Group: Libraries
Requires: metis-license = %{version}-%{release}
Requires: metis-filemap = %{version}-%{release}

%description lib
lib components for the metis package.


%package license
Summary: license components for the metis package.
Group: Default

%description license
license components for the metis package.


%prep
%setup -q -n metis-5.1.0
cd %{_builddir}/metis-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633801868
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DGKLIB_PATH=../GKlib -DSHARED:BOOL=TRUE
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64"
%cmake .. -DGKLIB_PATH=../GKlib -DSHARED:BOOL=TRUE
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd graphs
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/gpmetis test.mgraph 4
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/gpmetis 4elt.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/gpmetis copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/gpmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/ndmetis 4elt.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/ndmetis copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/mpmetis metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/m2gmetis metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}/usr/lib64:$LD_LIBRARY_PATH %{buildroot}/usr/bin/graphchk 4elt.graph
popd

%install
export SOURCE_DATE_EPOCH=1633801868
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/metis
cp %{_builddir}/metis-5.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/metis/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
pushd clr-build-avx2
%make_install_v3  || :
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
popd
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/lib64/haswell/
cp ./clr-build-avx2/libmetis/*.so %{buildroot}/usr/lib64/haswell

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cmpfillin
/usr/bin/gpmetis
/usr/bin/graphchk
/usr/bin/m2gmetis
/usr/bin/mpmetis
/usr/bin/ndmetis
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/metis.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-metis

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libmetis.so
/usr/lib64/libmetis.so
/usr/share/clear/optimized-elf/e8c86ef12670df71490b8906e2c31c8ff60c11d511d8bed8e5e291dc095b4548

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/metis/a7c3a4f7dcf7a014c7dfdd3f8752d699eb7f7c2e
