# Created by pyp2rpm-3.3.5
%global pypi_name cli2

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        1
Summary:        image::
Group:          Development/Python
License:        MIT
URL:            https://yourlabs.io/oss/cli2
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docstring-parser) >= 0.7.1
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setupmeta)
BuildRequires:  python3dist(setuptools)

%description
cli2: Dynamic CLI for Python 3 Expose Python functions or objects with a
minimalist argument typing style, or building your own command try during
runtime.Documentation available on RTFD <>_.Demo cli2 is a little library to
build CLIs, which documentation is available on

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%doc README.rst
%{_bindir}/cli2
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
