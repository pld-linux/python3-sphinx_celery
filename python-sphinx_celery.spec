#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx Celery theme
Summary(pl.UTF-8):	Motyw Celery dla Sphinksa
Name:		python-sphinx_celery
# keep 1.x here for python2/sphinx 1.8 support
Version:	1.4.8
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_celery/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-celery/sphinx_celery-%{version}.tar.gz
# Source0-md5:	85b5a0926ca54f24a5409ee00c63ebde
URL:		https://pypi.org/project/sphinx-celery/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools >= 20.6.7
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.7.1
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools >= 20.6.7
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.7.1
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides the Celery Sphinx theme and common Sphinx
utilities.

%description -l pl.UTF-8
Ten projekt zawiera motyw oraz wspólne narzędzia Sphiksa dla projektu
Celery.

%package -n python3-sphinx_celery
Summary:	Sphinx Celery theme
Summary(pl.UTF-8):	Motyw Celery dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-sphinx_celery
This project provides the Celery sphinx theme and common Sphinx
utilities.

%description -n python3-sphinx_celery -l pl.UTF-8
Ten projekt zawiera motyw oraz wspólne narzędzia Sphiksa dla projektu
Celery.

%prep
%setup -q -n sphinx_celery-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m nose sphinx_celery
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m nose sphinx_celery
%endif
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
%doc Changelog LICENSE README.rst
%{py_sitescriptdir}/sphinx_celery
%{py_sitescriptdir}/sphinx_celery-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_celery
%defattr(644,root,root,755)
%doc Changelog LICENSE README.rst
%{py3_sitescriptdir}/sphinx_celery
%{py3_sitescriptdir}/sphinx_celery-%{version}-py*.egg-info
%endif
