#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-future
Version  : 0.16.0
Release  : 9
URL      : https://github.com/PythonCharmers/python-future/archive/v0.16.0.tar.gz
Source0  : https://github.com/PythonCharmers/python-future/archive/v0.16.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-future-bin
Requires: python-future-python3
Requires: python-future-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the python-future package.
Group: Binaries

%description bin
bin components for the python-future package.


%package python
Summary: python components for the python-future package.
Group: Default
Requires: python-future-python3

%description python
python components for the python-future package.


%package python3
Summary: python3 components for the python-future package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-future package.


%prep
%setup -q -n python-future-0.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299159
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/futurize
/usr/bin/pasteurize

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
