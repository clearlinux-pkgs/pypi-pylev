#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pylev
Version  : 1.4.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/11/f2/404d2bfa30fb4ee7c7a7435d593f9f698b25d191cafec69dd0c726f02f11/pylev-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/f2/404d2bfa30fb4ee7c7a7435d593f9f698b25d191cafec69dd0c726f02f11/pylev-1.4.0.tar.gz
Summary  : A pure Python Levenshtein implementation that's not freaking GPL'd.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pylev-license = %{version}-%{release}
Requires: pypi-pylev-python = %{version}-%{release}
Requires: pypi-pylev-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
pylev
=====
A pure Python Levenshtein implementation that's not freaking GPL'd.
Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

%package license
Summary: license components for the pypi-pylev package.
Group: Default

%description license
license components for the pypi-pylev package.


%package python
Summary: python components for the pypi-pylev package.
Group: Default
Requires: pypi-pylev-python3 = %{version}-%{release}

%description python
python components for the pypi-pylev package.


%package python3
Summary: python3 components for the pypi-pylev package.
Group: Default
Requires: python3-core
Provides: pypi(pylev)

%description python3
python3 components for the pypi-pylev package.


%prep
%setup -q -n pylev-1.4.0
cd %{_builddir}/pylev-1.4.0
pushd ..
cp -a pylev-1.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398473
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pylev
cp %{_builddir}/pylev-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pylev/f3f2d5fbc62ee1d87e537bd07762d09671b3d7b0
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pylev/f3f2d5fbc62ee1d87e537bd07762d09671b3d7b0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
