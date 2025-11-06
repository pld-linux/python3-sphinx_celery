#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Sphinx Celery theme
Summary(pl.UTF-8):	Motyw Celery dla Sphinksa
Name:		python3-sphinx_celery
Version:	2.1.3
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_celery/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-celery/sphinx_celery-%{version}.tar.gz
# Source0-md5:	ad5def066a18bf2e2eef7d94634ee598
URL:		https://pypi.org/project/sphinx-celery/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:59.2.0
%if %{with tests}
BuildRequires:	python3-Sphinx >= 2.0.0
BuildRequires:	python3-pynose
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides the Celery Sphinx theme and common Sphinx
utilities.

%description -l pl.UTF-8
Ten projekt zawiera motyw oraz wspólne narzędzia Sphiksa dla projektu
Celery.

%prep
%setup -q -n sphinx_celery-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m nose sphinx_celery
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog LICENSE README.rst
%{py3_sitescriptdir}/sphinx_celery
%{py3_sitescriptdir}/sphinx_celery-%{version}-py*.egg-info
