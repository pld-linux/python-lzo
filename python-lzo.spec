# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	lzo
Summary:	Python bindings for the LZO data compression library
Name:		python-%{module}
Version:	1.12
Release:	1
License:	GPL v2.0+
Group:		Libraries/Python
Source0:	http://ftp.debian.org/debian/pool/main/p/python-lzo/python-lzo_%{version}.orig.tar.xz
# Source0-md5:	a4735228b29f4c40e1a8feff2185f9c0
URL:		https://github.com/jd-boyd/python-lzo
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	lzo-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-LZO provides Python bindings for LZO, i.e. you can access the
LZO library from your Python scripts thereby compressing ordinary
Python strings.

%package -n python3-%{module}
Summary:	Python bindings for the LZO data compression library
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Python-LZO provides Python bindings for LZO, i.e. you can access the
LZO library from your Python scripts thereby compressing ordinary
Python strings.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/*%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{py3_sitedir}/%{module}*.so
%{py3_sitedir}/*%{module}-%{version}-py*.egg-info
%endif
