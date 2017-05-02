#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-future
Version  : 0.16.0
Release  : 2
URL      : https://github.com/PythonCharmers/python-future/archive/v0.16.0.tar.gz
Source0  : https://github.com/PythonCharmers/python-future/archive/v0.16.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-future-bin
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

%description python
python components for the python-future package.


%prep
%setup -q -n python-future-0.16.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1485025824
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1485025824
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/futurize
/usr/bin/pasteurize

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
