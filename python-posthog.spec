Name:		python-posthog
Version:	7.53.0
Release:	1
Summary:	PostHog Python analytics SDK
License:	MIT
Group:		Development/Python
URL:		https://github.com/PostHog/posthog-python
Source0:	https://files.pythonhosted.org/packages/source/p/posthog/posthog-%{version}.tar.gz
BuildArch:	noarch
# METADATA floors would fail extra tests if cooker versions differ
%global __requires_exclude ^python[0-9.]*dist\\(
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(backoff)
Requires:	python%{pyver}dist(distro)
Requires:	python%{pyver}dist(typing-extensions)

%description
Official PostHog Python library. Aider uses it for optional telemetry.

# sdist wants setuptools>=83; cooker ships 81
%prep
%autosetup -n posthog-%{version}
sed -i 's/setuptools>=83.0.0/setuptools>=61/' pyproject.toml

%files
%doc README.md
%license LICENSE
%{py_sitedir}/posthog
%{py_sitedir}/posthog-*.*-info
